# ip_scanner_integration.py - IP Scanner Integration for MX-UI
# This file integrates the BBBL Scanner with MX-UI dashboard

import asyncio
import ipaddress
import socket
import threading
import queue
import time
import random
import subprocess
import platform
from datetime import datetime
from typing import List, Dict, Tuple, Optional
import json
import re
from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from main import LINKS, LINKS_LOCK, require_auth, get_host, vless_link_for_link, save_state, log_activity

# ============================================================================
# Data Models
# ============================================================================

class ScanRequest(BaseModel):
    ip_range: str  # e.g., "173.245.48.0/20" or comma separated
    count_per_range: int  # number of IPs to scan per range
    ports: List[int] = [443, 8443, 2053, 2083, 2087, 2096]
    timeout: float = 3.0
    workers: int = 100

class ApplyIPRequest(BaseModel):
    uuid: str
    new_ip: str
    new_port: Optional[int] = None

# ============================================================================
# Scanner Core (Adapted from BBBL Scanner)
# ============================================================================

# Cloudflare CIDR Ranges
CIDR_RANGES = [
    "173.245.48.0/20", "103.21.244.0/22", "103.22.200.0/22",
    "103.31.4.0/22", "141.101.64.0/18", "108.162.192.0/18",
    "190.93.240.0/20", "188.114.96.0/20", "197.234.240.0/22",
    "198.41.128.0/17", "162.158.0.0/15", "104.16.0.0/13",
    "104.24.0.0/14", "172.64.0.0/13", "131.0.72.0/22"
]

CLOUDFLARE_PORTS = {
    80: "HTTP", 443: "HTTPS", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
    2052: "Warp", 2053: "Warp", 2082: "Warp", 2083: "Warp",
    2086: "Warp", 2087: "Warp", 2095: "Warp", 2096: "Warp", 8880: "HTTP-Proxy"
}

router = APIRouter(prefix="/api/ipscanner", tags=["IP Scanner"])

class IPScannerCore:
    def __init__(self):
        self.results = []
        self.lock = threading.Lock()
        self.queue = queue.Queue()
        self.scanned = 0
        self.found = 0
        self.total = 0
        self.is_running = False
        self.progress = 0
        self.status_message = "Idle"

    def test_basic_connectivity(self) -> bool:
        """Test if scanner can connect to known Cloudflare IPs"""
        test_ips = ['1.1.1.1', '8.8.8.8', '104.16.0.1', '172.64.0.1']
        success_count = 0
        for test_ip in test_ips:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                result = sock.connect_ex((test_ip, 443))
                sock.close()
                if result == 0:
                    success_count += 1
            except:
                pass
        return success_count >= 1

    def get_all_ips_from_ranges(self, ranges: List[str]) -> List[str]:
        all_ips = []
        for cidr in ranges:
            try:
                network = ipaddress.ip_network(cidr.strip(), strict=False)
                ips = [str(ip) for ip in network.hosts()]
                all_ips.extend(ips)
            except Exception:
                continue
        return all_ips

    def ping_ip(self, ip: str, timeout: int = 2) -> Tuple[bool, float]:
        try:
            if platform.system().lower() == 'windows':
                command = ['ping', '-n', '1', '-w', str(timeout * 1000), ip]
            else:
                command = ['ping', '-c', '1', '-W', str(timeout), ip]
            
            start_time = time.perf_counter()
            result = subprocess.run(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                timeout=timeout + 1,
                text=True
            )
            end_time = time.perf_counter()
            
            if result.returncode == 0:
                output = result.stdout
                if platform.system().lower() == 'windows':
                    for line in output.split('\n'):
                        if 'time=' in line or 'time<' in line:
                            try:
                                time_str = line.split('time=')[-1].split('ms')[0].strip('<>')
                                ping_time = float(time_str)
                                return True, ping_time
                            except:
                                pass
                else:
                    for line in output.split('\n'):
                        if 'time=' in line:
                            try:
                                time_str = line.split('time=')[-1].split(' ')[0]
                                ping_time = float(time_str)
                                return True, ping_time
                            except:
                                pass
                return True, (end_time - start_time) * 1000
            return False, 0
        except:
            return False, 0

    def scan_port(self, ip: str, port: int, timeout: float) -> Tuple[bool, float]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            start_time = time.perf_counter()
            result = sock.connect_ex((ip, port))
            end_time = time.perf_counter()
            sock.close()
            if result == 0:
                return True, (end_time - start_time) * 1000
            return False, 0
        except:
            return False, 0

    def test_speed(self, ip: str, port: int, timeout: float = 3) -> Dict:
        best_result = {'reachable': False}
        for attempt in range(3):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                start_time = time.perf_counter()
                result = sock.connect_ex((ip, port))
                end_time = time.perf_counter()
                sock.close()
                
                if result == 0:
                    response_time = (end_time - start_time) * 1000
                    if response_time < 50:
                        rating = "EXCELLENT"
                    elif response_time < 100:
                        rating = "GOOD"
                    elif response_time < 200:
                        rating = "AVERAGE"
                    else:
                        rating = "SLOW"
                    
                    if not best_result['reachable'] or response_time < best_result.get('response_time', float('inf')):
                        best_result = {
                            'reachable': True, 
                            'response_time': round(response_time, 2), 
                            'rating': rating, 
                            'port': port
                        }
                    if rating == "EXCELLENT":
                        break
            except:
                pass
        return best_result

    def worker(self, ports: List[int], timeout: float, test_ping: bool, test_speed_enabled: bool):
        while True:
            try:
                ip = self.queue.get_nowait()
            except queue.Empty:
                break
            
            ip_info = {'ip': ip, 'open_ports': [], 'ping': None, 'speed_tests': []}
            
            if test_ping:
                ping_success, ping_time = self.ping_ip(ip, timeout=int(timeout))
                if ping_success:
                    ip_info['ping'] = round(ping_time, 2)
            
            for port in ports:
                try:
                    port_open, response_time = self.scan_port(ip, port, timeout)
                    if port_open:
                        port_info = {
                            'port': port, 
                            'service': CLOUDFLARE_PORTS.get(port, 'Unknown'), 
                            'response_time': round(response_time, 2)
                        }
                        ip_info['open_ports'].append(port_info)
                        
                        if test_speed_enabled:
                            speed_result = self.test_speed(ip, port, timeout * 2)
                            if speed_result['reachable']:
                                ip_info['speed_tests'].append(speed_result)
                except:
                    continue
            
            if ip_info['open_ports']:
                with self.lock:
                    self.results.append(ip_info)
                    self.found += 1
            
            with self.lock:
                self.scanned += 1
            
            self.queue.task_done()

    def scan(self, ranges: List[str], count_per_range: int, ports: List[int], 
             workers: int = 100, timeout: float = 3.0) -> List[Dict]:
        self.results = []
        self.scanned = 0
        self.found = 0
        self.is_running = True
        self.progress = 0
        self.status_message = "Starting scan..."
        
        # Get IPs from ranges
        all_ips = self.get_all_ips_from_ranges(ranges)
        if not all_ips:
            self.status_message = "No IPs found in ranges"
            self.is_running = False
            return []
        
        # Limit IPs per range
        if count_per_range > 0 and count_per_range < len(all_ips):
            scan_ips = random.sample(all_ips, min(count_per_range * len(ranges), len(all_ips)))
        else:
            scan_ips = all_ips
        
        self.total = len(scan_ips)
        
        # Fill queue
        for ip in scan_ips:
            self.queue.put(ip)
        
        # Start workers
        thread_list = []
        for _ in range(min(workers, self.total)):
            t = threading.Thread(target=self.worker, args=(ports, timeout, True, True))
            t.start()
            thread_list.append(t)
        
        # Monitor progress
        start_time = time.time()
        last_scanned = 0
        while any(t.is_alive() for t in thread_list):
            with self.lock:
                current_scanned = self.scanned
                current_found = self.found
            if current_scanned != last_scanned:
                self.progress = (current_scanned / self.total) * 100 if self.total > 0 else 0
                self.status_message = f"Scanning: {current_scanned}/{self.total} IPs, Found: {current_found}"
                last_scanned = current_scanned
            time.sleep(0.1)
        
        for t in thread_list:
            t.join()
        
        self.is_running = False
        self.progress = 100
        self.status_message = f"Scan complete. Found {self.found} clean IPs"
        
        # Sort results by ping
        sorted_results = sorted(
            self.results, 
            key=lambda x: (
                x.get('ping') or 9999,
                min([s.get('response_time', 9999) for s in x.get('speed_tests', [])] or [9999])
            )
        )
        
        return sorted_results

# Global scanner instance
scanner = IPScannerCore()

# ============================================================================
# API Endpoints
# ============================================================================

@router.post("/scan")
async def start_scan(request: ScanRequest, _=Depends(require_auth)):
    """Start a new IP scan"""
    if scanner.is_running:
        raise HTTPException(status_code=409, detail="Scan already in progress")
    
    # Parse IP ranges
    ranges = [r.strip() for r in request.ip_range.split(',') if r.strip()]
    if not ranges:
        raise HTTPException(status_code=400, detail="No IP ranges provided")
    
    # Validate ranges
    valid_ranges = []
    for r in ranges:
        try:
            ipaddress.ip_network(r, strict=False)
            valid_ranges.append(r)
        except Exception:
            pass
    
    if not valid_ranges:
        raise HTTPException(status_code=400, detail="Invalid IP ranges")
    
    # Start scan in background
    asyncio.create_task(run_scan_background(valid_ranges, request))
    
    return {
        "status": "started",
        "message": f"Scan started for {len(valid_ranges)} ranges",
        "total_ips_estimate": sum([2**(32 - int(r.split('/')[-1])) for r in valid_ranges])
    }

async def run_scan_background(ranges: List[str], request: ScanRequest):
    """Run scan in background thread"""
    loop = asyncio.get_event_loop()
    results = await loop.run_in_executor(
        None,
        lambda: scanner.scan(
            ranges=ranges,
            count_per_range=request.count_per_range,
            ports=request.ports,
            workers=request.workers,
            timeout=request.timeout
        )
    )
    # Store results for later retrieval
    scanner.results = results

@router.get("/status")
async def get_scan_status(_=Depends(require_auth)):
    """Get current scan status"""
    return {
        "is_running": scanner.is_running,
        "progress": scanner.progress,
        "scanned": scanner.scanned,
        "total": scanner.total,
        "found": scanner.found,
        "status_message": scanner.status_message
    }

@router.get("/results")
async def get_scan_results(limit: int = 10, _=Depends(require_auth)):
    """Get scan results (top N)"""
    if scanner.is_running:
        raise HTTPException(status_code=409, detail="Scan still in progress")
    
    results = scanner.results[:limit] if limit > 0 else scanner.results
    
    # Format results for display
    formatted = []
    for idx, ip_info in enumerate(results[:10], 1):
        ip = ip_info['ip']
        ping = ip_info.get('ping')
        
        # Get best port
        open_ports = ip_info.get('open_ports', [])
        best_port = None
        best_speed = None
        for port_info in open_ports:
            speed_info = next((s for s in ip_info.get('speed_tests', []) if s.get('port') == port_info['port']), None)
            if speed_info:
                if best_speed is None or speed_info.get('response_time', 9999) < best_speed.get('response_time', 9999):
                    best_speed = speed_info
                    best_port = port_info['port']
            elif best_port is None:
                best_port = port_info['port']
        
        formatted.append({
            "rank": idx,
            "ip": ip,
            "port": best_port or (open_ports[0]['port'] if open_ports else 443),
            "ping": round(ping, 1) if ping else None,
            "speed": round(best_speed.get('response_time', 0), 1) if best_speed else None,
            "rating": best_speed.get('rating') if best_speed else None,
            "all_ports": [p['port'] for p in open_ports]
        })
    
    return {
        "results": formatted,
        "total_found": len(scanner.results),
        "scan_complete": not scanner.is_running
    }

@router.post("/apply")
async def apply_ip_to_config(request: ApplyIPRequest, req: Request, _=Depends(require_auth)):
    """Apply a new IP to a configuration"""
    async with LINKS_LOCK:
        if request.uuid not in LINKS:
            raise HTTPException(status_code=404, detail="Configuration not found")
        
        link = LINKS[request.uuid]
        
        # Check if domain is not railway.app
        host = get_host(req)
        if 'railway.app' in host:
            raise HTTPException(status_code=400, detail="Cannot modify IP on railway.app domain")
        
        # Update the vless link with new IP
        # The IP is embedded in the vless link, we need to regenerate it
        # But we also need to update the actual configuration storage
        
        # Store the custom IP in the link data
        link['custom_ip'] = request.new_ip
        if request.new_port:
            link['custom_port'] = request.new_port
        
        # Regenerate the vless link with the new IP
        new_vless = vless_link_for_link(link, request.uuid, request.new_ip)
        
        log_activity("ipscanner", f"Applied IP {request.new_ip} to config {link.get('label', 'Unknown')}", "info")
    
    await save_state()
    
    return {
        "ok": True,
        "message": f"Applied IP {request.new_ip} to config",
        "uuid": request.uuid,
        "new_vless_link": new_vless
    }

@router.post("/check-domain")
async def check_domain(request: Request, _=Depends(require_auth)):
    """Check if the current domain is suitable for IP modification"""
    host = get_host(request)
    is_railway = 'railway.app' in host
    return {
        "domain": host,
        "is_railway": is_railway,
        "can_modify_ip": not is_railway,
        "message": "Cannot modify IP on railway.app domain" if is_railway else "Domain is suitable for IP modification"
    }

@router.get("/predefined-ranges")
async def get_predefined_ranges(_=Depends(require_auth)):
    """Get predefined Cloudflare ranges"""
    return {"ranges": CIDR_RANGES}

@router.get("/ports")
async def get_common_ports(_=Depends(require_auth)):
    """Get common Cloudflare ports"""
    return {"ports": list(CLOUDFLARE_PORTS.keys())}