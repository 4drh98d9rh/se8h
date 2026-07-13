# pages.py - MX-UI v1.0.0
# All templates with escaped braces for Python .format()

# ---------- LOGIN_HTML ----------
# ---------- LOGIN_HTML (with Persian font support) ----------
LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login · MX-UI</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Vazirmatn:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'Vazirmatn', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #070a13;
        }
        .glow-effect {
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.12);
        }
        @keyframes pulse-slow {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .pulse-slow {
            animation: pulse-slow 2s ease-in-out infinite;
        }
        .input-focus-ring:focus {
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
        }
        @media (max-width: 640px) {
            .mobile-padding {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
        /* Persian font support - Vazirmatn for Persian characters */
        .font-persian {
            font-family: 'Vazirmatn', 'Inter', sans-serif;
        }
        /* Ensure English text still looks good */
        .font-english {
            font-family: 'Inter', 'Vazirmatn', sans-serif;
        }
        /* Mixed content support */
        .font-mixed {
            font-family: 'Inter', 'Vazirmatn', sans-serif;
        }
    </style>
</head>
<body class="font-sans text-slate-200 min-h-screen flex items-center justify-center bg-[#070a13] relative antialiased tracking-tight p-4 mobile-padding">
    
    <!-- Background Effects -->
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_0%,rgba(59,130,246,0.08),transparent_70%)] pointer-events-none"></div>
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_60%_40%_at_50%_100%,rgba(99,102,241,0.05),transparent_70%)] pointer-events-none"></div>
    
    <!-- Grid Pattern Overlay -->
    <div class="absolute inset-0 opacity-[0.03] pointer-events-none" style="background-image: radial-gradient(circle at 1px 1px, #3b82f6 1px, transparent 0); background-size: 24px 24px;"></div>
    
    <div class="w-full max-w-md relative z-10">
        <div class="bg-slate-900/80 border border-slate-800/80 rounded-2xl p-6 sm:p-8 backdrop-blur-xl glow-effect transition-all duration-300 hover:border-slate-700/80">
            
            <!-- Logo & Brand -->
            <div class="flex items-center gap-3 mb-6">
                <div class="bg-blue-600 p-2 rounded-xl text-white glow-effect flex-shrink-0">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                        <polyline points="9 12 11 14 15 10"/>
                    </svg>
                </div>
                <div class="flex-1 min-w-0">
                    <span class="font-bold text-lg tracking-wide bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent block truncate font-english">MX-UI PANEL</span>
                    <span class="text-xs text-slate-500 font-medium font-english">v1.0.0</span>
                </div>
            </div>
            
            <!-- Title -->
            <h1 class="text-xl font-bold text-slate-100 mb-1 font-english">Sign In</h1>
            <p class="text-sm text-slate-400 mb-6 font-english">Enter your password to access the dashboard</p>
            
            <!-- Default Password Display -->
            <div class="bg-slate-800/40 border border-slate-700/50 rounded-xl p-3 mb-5">
                <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
                    <span class="text-xs text-slate-400 font-english">Default password</span>
                    <span id="default-password-display" class="text-xs font-mono font-bold text-blue-400 bg-blue-500/10 px-2 py-1 rounded border border-blue-500/20 cursor-pointer hover:bg-blue-500/20 transition text-center sm:text-left font-english" onclick="document.getElementById('pw').value='MUVIXO';document.getElementById('pw').focus();">
                        MUVIXO
                    </span>
                </div>
                <div id="password-status-message" class="hidden mt-2 text-xs text-amber-400 border-t border-amber-500/20 pt-2">
                    <span class="font-medium font-english">⚠️ Password changed</span>
                    <span class="text-slate-400 ml-2 font-english">(your custom password)</span>
                </div>
            </div>
            
            <!-- Login Form -->
            <form id="loginForm">
                <div class="mb-4">
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2 font-english">Password</label>
                    <input type="password" id="pw" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition input-focus-ring font-english" placeholder="Enter your password" autofocus required>
                </div>
                <button type="submit" id="loginButton" class="w-full bg-blue-600 hover:bg-blue-500 text-white font-medium text-sm px-4 py-2.5 rounded-xl transition duration-200 shadow-lg shadow-blue-600/10 flex items-center justify-center gap-2 font-english">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/>
                        <polyline points="10 17 15 12 10 7"/>
                        <line x1="15" y1="12" x2="3" y2="12"/>
                    </svg>
                    Sign In
                </button>
                <div id="errorMsg" class="mt-3 text-sm text-red-400 hidden font-english"></div>
            </form>
            
            <!-- Footer -->
            <div class="mt-6 pt-4 border-t border-slate-800/60 text-center text-xs text-slate-500 font-english">
                Created by Muvixo
            </div>
        </div>
    </div>

    <script>
        // Check if default password is still used
        async function checkDefaultPassword() {
            try {
                const res = await fetch('/api/is-default-password');
                const data = await res.json();
                if (!data.is_default) {
                    const display = document.getElementById('default-password-display');
                    display.textContent = 'Password changed';
                    display.className = 'text-xs font-mono font-bold text-amber-400 bg-amber-500/10 px-2 py-1 rounded border border-amber-500/20 text-center sm:text-left font-english';
                    display.onclick = null;
                    
                    // Show status message
                    const statusMsg = document.getElementById('password-status-message');
                    statusMsg.classList.remove('hidden');
                }
            } catch(e) {
                console.error('Error checking password status:', e);
            }
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            checkDefaultPassword();
            
            // Auto-focus the password field
            const pwInput = document.getElementById('pw');
            if (pwInput) {
                setTimeout(() => pwInput.focus(), 100);
            }
        });

        document.getElementById('loginForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('loginButton');
            const err = document.getElementById('errorMsg');
            err.classList.add('hidden');
            btn.disabled = true;
            
            // Store original button content
            const originalContent = btn.innerHTML;
            btn.innerHTML = '<div class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div> Signing in...';
            
            try {
                const res = await fetch('/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ password: document.getElementById('pw').value })
                });
                
                if (!res.ok) {
                    let errorMsg = 'Invalid password';
                    try {
                        const data = await res.json();
                        if (data && data.detail) {
                            errorMsg = data.detail;
                        }
                    } catch (parseError) {
                        if (res.statusText) {
                            errorMsg = res.statusText;
                        }
                    }
                    throw new Error(errorMsg);
                }
                
                location.href = '/dashboard';
                
            } catch (e) {
                err.textContent = e.message || 'Invalid password';
                err.classList.remove('hidden');
                btn.disabled = false;
                btn.innerHTML = originalContent;
                
                const pwInput = document.getElementById('pw');
                pwInput.classList.add('border-red-500');
                setTimeout(() => {
                    pwInput.classList.remove('border-red-500');
                }, 1000);
                
                pwInput.value = '';
                pwInput.focus();
            }
        });

        document.getElementById('pw').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                document.getElementById('loginForm').dispatchEvent(new Event('submit'));
            }
        });
        
        window.addEventListener('pageshow', function(event) {
            if (event.persisted) {
                checkDefaultPassword();
            }
        });
    </script>
</body>
</html>"""
# ---------- DASHBOARD_HTML (with Database Settings Modal & IP Scanner) ----------
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.5, user-scalable=yes" />
    <title>MX-UI v1.0.0</title>
    <script src="https://cdn.tailwindcss.com">
    </script>
    <script src="https://unpkg.com/lucide@latest">
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Vazirmatn:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'Vazirmatn', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    }
                }
            }
        }
    </script>
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            background-color: #070a13;
        }
        .glow-effect {
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.12);
        }
        .modal-glow {
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), 0 0 50px rgba(59, 130, 246, 0.05);
        }
        .circle-chart {
            transition: stroke-dasharray 0.35s ease;
            transform: rotate(-90deg);
            transform-origin: 50% 50%;
        }
        .custom-modal-overlay {
            transition: opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.2s, visibility 0.2s;
            visibility: hidden;
            opacity: 0;
            backdrop-filter: blur(0px);
        }
        .custom-modal-overlay.active {
            visibility: visible;
            opacity: 1;
            backdrop-filter: blur(12px);
        }
        .toast {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%) translateY(20px);
            background: #0f172a;
            border: 1px solid #1e293b;
            color: #e2e8f0;
            padding: 8px 18px;
            border-radius: 12px;
            font-size: 13px;
            font-family: 'Inter', 'Vazirmatn', sans-serif;
            opacity: 0;
            transition: opacity 0.25s, transform 0.25s;
            z-index: 9999;
            pointer-events: none;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            max-width: 90vw;
            text-align: center;
        }
        .toast.show {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
        .toast.success {
            border-color: #22c55e;
            color: #86efac;
        }
        .toast.error {
            border-color: #ef4444;
            color: #fca5a5;
        }
        .status-dot {
            display: inline-block;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            margin-right: 4px;
        }
        .status-dot.active {
            background-color: #22c55e;
        }
        .status-dot.inactive {
            background-color: #ef4444;
        }
        .qr-code-container {
            transition: all 0.3s ease;
        }
        .qr-code-container:hover {
            transform: scale(1.02);
        }
        .config-row {
            transition: background-color 0.15s ease;
        }
        .config-row:hover {
            background-color: rgba(30, 41, 59, 0.3);
        }
        @media (max-width: 640px) {
            .mobile-stack {
                flex-direction: column;
                align-items: stretch;
            }
            .mobile-full-width {
                width: 100%;
            }
            .mobile-text-center {
                text-align: center;
            }
            .mobile-padding {
                padding-left: 0.75rem;
                padding-right: 0.75rem;
            }
            .ring-container {
                flex-direction: row;
                justify-content: space-around;
            }
        }
        @media (max-width: 480px) {
            .xs-text-sm {
                font-size: 0.75rem;
            }
            .xs-padding {
                padding: 0.5rem;
            }
        }
        .scrollable-modal-content {
            max-height: 65vh;
            overflow-y: auto;
        }
        .scrollable-modal-content::-webkit-scrollbar {
            width: 4px;
        }
        .scrollable-modal-content::-webkit-scrollbar-track {
            background: transparent;
        }
        .scrollable-modal-content::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 2px;
        }
        .input-focus-ring:focus {
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
        }
        .input-focus-ring-amber:focus {
            box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.2);
        }
        .input-focus-ring-purple:focus {
            box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.2);
        }
        .input-focus-ring-green:focus {
            box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.2);
        }
        .input-focus-ring-cyan:focus {
            box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.2);
        }
        .font-persian {
            font-family: 'Vazirmatn', 'Inter', sans-serif;
        }
        .font-english {
            font-family: 'Inter', 'Vazirmatn', sans-serif;
        }
        .font-mixed {
            font-family: 'Inter', 'Vazirmatn', sans-serif;
        }
        .toggle-switch {
            position: relative;
            display: inline-block;
            width: 36px;
            height: 20px;
        }
        .toggle-switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }
        .toggle-slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #475569;
            transition: .3s;
            border-radius: 20px;
        }
        .toggle-slider:before {
            position: absolute;
            content: "";
            height: 16px;
            width: 16px;
            left: 2px;
            bottom: 2px;
            background-color: white;
            transition: .3s;
            border-radius: 50%;
        }
        .toggle-switch input:checked + .toggle-slider {
            background-color: #22c55e;
        }
        .toggle-switch input:checked + .toggle-slider:before {
            transform: translateX(16px);
        }
        .toggle-switch input:focus + .toggle-slider {
            box-shadow: 0 0 1px #22c55e;
        }
        .toggle-label {
            font-size: 10px;
            font-weight: 500;
            color: #94a3b8;
            margin-left: 8px;
            transition: color 0.2s;
        }
        .group:hover .toggle-label {
            color: #e2e8f0;
        }
        .system-details-wrapper {
            overflow: hidden;
            max-height: 0;
            opacity: 0;
            transition: max-height 0.6s cubic-bezier(0.4, 0, 0.2, 1), 
                        opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1),
                        margin 0.5s cubic-bezier(0.4, 0, 0.2, 1),
                        padding 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            margin-bottom: 0;
            padding-top: 0;
            padding-bottom: 0;
        }
        .system-details-wrapper.open {
            max-height: 2800px;
            opacity: 1;
            margin-bottom: 1.25rem;
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
        }
        .system-details-wrapper .detail-card {
            transform: translateY(30px) scale(0.97);
            opacity: 0;
            transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), 
                        opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            will-change: transform, opacity;
        }
        .system-details-wrapper.open .detail-card {
            transform: translateY(0) scale(1);
            opacity: 1;
        }
        .system-details-wrapper.open .detail-card:nth-child(1) { transition-delay: 0.05s; }
        .system-details-wrapper.open .detail-card:nth-child(2) { transition-delay: 0.10s; }
        .system-details-wrapper.open .detail-card:nth-child(3) { transition-delay: 0.15s; }
        .system-details-wrapper.open .detail-card:nth-child(4) { transition-delay: 0.20s; }
        .system-details-wrapper.open .detail-card:nth-child(5) { transition-delay: 0.25s; }
        .system-details-wrapper.open .detail-card:nth-child(6) { transition-delay: 0.30s; }
        .detail-card {
            transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1), 
                        border-color 0.25s ease,
                        box-shadow 0.25s ease;
        }
        .detail-card:hover {
            transform: translateY(-3px) scale(1.01);
            border-color: rgba(59, 130, 246, 0.4);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        }
        #toggleSystemBtn {
            transition: all 0.3s ease;
        }
        #toggleSystemBtn:hover {
            transform: scale(1.05);
        }
        #toggleSystemBtn:active {
            transform: scale(0.95);
        }
        #toggleSystemIcon {
            transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
            display: inline-block;
        }
        #toggleSystemIcon.rotated {
            transform: rotate(180deg) scale(1.1);
        }
        #toggleSystemText {
            transition: all 0.3s ease;
        }
        #systemMainStats > div {
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        }
        #systemMainStats > div:hover {
            transform: translateY(-2px);
            border-color: rgba(59, 130, 246, 0.25);
            box-shadow: 0 4px 20px rgba(59, 130, 246, 0.05);
        }
        .circle-chart.updating {
            animation: pulse-chart 0.5s ease;
        }
        @keyframes pulse-chart {
            0% { opacity: 0.7; }
            50% { opacity: 1; stroke-width: 4; }
            100% { opacity: 0.7; }
        }
        .stat-value {
            transition: all 0.3s ease;
        }
        .config-row {
            transition: all 0.2s ease;
        }
        .config-row .toggle-label {
            transition: all 0.3s ease;
        }
        .db-card {
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid rgba(51, 65, 85, 0.5);
            border-radius: 12px;
            padding: 12px 16px;
            transition: all 0.2s ease;
        }
        .db-card:hover {
            border-color: rgba(59, 130, 246, 0.3);
            background: rgba(15, 23, 42, 0.7);
        }
        .db-label {
            font-size: 10px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            font-family: 'Inter', 'Vazirmatn', sans-serif;
        }
        .db-value {
            font-size: 13px;
            font-weight: 500;
            color: #e2e8f0;
            font-family: 'JetBrains Mono', monospace;
            word-break: break-all;
        }
        .db-value.highlight {
            color: #60a5fa;
        }
        .db-value.green {
            color: #34d399;
        }
        .db-value.amber {
            color: #fbbf24;
        }
        .db-value.rose {
            color: #f87171;
        }
        .file-drop-zone {
            border: 2px dashed #334155;
            border-radius: 12px;
            padding: 30px 20px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
            background: rgba(15, 23, 42, 0.3);
        }
        .file-drop-zone:hover {
            border-color: #3b82f6;
            background: rgba(59, 130, 246, 0.05);
        }
        .file-drop-zone.dragover {
            border-color: #22c55e;
            background: rgba(34, 197, 94, 0.05);
        }
        .file-drop-zone.has-file {
            border-color: #22c55e;
            background: rgba(34, 197, 94, 0.05);
        }
        .ip-result-row {
            transition: all 0.2s ease;
            cursor: pointer;
        }
        .ip-result-row:hover {
            background-color: rgba(6, 182, 212, 0.05);
        }
        .ip-result-row.selected {
            background-color: rgba(6, 182, 212, 0.15);
            border-left: 2px solid #06b6d4;
        }
        .scan-progress-bar {
            transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .domain-check-icon {
            transition: all 0.3s ease;
        }
        .rating-badge {
            font-size: 9px;
            padding: 1px 8px;
            border-radius: 9999px;
            font-weight: 600;
        }
        .rating-badge.excellent {
            background: rgba(52, 211, 153, 0.15);
            color: #34d399;
            border: 1px solid rgba(52, 211, 153, 0.2);
        }
        .rating-badge.good {
            background: rgba(6, 182, 212, 0.15);
            color: #22d3ee;
            border: 1px solid rgba(6, 182, 212, 0.2);
        }
        .rating-badge.average {
            background: rgba(251, 191, 36, 0.15);
            color: #fbbf24;
            border: 1px solid rgba(251, 191, 36, 0.2);
        }
        .rating-badge.slow {
            background: rgba(239, 68, 68, 0.15);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.2);
        }
        .ip-select-btn {
            transition: all 0.2s ease;
        }
        .ip-select-btn:hover {
            transform: scale(1.05);
        }
        .ip-select-btn:active {
            transform: scale(0.95);
        }
    </style>
</head>
<body class="font-sans text-slate-200 min-h-screen flex flex-col relative antialiased tracking-tight">

    <div class="toast" id="toast"></div>

    <!-- Top Navigation -->
    <header class="border-b border-slate-800/80 bg-slate-900/40 backdrop-blur-md sticky top-0 z-40 transition-all duration-300">
        <div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between gap-2 mobile-padding">
            <div class="flex items-center space-x-2 sm:space-x-3 min-w-0">
                <div class="bg-blue-600 p-1.5 sm:p-2 rounded-xl text-white glow-effect flex-shrink-0 transition-transform duration-300 hover:scale-110">
                    <i data-lucide="shield-check" class="w-4 h-4 sm:w-5 sm:h-5"></i>
                </div>
                <div class="min-w-0">
                    <span class="font-bold text-sm sm:text-lg tracking-wide bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent font-sans truncate block font-english">MX-UI PANEL</span>
                    <span class="text-[10px] sm:text-xs text-slate-500 font-medium tracking-normal block truncate font-english">v1.0.0</span>
                </div>
            </div>
            <div class="flex items-center space-x-1 sm:space-x-3 flex-shrink-0">
                <span class="hidden sm:inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 whitespace-nowrap transition-all duration-300 hover:bg-emerald-500/20 font-english">
                    <span class="w-1.5 h-1.5 mr-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                    Online
                </span>
                <!-- IP Scanner Button -->
                <button onclick="toggleModal('ipScannerModal', true)" class="text-slate-400 hover:text-cyan-400 text-xs sm:text-sm font-medium flex items-center gap-1 p-1.5 sm:p-0 transition-all duration-300 hover:scale-105 font-english" title="IP Scanner">
                    <i data-lucide="scan" class="w-4 h-4 sm:w-5 sm:h-5"></i>
                    <span class="hidden xs:inline font-english">IP Scanner</span>
                </button>
                <!-- Database Settings Button -->
                <button onclick="toggleModal('databaseModal', true)" class="text-slate-400 hover:text-emerald-400 text-xs sm:text-sm font-medium flex items-center gap-1 p-1.5 sm:p-0 transition-all duration-300 hover:scale-105 font-english" title="Database Settings">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-4 h-4 sm:w-5 sm:h-5">
                        <ellipse cx="12" cy="5" rx="9" ry="3" />
                        <path d="M3 5v6c0 1.66 4 3 9 3s9-1.34 9-3V5" />
                        <path d="M3 11v6c0 1.66 4 3 9 3s9-1.34 9-3v-6" />
                    </svg>
                    <span class="hidden xs:inline font-english">Database</span>
                </button>
                <button onclick="toggleModal('settingsModal', true)" class="text-slate-400 hover:text-slate-200 text-xs sm:text-sm font-medium flex items-center gap-1 p-1.5 sm:p-0 transition-all duration-300 hover:scale-105 font-english">
                    <i data-lucide="settings" class="w-4 h-4"></i>
                    <span class="hidden xs:inline font-english">Settings</span>
                </button>
                <button onclick="logout()" class="text-slate-400 hover:text-slate-200 text-xs sm:text-sm font-medium flex items-center gap-1 p-1.5 sm:p-0 transition-all duration-300 hover:scale-105 font-english">
                    <i data-lucide="log-out" class="w-4 h-4"></i>
                    <span class="hidden xs:inline font-english">Logout</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main -->
    <main class="max-w-6xl w-full mx-auto px-4 py-6 sm:py-8 flex-grow mobile-padding">

        <!-- Stats Summary -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4 mb-6 sm:mb-8">
            <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-3 sm:p-4 text-center transition-all duration-300 hover:border-blue-500/30 hover:shadow-lg hover:shadow-blue-500/5">
                <p class="text-[8px] sm:text-[10px] text-slate-500 font-bold uppercase tracking-wider font-english">Traffic</p>
                <p class="text-sm sm:text-lg font-bold text-blue-400 font-mono truncate stat-value font-english" id="total-traffic">0 MB</p>
            </div>
            <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-3 sm:p-4 text-center transition-all duration-300 hover:border-amber-500/30 hover:shadow-lg hover:shadow-amber-500/5">
                <p class="text-[8px] sm:text-[10px] text-slate-500 font-bold uppercase tracking-wider font-english">Usage</p>
                <p class="text-sm sm:text-lg font-bold text-amber-400 font-mono truncate stat-value font-english" id="total-usage">0 GB</p>
            </div>
            <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-3 sm:p-4 text-center transition-all duration-300 hover:border-emerald-500/30 hover:shadow-lg hover:shadow-emerald-500/5">
                <p class="text-[8px] sm:text-[10px] text-slate-500 font-bold uppercase tracking-wider font-english">Inbounds</p>
                <p class="text-sm sm:text-lg font-bold text-emerald-400 font-mono truncate stat-value font-english" id="total-inbounds">0</p>
            </div>
            <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-3 sm:p-4 text-center transition-all duration-300 hover:border-purple-500/30 hover:shadow-lg hover:shadow-purple-500/5">
                <p class="text-[8px] sm:text-[10px] text-slate-500 font-bold uppercase tracking-wider font-english">Connections</p>
                <p class="text-sm sm:text-lg font-bold text-purple-400 font-mono truncate stat-value font-english" id="active-connections">0</p>
            </div>
        </div>

        <!-- Hardware Diagnostic Rings with Show More -->
        <div class="flex items-center justify-between mb-3 px-1">
            <h2 class="text-[10px] sm:text-xs font-bold text-slate-500 uppercase tracking-widest font-english">System Diagnostics</h2>
            <button onclick="toggleSystemDetails()" id="toggleSystemBtn" class="text-[10px] sm:text-xs text-blue-400 hover:text-blue-300 transition-all duration-300 flex items-center gap-1 group cursor-pointer select-none font-english">
                <i data-lucide="chevron-down" id="toggleSystemIcon" class="w-3 h-3 sm:w-4 sm:h-4"></i>
                <span id="toggleSystemText" class="transition-all duration-300 font-english">Show More</span>
            </button>
        </div>

        <!-- Main System Stats -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 mb-3 sm:mb-4" id="systemMainStats">
            <!-- CPU -->
            <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-3 sm:p-4 flex flex-row sm:flex-row items-center justify-between gap-2 sm:gap-4 cursor-default">
                <div class="relative w-12 h-12 sm:w-16 sm:h-16 shrink-0">
                    <svg class="w-full h-full" viewBox="0 0 36 36">
                        <path class="text-slate-800" stroke-width="3" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                        <path class="text-blue-500 circle-chart" stroke-dasharray="0, 100" stroke-width="3" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                    </svg>
                    <div class="absolute inset-0 flex items-center justify-center text-[8px] sm:text-[10px] font-mono font-bold text-blue-400 transition-all duration-300 font-english" id="ring-cpu-pct">0%</div>
                </div>
                <div class="text-right flex-1 min-w-0">
                    <p class="text-[8px] sm:text-[10px] text-slate-500 font-bold uppercase tracking-wider font-english">CPU</p>
                    <p class="text-xs sm:text-lg font-bold mt-0.5 text-slate-100 font-mono truncate transition-all duration-300 font-english" id="ring-cpu-val">0 Cores</p>
                </div>
            </div>
            <!-- RAM -->
            <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-3 sm:p-4 flex flex-row sm:flex-row items-center justify-between gap-2 sm:gap-4 cursor-default">
                <div class="relative w-12 h-12 sm:w-16 sm:h-16 shrink-0">
                    <svg class="w-full h-full" viewBox="0 0 36 36">
                        <path class="text-slate-800" stroke-width="3" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                        <path class="text-indigo-500 circle-chart" stroke-dasharray="0, 100" stroke-width="3" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                    </svg>
                    <div class="absolute inset-0 flex items-center justify-center text-[8px] sm:text-[10px] font-mono font-bold text-indigo-400 transition-all duration-300 font-english" id="ring-ram-pct">0%</div>
                </div>
                <div class="text-right flex-1 min-w-0">
                    <p class="text-[8px] sm:text-[10px] text-slate-500 font-bold uppercase tracking-wider font-english">RAM</p>
                    <p class="text-[10px] sm:text-lg font-bold mt-0.5 text-slate-100 font-mono truncate transition-all duration-300 font-english" id="ring-ram-val">0 GB</p>
                </div>
            </div>
            <!-- Swap -->
            <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-3 sm:p-4 flex flex-row sm:flex-row items-center justify-between gap-2 sm:gap-4 cursor-default">
                <div class="relative w-12 h-12 sm:w-16 sm:h-16 shrink-0">
                    <svg class="w-full h-full" viewBox="0 0 36 36">
                        <path class="text-slate-800" stroke-width="3" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                        <path class="text-amber-500 circle-chart" stroke-dasharray="0, 100" stroke-width="3" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                    </svg>
                    <div class="absolute inset-0 flex items-center justify-center text-[8px] sm:text-[10px] font-mono font-bold text-amber-400 transition-all duration-300 font-english" id="ring-swap-pct">0%</div>
                </div>
                <div class="text-right flex-1 min-w-0">
                    <p class="text-[8px] sm:text-[10px] text-slate-500 font-bold uppercase tracking-wider font-english">Swap</p>
                    <p class="text-[10px] sm:text-lg font-bold mt-0.5 text-slate-100 font-mono truncate transition-all duration-300 font-english" id="ring-swap-val">0 GB</p>
                </div>
            </div>
            <!-- Storage -->
            <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-3 sm:p-4 flex flex-row sm:flex-row items-center justify-between gap-2 sm:gap-4 cursor-default">
                <div class="relative w-12 h-12 sm:w-16 sm:h-16 shrink-0">
                    <svg class="w-full h-full" viewBox="0 0 36 36">
                        <path class="text-slate-800" stroke-width="3" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                        <path class="text-rose-500 circle-chart" stroke-dasharray="0, 100" stroke-width="3" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                    </svg>
                    <div class="absolute inset-0 flex items-center justify-center text-[8px] sm:text-[10px] font-mono font-bold text-rose-400 transition-all duration-300 font-english" id="ring-disk-pct">0%</div>
                </div>
                <div class="text-right flex-1 min-w-0">
                    <p class="text-[8px] sm:text-[10px] text-slate-500 font-bold uppercase tracking-wider font-english">Storage</p>
                    <p class="text-[10px] sm:text-lg font-bold mt-0.5 text-slate-100 font-mono truncate transition-all duration-300 font-english" id="ring-disk-val">0 GB</p>
                </div>
            </div>
        </div>

        <!-- Expanded System Details with Slide Animation -->
        <div id="systemDetailsWrapper" class="system-details-wrapper">
            <div class="grid grid-cols-2 lg:grid-cols-3 gap-3 sm:gap-4">
                <!-- CPU Details -->
                <div class="detail-card bg-slate-900/40 border border-slate-800/60 rounded-xl p-3 sm:p-4">
                    <div class="flex items-center gap-2 mb-2">
                        <i data-lucide="cpu" class="w-4 h-4 text-blue-400"></i>
                        <span class="text-[10px] sm:text-xs font-bold text-slate-400 uppercase tracking-wider font-english">CPU Details</span>
                    </div>
                    <div class="space-y-1.5 text-[10px] sm:text-xs">
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Load Average</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="cpu-load-avg">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Cores / Threads</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="cpu-cores-detail">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Usage (User)</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="cpu-user">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Usage (System)</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="cpu-system">--</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-400 font-english">Usage (Idle)</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="cpu-idle">--</span>
                        </div>
                    </div>
                </div>

                <!-- RAM Details -->
                <div class="detail-card bg-slate-900/40 border border-slate-800/60 rounded-xl p-3 sm:p-4">
                    <div class="flex items-center gap-2 mb-2">
                        <i data-lucide="memory-stick" class="w-4 h-4 text-indigo-400"></i>
                        <span class="text-[10px] sm:text-xs font-bold text-slate-400 uppercase tracking-wider font-english">RAM Details</span>
                    </div>
                    <div class="space-y-1.5 text-[10px] sm:text-xs">
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Total</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="ram-total-detail">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Used</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="ram-used-detail">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Free</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="ram-free-detail">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Available</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="ram-available-detail">--</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-400 font-english">Cached</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="ram-cached-detail">--</span>
                        </div>
                    </div>
                </div>

                <!-- Swap Details -->
                <div class="detail-card bg-slate-900/40 border border-slate-800/60 rounded-xl p-3 sm:p-4">
                    <div class="flex items-center gap-2 mb-2">
                        <i data-lucide="hard-drive" class="w-4 h-4 text-amber-400"></i>
                        <span class="text-[10px] sm:text-xs font-bold text-slate-400 uppercase tracking-wider font-english">Swap Details</span>
                    </div>
                    <div class="space-y-1.5 text-[10px] sm:text-xs">
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Total</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="swap-total-detail">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Used</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="swap-used-detail">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Free</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="swap-free-detail">--</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-400 font-english">Usage</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="swap-usage-detail">--</span>
                        </div>
                    </div>
                </div>

                <!-- Storage Details -->
                <div class="detail-card bg-slate-900/40 border border-slate-800/60 rounded-xl p-3 sm:p-4">
                    <div class="flex items-center gap-2 mb-2">
                        <i data-lucide="database" class="w-4 h-4 text-rose-400"></i>
                        <span class="text-[10px] sm:text-xs font-bold text-slate-400 uppercase tracking-wider font-english">Storage Details</span>
                    </div>
                    <div class="space-y-1.5 text-[10px] sm:text-xs">
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Total</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="disk-total-detail">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Used</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="disk-used-detail">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Free</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="disk-free-detail">--</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-400 font-english">Usage</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="disk-usage-detail">--</span>
                        </div>
                    </div>
                </div>

                <!-- Network Details -->
                <div class="detail-card bg-slate-900/40 border border-slate-800/60 rounded-xl p-3 sm:p-4">
                    <div class="flex items-center gap-2 mb-2">
                        <i data-lucide="network" class="w-4 h-4 text-cyan-400"></i>
                        <span class="text-[10px] sm:text-xs font-bold text-slate-400 uppercase tracking-wider font-english">Network Stats</span>
                    </div>
                    <div class="space-y-1.5 text-[10px] sm:text-xs">
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Total Traffic</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="network-total">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Total Requests</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="network-requests">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Active Connections</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="network-connections">--</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-400 font-english">Errors</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="network-errors">--</span>
                        </div>
                    </div>
                </div>

                <!-- System Info -->
                <div class="detail-card bg-slate-900/40 border border-slate-800/60 rounded-xl p-3 sm:p-4">
                    <div class="flex items-center gap-2 mb-2">
                        <i data-lucide="info" class="w-4 h-4 text-green-400"></i>
                        <span class="text-[10px] sm:text-xs font-bold text-slate-400 uppercase tracking-wider font-english">System Info</span>
                    </div>
                    <div class="space-y-1.5 text-[10px] sm:text-xs">
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Uptime</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="sys-uptime">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Active Configs</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="sys-active-configs">--</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-800/40 pb-1">
                            <span class="text-slate-400 font-english">Total Configs</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="sys-total-configs">--</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-400 font-english">Expired Configs</span>
                            <span class="text-slate-200 font-mono transition-all duration-300 font-english" id="sys-expired-configs">--</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Configurations Container -->
        <div class="bg-slate-900 border border-slate-800/80 rounded-2xl overflow-hidden glow-effect transition-all duration-300">
            <div class="p-4 sm:p-6 border-b border-slate-800/80 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 bg-slate-900/40">
                <div class="min-w-0">
                    <h2 class="text-lg sm:text-xl font-bold text-slate-100 truncate font-english">Configs</h2>
                    <p class="text-xs sm:text-sm text-slate-400 mt-0.5 truncate font-english">All V2Ray configurations:</p>
                </div>
                <button onclick="toggleModal('inboundModal', true)" class="flex items-center justify-center space-x-2 bg-blue-600 hover:bg-blue-500 text-white font-medium text-xs sm:text-sm px-3 sm:px-4 py-2 sm:py-2.5 rounded-xl transition-all duration-300 shadow-lg shadow-blue-600/10 hover:shadow-blue-600/25 hover:scale-105 active:scale-95 shrink-0 font-english">
                    <i data-lucide="plus" class="w-3 h-3 sm:w-4 sm:h-4"></i>
                    <span>Add Config</span>
                </button>
            </div>
            <div class="divide-y divide-slate-800/60" id="config-list">
                <!-- dynamically loaded -->
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-800/60 bg-slate-950 py-3 sm:py-4 text-[10px] sm:text-xs text-slate-500">
        <div class="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2 mobile-padding">
            <div class="flex items-center space-x-2 sm:space-x-3 flex-wrap justify-center sm:justify-start">
                <p class="font-english">MX-UI v1.0.0</p>
                <span class="text-[8px] sm:text-[9px] font-mono font-bold tracking-widest text-slate-400 border border-slate-800 px-1.5 py-0.5 rounded bg-slate-900/60 select-none transition-all duration-300 hover:border-slate-600 font-english">
                    Created by Muvixo
                </span>
            </div>
            <div class="flex items-center space-x-3 sm:space-x-4 flex-wrap justify-center">
                <span class="font-english">Core: <strong class="text-slate-400 font-mono text-[10px] sm:text-[11px] transition-all duration-300 font-english" id="uptime-display">00:00:00</strong></span>
                <span class="font-english">API: <strong class="text-emerald-400 transition-all duration-300 font-english">Connected</strong></span>
            </div>
        </div>
    </footer>

    <!-- ===== MODAL: IP SCANNER ===== -->
    <div id="ipScannerModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/75">
        <div class="bg-slate-900 border border-slate-800 w-full max-w-4xl rounded-2xl overflow-hidden modal-glow max-h-[95vh] flex flex-col transition-all duration-300 transform scale-95 opacity-0 active:scale-100 active:opacity-100">
            <!-- Header -->
            <div class="p-4 sm:p-6 border-b border-slate-800 flex items-center justify-between bg-slate-900/40 shrink-0">
                <div class="flex items-center space-x-3 min-w-0">
                    <div class="p-2 bg-cyan-500/10 rounded-lg text-cyan-400 border border-cyan-500/20 shrink-0">
                        <i data-lucide="scan" class="w-4 h-4 sm:w-5 sm:h-5"></i>
                    </div>
                    <div class="min-w-0">
                        <h3 class="text-base sm:text-lg font-bold text-slate-100 truncate font-english">IP Scanner</h3>
                        <p class="text-[10px] sm:text-xs text-slate-400 truncate font-english">Find better Cloudflare IPs for your configs</p>
                    </div>
                </div>
                <button onclick="toggleModal('ipScannerModal', false)" class="p-1.5 sm:p-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded-xl transition-all duration-300">
                    <i data-lucide="x" class="w-4 h-4 sm:w-5 sm:h-5"></i>
                </button>
            </div>
            
            <!-- Content -->
            <div class="p-4 sm:p-6 overflow-y-auto flex-1 scrollable-modal-content">
                <!-- Domain Check -->
                <div id="domainCheckResult" class="mb-4 p-3 rounded-xl bg-slate-800/30 border border-slate-700/50 flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center domain-check-icon" id="domainCheckIcon">
                        <i data-lucide="loader-2" class="w-4 h-4 text-slate-400 animate-spin"></i>
                    </div>
                    <div>
                        <p class="text-xs text-slate-400 font-english">Checking domain...</p>
                        <p class="text-xs font-mono text-slate-300 font-english" id="domainCheckText">Loading...</p>
                    </div>
                </div>
                
                <!-- Scan Configuration -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 font-english">IP Ranges</label>
                        <select id="scan-ranges" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-cyan-500 transition-all duration-300 font-mono font-english input-focus-ring-cyan">
                            <option value="all">All Cloudflare Ranges (15 ranges)</option>
                            <option value="173.245.48.0/20,103.21.244.0/22,103.22.200.0/22">Small (3 ranges)</option>
                            <option value="104.16.0.0/13,104.24.0.0/14,172.64.0.0/13,162.158.0.0/15">Medium (4 ranges)</option>
                            <option value="108.162.192.0/18,141.101.64.0/18,104.16.0.0/13,104.24.0.0/14,172.64.0.0/13,162.158.0.0/15,131.0.72.0/22,173.245.48.0/20,103.21.244.0/22,103.22.200.0/22,103.31.4.0/22,190.93.240.0/20,188.114.96.0/20,197.234.240.0/22,198.41.128.0/17">All Ranges</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 font-english">IPs Per Range</label>
                        <input type="number" id="scan-count" value="100" min="1" max="10000" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-cyan-500 transition-all duration-300 font-mono font-english input-focus-ring-cyan">
                    </div>
                </div>
                
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 font-english">Ports</label>
                        <select id="scan-ports" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-cyan-500 transition-all duration-300 font-mono font-english input-focus-ring-cyan">
                            <option value="443">HTTPS (443)</option>
                            <option value="443,8443">HTTPS + Alt (443, 8443)</option>
                            <option value="443,8443,2053,2083,2087,2096">All Common</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 font-english">Workers</label>
                        <select id="scan-workers" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-cyan-500 transition-all duration-300 font-mono font-english input-focus-ring-cyan">
                            <option value="50">50 (Slow)</option>
                            <option value="100" selected>100 (Recommended)</option>
                            <option value="200">200 (Fast)</option>
                            <option value="300">300 (Very Fast)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 font-english">Timeout (sec)</label>
                        <select id="scan-timeout" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-cyan-500 transition-all duration-300 font-mono font-english input-focus-ring-cyan">
                            <option value="2">2 (Fast)</option>
                            <option value="3" selected>3 (Default)</option>
                            <option value="5">5 (Slow)</option>
                            <option value="10">10 (Very Slow)</option>
                        </select>
                    </div>
                </div>
                
                <!-- Scan Button & Progress -->
                <div class="flex flex-col sm:flex-row gap-3 mb-4">
                    <button onclick="startIPScan()" id="scanStartBtn" class="flex-1 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-cyan-600/10 hover:shadow-cyan-600/25 flex items-center justify-center gap-2 font-english">
                        <i data-lucide="play" class="w-4 h-4"></i>
                        Start Scan
                    </button>
                    <button onclick="cancelIPScan()" id="scanCancelBtn" class="flex-1 py-2.5 bg-slate-700 hover:bg-slate-600 text-slate-300 text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 flex items-center justify-center gap-2 font-english hidden">
                        <i data-lucide="x-circle" class="w-4 h-4"></i>
                        Cancel
                    </button>
                </div>
                
                <!-- Progress Bar -->
                <div id="scanProgressContainer" class="hidden mb-4">
                    <div class="flex justify-between text-[10px] text-slate-400 mb-1">
                        <span id="scanProgressText" class="font-english">Scanning...</span>
                        <span id="scanProgressPercent" class="font-mono font-english">0%</span>
                    </div>
                    <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                        <div id="scanProgressBar" class="h-full bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full scan-progress-bar" style="width: 0%;"></div>
                    </div>
                    <div class="flex justify-between text-[10px] text-slate-500 mt-1">
                        <span id="scanStats" class="font-english">Found: 0 IPs</span>
                        <span id="scanStatus" class="font-english">Idle</span>
                    </div>
                </div>
                
                <!-- Results Table -->
                <div id="scanResultsContainer" class="hidden">
                    <div class="flex items-center justify-between mb-3">
                        <h4 class="text-xs font-bold text-slate-400 uppercase tracking-wider font-english">Top 10 Results</h4>
                        <span id="totalFoundLabel" class="text-[10px] text-slate-500 font-english">Total: 0 IPs</span>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-[10px] sm:text-xs">
                            <thead>
                                <tr class="text-slate-500 border-b border-slate-700/50">
                                    <th class="text-left py-2 px-2 font-english">#</th>
                                    <th class="text-left py-2 px-2 font-english">IP Address</th>
                                    <th class="text-left py-2 px-2 font-english">Port</th>
                                    <th class="text-left py-2 px-2 font-english">Ping (ms)</th>
                                    <th class="text-left py-2 px-2 font-english">Speed (ms)</th>
                                    <th class="text-left py-2 px-2 font-english">Rating</th>
                                    <th class="text-center py-2 px-2 font-english">Action</th>
                                </tr>
                            </thead>
                            <tbody id="scanResultsBody">
                            </tbody>
                        </table>
                    </div>
                    <div class="mt-3 flex flex-wrap items-center justify-between gap-2">
                        <span id="applyStatus" class="text-[10px] text-slate-500 font-english">Select an IP to apply</span>
                        <button onclick="applySelectedIP()" id="applyIPBtn" class="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-medium rounded-xl transition-all duration-300 shadow-lg shadow-emerald-600/10 hover:shadow-emerald-600/25 flex items-center gap-2 font-english disabled:opacity-50 disabled:cursor-not-allowed" disabled>
                            <i data-lucide="check" class="w-3.5 h-3.5"></i>
                            Apply Selected
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- Footer -->
            <div class="p-3 sm:p-4 border-t border-slate-800 bg-slate-950/40 flex items-center justify-end shrink-0">
                <button onclick="toggleModal('ipScannerModal', false)" class="px-6 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 hover:scale-105 active:scale-95 font-english">
                    Close
                </button>
            </div>
        </div>
    </div>

    <!-- ===== MODAL: DATABASE SETTINGS ===== -->
    <div id="databaseModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/75">
        <div class="bg-slate-900 border border-slate-800 w-full max-w-4xl rounded-2xl overflow-hidden modal-glow max-h-[95vh] flex flex-col transition-all duration-300 transform scale-95 opacity-0 active:scale-100 active:opacity-100">
            <div class="p-4 sm:p-6 border-b border-slate-800 flex items-center justify-between bg-slate-900/40 shrink-0">
                <div class="flex items-center space-x-3 min-w-0">
                    <div class="p-2 bg-emerald-500/10 rounded-lg text-emerald-400 border border-emerald-500/20 shrink-0">
                        <svg version="1.0" xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 512.000000 512.000000" preserveAspectRatio="xMidYMid meet" fill="currentColor">
                            <g transform="translate(0.000000,512.000000) scale(0.100000,-0.100000)" stroke="none">
                                <path d="M2245 5113 c-230 -13 -393 -27 -525 -44 -757 -97 -1254 -301 -1378
                                -566 l-27 -58 0 -1885 0 -1885 26 -55 c47 -101 179 -220 327 -294 761 -384
                                2532 -437 3521 -106 311 103 516 243 590 400 l26 55 0 1885 0 1885 -26 55
                                c-152 324 -843 553 -1843 610 -160 9 -563 11 -691 3z m680 -303 c570 -32 1104
                                -139 1380 -278 118 -59 205 -134 205 -176 0 -9 -20 -36 -45 -60 -173 -169
                                -706 -311 -1380 -368 -200 -16 -866 -16 -1055 0 -547 49 -966 142 -1240 275
                                -96 47 -180 120 -180 157 0 41 87 113 202 169 443 214 1284 326 2113 281z
                                m-2101 -950 c264 -105 720 -192 1211 -232 204 -16 860 -16 1060 0 567 47 1022 145 1313 282 l102 49 0 -411 0 -412 -48 -45 c-152 -146 -632 -284 -1202 -346
                                -344 -37 -911 -44 -1245 -15 -646 56 -1192 201 -1357 360 l-48 46 0 111 0 112
                                103 -49 c275 -129 745 -234 1227 -273 l155 -12 6 40 c3 22 9 88 12 147 8 126 30 111 -178 128
                                -574 47 -1118 198 -1282 355 l-43 42 0 111 0 112 70 -35 c38 -19 103 -48 144 -65z
                                m0 -1200 c264 -105 719 -192 1211 -232 202 -16 860 -16 1050 0 608 53 1033 144 1322 281 l103 50 0 -411 0 -412 -48 -45
                                c-152 -146 -632 -284 -1202 -346 -344 -37 -911 -44 -1245 -15 -646 56 -1192 201 -1357
                                360 l-48 46 0 111 0 112 103 -49 c275 -129 745 -234 1227 -273 l155 -12 6 40
                                c3 22 9 88 12 147 8 126 30 111 -178 128 -574 47 -1118 198 -1282 355 l-43 42
                                0 111 0 112 70 -35 c38 -19 103 -48 144 -65z m0 -1200 c265 -105 717 -192
                                1211 -232 202 -16 860 -16 1050 0 608 53 1033 144 1322 281 l103 50 0 -406 c0
                                -465 7 -431 -98 -502 -119 -80 -274 -142 -510 -202 -654 -167 -1584 -196
                                -2332 -73 -423 69 -788 195 -910 313 l-50 47 0 111 0 112 103 -49 c275 -129
                                745 -234 1227 -273 l155 -12 6 40 c3 22 9 88 12 147 8 126 30 111 -178 128
                                -334 27 -679 92 -935 177 -128 42 -290 126 -342 178 l-48 47 0 109 0 109 70
                                -35 c38 -19 103 -48 144 -65z"/>
                                <path d="M2410 3160 l0 -150 150 0 150 0 0 150 0 150 -150 0 -150 0 0 -150z"/>
                                <path d="M2410 1960 l0 -150 150 0 150 0 0 150 0 150 -150 0 -150 0 0 -150z"/>
                                <path d="M2410 760 l0 -150 150 0 150 0 0 150 0 150 -150 0 -150 0 0 -150z"/>
                            </g>
                        </svg>
                    </div>
                    <div class="min-w-0">
                        <h3 class="text-base sm:text-lg font-bold text-slate-100 truncate font-english">Database Management</h3>
                        <p class="text-[10px] sm:text-xs text-slate-400 truncate font-english">View all stored data, backup and restore your configuration</p>
                    </div>
                </div>
                <button onclick="toggleModal('databaseModal', false)" class="p-1.5 sm:p-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded-xl transition-all duration-300"><i data-lucide="x" class="w-4 h-4 sm:w-5 sm:h-5"></i></button>
            </div>
            
            <div class="p-4 sm:p-6 overflow-y-auto flex-1 scrollable-modal-content space-y-4 sm:space-y-6">
                <!-- Database Stats Cards -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-3" id="dbStats">
                    <div class="db-card">
                        <div class="db-label font-english">Total Configs</div>
                        <div class="db-value highlight font-english" id="db-total-configs">0</div>
                    </div>
                    <div class="db-card">
                        <div class="db-label font-english">Active Configs</div>
                        <div class="db-value green font-english" id="db-active-configs">0</div>
                    </div>
                    <div class="db-card">
                        <div class="db-label font-english">Total Traffic</div>
                        <div class="db-value amber font-english" id="db-total-traffic">0 B</div>
                    </div>
                    <div class="db-card">
                        <div class="db-label font-english">Last Saved</div>
                        <div class="db-value font-english" id="db-last-saved">Never</div>
                    </div>
                </div>

                <!-- Config Details Table -->
                <div class="db-card">
                    <div class="db-label mb-3 font-english">All Configurations Details</div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-[11px] sm:text-xs">
                            <thead>
                                <tr class="text-slate-500 border-b border-slate-700/50">
                                    <th class="text-left py-2 px-2 font-english">Label</th>
                                    <th class="text-left py-2 px-2 font-english">UUID</th>
                                    <th class="text-right py-2 px-2 font-english">Used</th>
                                    <th class="text-right py-2 px-2 font-english">Limit</th>
                                    <th class="text-center py-2 px-2 font-english">Status</th>
                                    <th class="text-right py-2 px-2 font-english">IPs</th>
                                </tr>
                            </thead>
                            <tbody id="dbConfigsBody">
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Backup / Restore Section -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <!-- Download Backup -->
                    <div class="db-card">
                        <div class="flex items-center gap-2 mb-3">
                            <i data-lucide="download" class="w-4 h-4 text-blue-400"></i>
                            <span class="db-label font-english">Backup Database</span>
                        </div>
                        <p class="text-[10px] text-slate-400 mb-3 font-english">Download complete database as JSON file</p>
                        <button onclick="downloadDatabase()" class="w-full py-2.5 bg-blue-600 hover:bg-blue-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-blue-600/10 hover:shadow-blue-600/25 flex items-center justify-center gap-2 font-english">
                            <i data-lucide="download" class="w-4 h-4"></i>
                            Download mx-ui.json
                        </button>
                    </div>

                    <!-- Restore Backup -->
                    <div class="db-card">
                        <div class="flex items-center gap-2 mb-3">
                            <i data-lucide="upload" class="w-4 h-4 text-emerald-400"></i>
                            <span class="db-label font-english">Restore Database</span>
                        </div>
                        <p class="text-[10px] text-slate-400 mb-3 font-english">Upload a mx-ui.json backup file</p>
                        <div class="file-drop-zone" id="dropZone" onclick="document.getElementById('fileInput').click()">
                            <input type="file" id="fileInput" accept=".json" class="hidden" onchange="handleFileSelect(event)">
                            <div id="dropZoneContent">
                                <i data-lucide="upload-cloud" class="w-8 h-8 text-slate-500 mx-auto mb-2"></i>
                                <p class="text-xs text-slate-400 font-english">Drop your mx-ui.json here or click to browse</p>
                                <p class="text-[10px] text-slate-500 mt-1 font-english" id="fileName">No file selected</p>
                            </div>
                        </div>
                        <button onclick="restoreDatabase()" id="restoreBtn" class="w-full mt-3 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-emerald-600/10 hover:shadow-emerald-600/25 flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed font-english">
                            <i data-lucide="upload" class="w-4 h-4"></i>
                            Restore Database
                        </button>
                    </div>
                </div>
            </div>

            <div class="p-3 sm:p-4 border-t border-slate-800 bg-slate-950/40 flex items-center justify-end shrink-0">
                <button onclick="toggleModal('databaseModal', false)" class="px-6 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 hover:scale-105 active:scale-95 font-english">
                    Close
                </button>
            </div>
        </div>
    </div>

    <!-- ===== MODAL: INBOUND ===== -->
    <div id="inboundModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/75">
        <div class="bg-slate-900 border border-slate-800 w-full max-w-2xl rounded-2xl overflow-hidden modal-glow max-h-[95vh] flex flex-col transition-all duration-300 transform scale-95 opacity-0 active:scale-100 active:opacity-100">
            <div class="p-4 sm:p-6 border-b border-slate-800 flex items-center justify-between bg-slate-900/40 shrink-0">
                <div class="flex items-center space-x-3 min-w-0">
                    <div class="p-2 bg-blue-500/10 rounded-lg text-blue-400 border border-blue-500/20 shrink-0"><i data-lucide="plus-circle" class="w-4 h-4 sm:w-5 sm:h-5"></i></div>
                    <div class="min-w-0">
                        <h3 class="text-base sm:text-lg font-bold text-slate-100 truncate font-english">Add New Config</h3>
                        <p class="text-[10px] sm:text-xs text-slate-400 truncate font-english">Deploy a new VLESS or XHTTP configuration.</p>
                    </div>
                </div>
                <button onclick="toggleModal('inboundModal', false)" class="p-1.5 sm:p-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded-xl transition-all duration-300"><i data-lucide="x" class="w-4 h-4 sm:w-5 sm:h-5"></i></button>
            </div>
            <div class="p-4 sm:p-6 overflow-y-auto flex-1 scrollable-modal-content space-y-4 sm:space-y-5">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Remark / Label</label>
                        <input type="text" id="new-label" placeholder="e.g., US-Reality" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 input-focus-ring font-mixed">
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Protocol</label>
                        <select id="new-protocol" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 font-mono text-xs font-english">
                            <option value="vless-ws">VLESS + WS</option>
                            <option value="xhttp-packet-up">XHTTP (packet-up)</option>
                            <option value="xhttp-stream-up">XHTTP (stream-up)</option>
                        </select>
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Fingerprint (uTLS)</label>
                        <select id="new-fp" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 font-mono text-xs font-english">
                            <option value="chrome">chrome</option>
                            <option value="firefox">firefox</option>
                            <option value="safari">safari</option>
                            <option value="ios">ios</option>
                            <option value="android">android</option>
                            <option value="edge">edge</option>
                            <option value="360">360</option>
                            <option value="qq">qq</option>
                            <option value="random">random</option>
                            <option value="randomized">randomized</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">ALPN (optional)</label>
                        <input type="text" id="new-alpn" placeholder="e.g., h2,http/1.1" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mixed text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 input-focus-ring">
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Traffic Limit (MB)</label>
                        <input type="number" id="new-limit" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 input-focus-ring font-english">
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Expiry (days, 0 = unlimited)</label>
                        <input type="number" id="new-expiry" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 input-focus-ring font-english">
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">IP Limit (0 = unlimited)</label>
                        <input type="number" id="new-iplimit" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 input-focus-ring font-english">
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Speed Limit (0 = unlimited)</label>
                        <div class="flex gap-2">
                            <input type="number" id="new-speed" value="0" step="0.5" class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 input-focus-ring font-english">
                            <select id="new-speed-unit" class="bg-slate-950 border border-slate-800 rounded-xl px-2 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 font-mono font-english">
                                <option value="MBIT">Mbps</option>
                                <option value="KB">KB/s</option>
                                <option value="MB">MB/s</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="p-3 sm:p-4 border-t border-slate-800 bg-slate-950/40 flex flex-col sm:flex-row items-center justify-end space-y-2 sm:space-y-0 sm:space-x-3 shrink-0">
                <button onclick="toggleModal('inboundModal', false)" class="w-full sm:w-auto px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 font-english">Cancel</button>
                <button onclick="createConfig()" class="w-full sm:w-auto px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-blue-600/10 hover:shadow-blue-600/25 font-english">Deploy Config</button>
            </div>
        </div>
    </div>

    <!-- ===== MODAL: EDIT ===== -->
    <div id="editModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/75">
        <div class="bg-slate-900 border border-slate-800 w-full max-w-2xl rounded-2xl overflow-hidden modal-glow max-h-[95vh] flex flex-col transition-all duration-300 transform scale-95 opacity-0 active:scale-100 active:opacity-100">
            <div class="p-4 sm:p-6 border-b border-slate-800 flex items-center justify-between bg-slate-900/40 shrink-0">
                <div class="flex items-center space-x-3 min-w-0">
                    <div class="p-2 bg-amber-500/10 rounded-lg text-amber-400 border border-amber-500/20 shrink-0"><i data-lucide="edit" class="w-4 h-4 sm:w-5 sm:h-5"></i></div>
                    <div class="min-w-0">
                        <h3 class="text-base sm:text-lg font-bold text-slate-100 truncate font-english">Modify Config: <span id="editNodeTitle" class="text-amber-400 font-english">Node</span></h3>
                        <p class="text-[10px] sm:text-xs text-slate-400 truncate font-english">Altering production values resets live connection pipelines.</p>
                    </div>
                </div>
                <button onclick="toggleModal('editModal', false)" class="p-1.5 sm:p-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded-xl transition-all duration-300"><i data-lucide="x" class="w-4 h-4 sm:w-5 sm:h-5"></i></button>
            </div>
            <div class="p-4 sm:p-6 overflow-y-auto flex-1 scrollable-modal-content space-y-4 sm:space-y-5">
                <input type="hidden" id="edit-uuid">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Remark Label</label>
                        <input type="text" id="edit-label" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-amber-500 transition-all duration-300 font-mixed input-focus-ring-amber" placeholder="Enter label name">
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Protocol</label>
                        <select id="edit-protocol" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-amber-500 transition-all duration-300 font-mono text-xs font-english">
                            <option value="vless-ws">VLESS + WS</option>
                            <option value="xhttp-packet-up">XHTTP (packet-up)</option>
                            <option value="xhttp-stream-up">XHTTP (stream-up)</option>
                        </select>
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Fingerprint</label>
                        <select id="edit-fp" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-amber-500 transition-all duration-300 font-mono text-xs font-english">
                            <option value="chrome">chrome</option>
                            <option value="firefox">firefox</option>
                            <option value="safari">safari</option>
                            <option value="ios">ios</option>
                            <option value="android">android</option>
                            <option value="edge">edge</option>
                            <option value="360">360</option>
                            <option value="qq">qq</option>
                            <option value="random">random</option>
                            <option value="randomized">randomized</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">ALPN (optional)</label>
                        <input type="text" id="edit-alpn" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mixed text-slate-200 focus:outline-none focus:border-amber-500 transition-all duration-300 input-focus-ring-amber" placeholder="e.g., h2,http/1.1">
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Traffic Limit (MB)</label>
                        <input type="number" id="edit-limit" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-amber-500 transition-all duration-300 input-focus-ring-amber font-english">
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Expiry (days from now)</label>
                        <input type="number" id="edit-expiry" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-amber-500 transition-all duration-300 input-focus-ring-amber font-english">
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">IP Limit</label>
                        <input type="number" id="edit-iplimit" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-amber-500 transition-all duration-300 input-focus-ring-amber font-english">
                    </div>
                    <div>
                        <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Speed Limit</label>
                        <div class="flex gap-2">
                            <input type="number" id="edit-speed" value="0" step="0.5" class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-amber-500 transition-all duration-300 input-focus-ring-amber font-english">
                            <select id="edit-speed-unit" class="bg-slate-950 border border-slate-800 rounded-xl px-2 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-amber-500 transition-all duration-300 font-mono font-english">
                                <option value="MBIT">Mbps</option>
                                <option value="KB">KB/s</option>
                                <option value="MB">MB/s</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="p-3 sm:p-4 border-t border-slate-800 bg-slate-950/40 flex flex-col sm:flex-row items-center justify-end space-y-2 sm:space-y-0 sm:space-x-3 shrink-0">
                <button onclick="toggleModal('editModal', false)" class="w-full sm:w-auto px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 font-english">Discard</button>
                <button onclick="saveEdit()" class="w-full sm:w-auto px-4 py-2 bg-amber-600 hover:bg-amber-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-amber-600/10 hover:shadow-amber-600/25 font-english">Commit Changes</button>
            </div>
        </div>
    </div>

    <!-- ===== MODAL: QR ===== -->
    <div id="qrModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/75">
        <div class="bg-slate-900 border border-slate-800 w-full max-w-3xl rounded-2xl overflow-hidden modal-glow max-h-[95vh] flex flex-col transition-all duration-300 transform scale-95 opacity-0 active:scale-100 active:opacity-100">
            <div class="p-4 sm:p-6 border-b border-slate-800 flex items-center justify-between bg-slate-900/40 shrink-0">
                <div class="flex items-center space-x-3 min-w-0">
                    <div class="p-2 bg-blue-500/10 rounded-lg text-blue-400 border border-blue-500/20 shrink-0">
                        <svg version="1.0" xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 sm:w-5 sm:h-5" viewBox="0 0 512.000000 512.000000" preserveAspectRatio="xMidYMid meet" fill="currentColor">
                            <g transform="translate(0.000000,512.000000) scale(0.100000,-0.100000)" stroke="none">
                                <path d="M545 5104 c-38 -8 -113 -35 -165 -61 -78 -38 -109 -60 -176 -127 -67
                                -67 -89 -98 -127 -176 -75 -154 -77 -172 -77 -767 0 -316 4 -532 10 -554 34
                                -122 166 -186 303 -148 47 13 102 60 130 113 22 40 22 49 27 581 l5 540 25 43
                                c15 27 42 54 70 70 l45 27 535 5 c515 5 537 6 580 26 188 87 169 379 -29 434
                                -22 6 -238 10 -561 9 -416 0 -540 -4 -595 -15z"/>
                                <path d="M3420 5111 c-103 -32 -160 -110 -160 -220 0 -98 42 -170 124 -214 40
                                -22 49 -22 581 -27 l540 -5 43 -25 c27 -15 54 -42 70 -70 l27 -45 5 -540 c5
                                -532 5 -541 27 -581 98 -182 379 -160 433 35 6 22 10 238 10 554 0 594 -2 613
                                -76 765 -94 192 -263 322 -476 366 -65 14 -159 16 -600 15 -288 0 -534 -4
                                -548 -8z"/>
                                <path d="M1074 4174 c-23 -8 -58 -31 -77 -51 -67 -66 -67 -69 -67 -625 0 -327
                                4 -514 11 -542 14 -55 59 -110 112 -139 42 -22 43 -22 577 -22 529 0 535 0
                                575 22 46 24 75 54 101 103 18 33 19 67 19 570 0 534 0 535 -22 577 -29 53
                                -84 98 -139 112 -28 7 -214 11 -546 10 -414 0 -510 -3 -544 -15z m786 -684 l0
                                -230 -230 0 -230 0 0 230 0 230 230 0 230 0 0 -230z"/>
                                <path d="M2941 4175 c-51 -16 -94 -54 -124 -110 -22 -40 -22 -46 -22 -575 0
                                -529 0 -535 22 -575 24 -46 54 -75 103 -101 33 -18 67 -19 570 -19 534 0 535
                                0 577 22 53 29 98 84 112 139 7 28 11 214 11 537 0 554 -1 561 -67 629 -66 67
                                -72 68 -637 67 -394 0 -510 -3 -545 -14z m779 -685 l0 -230 -230 0 -230 0 0
                                230 0 230 230 0 230 0 0 -230z"/>
                                <path d="M1105 2321 c-43 -11 -76 -29 -113 -64 -60 -58 -62 -75 -62 -633 0
                                -560 0 -557 68 -627 64 -66 73 -67 629 -67 323 0 509 4 537 11 55 14 110 59
                                139 112 22 42 22 43 22 577 0 503 -1 537 -19 570 -26 49 -55 79 -101 103 -39
                                22 -48 22 -555 24 -283 1 -528 -2 -545 -6z m755 -691 l0 -230 -230 0 -230 0 0
                                230 0 230 230 0 230 0 0 -230z"/>
                                <path d="M2965 2321 c-70 -18 -117 -56 -151 -121 -15 -28 -19 -65 -22 -186 -5
                                -203 5 -254 67 -315 54 -55 109 -74 193 -66 103 9 174 69 198 168 7 29 10 107
                                8 205 -3 168 -10 196 -62 252 -47 52 -158 82 -231 63z"/>
                                <path d="M3665 2321 c-105 -27 -175 -117 -175 -226 0 -100 66 -194 154 -220
                                61 -18 316 -20 383 -3 32 8 61 25 94 57 39 38 49 56 60 105 25 113 -17 212
                                -112 266 -41 24 -53 25 -209 27 -91 1 -178 -2 -195 -6z"/>
                                <path d="M119 1833 c-57 -30 -92 -71 -109 -132 -6 -22 -10 -238 -10 -554 0
                                -595 2 -613 77 -767 38 -78 60 -109 127 -176 67 -67 98 -89 176 -127 154 -75
                                172 -77 767 -77 316 0 532 4 554 10 122 34 186 166 148 303 -13 47 -60 102
                                -113 130 -40 22 -49 22 -581 27 l-540 5 -43 25 c-27 15 -54 42 -70 70 l-27 45
                                -5 540 c-5 532 -5 541 -27 581 -62 117 -202 158 -324 97z"/>
                                <path d="M4796 1845 c-47 -17 -91 -57 -119 -110 -22 -39 -22 -51 -27 -580 l-5
                                -540 -27 -45 c-16 -28 -43 -55 -70 -70 l-43 -25 -540 -5 c-532 -5 -541 -5
                                -581 -27 -182 -98 -160 -379 35 -433 22 -6 238 -10 554 -10 434 0 530 3 595
                                16 213 44 382 174 476 366 74 152 76 171 76 765 0 316 -4 532 -10 554 -17 61
                                -52 102 -109 132 -62 31 -139 36 -205 12z"/>
                                <path d="M3188 1386 c-104 -28 -158 -104 -158 -219 0 -106 33 -167 115 -210
                                39 -21 53 -22 438 -25 463 -3 477 -1 545 72 102 111 73 291 -59 366 l-44 25
                                -395 2 c-298 2 -407 -1 -442 -11z"/>
                            </g>
                        </svg>
                    </div>
                    <div class="min-w-0">
                        <h3 class="text-base sm:text-lg font-bold text-slate-100 truncate font-english">QR Codes</h3>
                        <p class="text-[10px] sm:text-xs text-slate-400 truncate font-english" id="qrTargetLabel">Default Link</p>
                    </div>
                </div>
                <button onclick="toggleModal('qrModal', false)" class="p-1.5 sm:p-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded-xl transition-all duration-300 shrink-0">
                    <i data-lucide="x" class="w-4 h-4 sm:w-5 sm:h-5"></i>
                </button>
            </div>

            <div class="p-4 sm:p-6 overflow-y-auto flex-1 scrollable-modal-content">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 mb-4">
                    <div class="bg-slate-950/60 border border-slate-800/60 rounded-xl p-4 text-center qr-code-container transition-all duration-300 hover:border-blue-500/30">
                        <p class="text-[10px] sm:text-xs text-slate-400 mb-3 font-medium flex items-center justify-center gap-2 font-english">
                            <i data-lucide="link" class="w-3 h-3 sm:w-4 sm:h-4"></i>
                            Config Link
                        </p>
                        <div class="mx-auto w-32 h-32 sm:w-40 sm:h-40 bg-white p-2 rounded-xl shadow-inner flex items-center justify-center border-2 border-slate-700/50 transition-all duration-300 hover:border-blue-500/50">
                            <img id="qrImage" src="" alt="Config QR Code" class="w-full h-full object-contain">
                        </div>
                        <button onclick="copyText(document.getElementById('qrTextPayload').textContent)" class="mt-3 text-[10px] sm:text-xs text-blue-400 hover:text-blue-300 transition-all duration-300 flex items-center justify-center gap-1.5 mx-auto hover:scale-105 font-english">
                            <i data-lucide="copy" class="w-3 h-3 sm:w-4 sm:h-4"></i>
                            Copy Config Link
                        </button>
                    </div>

                    <div class="bg-slate-950/60 border border-slate-800/60 rounded-xl p-4 text-center qr-code-container transition-all duration-300 hover:border-blue-500/30">
                        <p class="text-[10px] sm:text-xs text-slate-400 mb-3 font-medium flex items-center justify-center gap-2 font-english">
                            <i data-lucide="folder-tree" class="w-3 h-3 sm:w-4 sm:h-4"></i>
                            Subscription Link
                        </p>
                        <div class="mx-auto w-32 h-32 sm:w-40 sm:h-40 bg-white p-2 rounded-xl shadow-inner flex items-center justify-center border-2 border-slate-700/50 transition-all duration-300 hover:border-blue-500/50">
                            <img id="qrSubImage" src="" alt="Subscription QR Code" class="w-full h-full object-contain">
                        </div>
                        <button onclick="copyText(document.getElementById('qrSubPayload').textContent)" class="mt-3 text-[10px] sm:text-xs text-blue-400 hover:text-blue-300 transition-all duration-300 flex items-center justify-center gap-1.5 mx-auto hover:scale-105 font-english">
                            <i data-lucide="copy" class="w-3 h-3 sm:w-4 sm:h-4"></i>
                            Copy Sub Link
                        </button>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div class="bg-slate-950/60 border border-slate-800/60 rounded-xl p-3">
                        <span class="text-[8px] sm:text-[10px] text-slate-500 block uppercase font-bold tracking-wider mb-1 flex items-center gap-1.5 font-english">
                            <i data-lucide="link" class="w-3 h-3"></i>
                            Config Link
                        </span>
                        <p id="qrTextPayload" class="text-[8px] sm:text-[10px] font-mono text-slate-400 break-all select-all truncate bg-slate-950/50 p-1.5 rounded border border-slate-800/40 font-english">https://example.com/config</p>
                    </div>
                    <div class="bg-slate-950/60 border border-slate-800/60 rounded-xl p-3">
                        <span class="text-[8px] sm:text-[10px] text-slate-500 block uppercase font-bold tracking-wider mb-1 flex items-center gap-1.5 font-english">
                            <i data-lucide="folder-tree" class="w-3 h-3"></i>
                            Subscription Link
                        </span>
                        <p id="qrSubPayload" class="text-[8px] sm:text-[10px] font-mono text-slate-400 break-all select-all truncate bg-slate-950/50 p-1.5 rounded border border-slate-800/40 font-english">https://example.com/sub</p>
                    </div>
                </div>
            </div>

            <div class="p-3 sm:p-4 border-t border-slate-800 bg-slate-950/40 flex items-center justify-end shrink-0">
                <button onclick="toggleModal('qrModal', false)" class="px-6 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 hover:scale-105 active:scale-95 font-english">
                    Close
                </button>
            </div>
        </div>
    </div>

    <!-- ===== MODAL: CONFIRM ===== -->
    <div id="confirmModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80">
        <div class="bg-slate-900 border border-slate-800 w-full max-w-sm rounded-2xl overflow-hidden modal-glow p-4 sm:p-6 text-center space-y-3 sm:space-y-4 transition-all duration-300 transform scale-95 opacity-0 active:scale-100 active:opacity-100">
            <div class="mx-auto w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-red-500/10 border border-red-500/30 flex items-center justify-center text-red-400">
                <i data-lucide="alert-triangle" class="w-5 h-5 sm:w-6 sm:h-6"></i>
            </div>
            <div class="space-y-1">
                <h3 class="text-sm sm:text-base font-bold text-slate-100 font-english">Confirm Action</h3>
                <p id="confirmMessage" class="text-[11px] sm:text-xs text-slate-400 leading-relaxed px-2 font-english">Are you sure?</p>
            </div>
            <div class="flex gap-3">
                <button onclick="_confirmNo()" class="flex-1 py-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 text-[10px] sm:text-xs font-semibold rounded-xl transition-all duration-300 font-english">Cancel</button>
                <button onclick="_confirmYes()" class="flex-1 py-2 bg-red-600 hover:bg-red-500 text-white text-[10px] sm:text-xs font-semibold rounded-xl transition-all duration-300 font-english">Delete</button>
            </div>
        </div>
    </div>

    <!-- ===== MODAL: SETTINGS ===== -->
    <div id="settingsModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/75">
        <div class="bg-slate-900 border border-slate-800 w-full max-w-2xl rounded-2xl overflow-hidden modal-glow max-h-[95vh] flex flex-col transition-all duration-300 transform scale-95 opacity-0 active:scale-100 active:opacity-100">
            <div class="p-4 sm:p-6 border-b border-slate-800 flex items-center justify-between bg-slate-900/40 shrink-0">
                <div class="flex items-center space-x-3 min-w-0">
                    <div class="p-2 bg-blue-500/10 rounded-lg text-blue-400 border border-blue-500/20 shrink-0"><i data-lucide="settings" class="w-4 h-4 sm:w-5 sm:h-5"></i></div>
                    <div class="min-w-0">
                        <h3 class="text-base sm:text-lg font-bold text-slate-100 truncate font-english">Settings</h3>
                        <p class="text-[10px] sm:text-xs text-slate-400 truncate font-english">Manage dashboard paths and security</p>
                    </div>
                </div>
                <button onclick="toggleModal('settingsModal', false)" class="p-1.5 sm:p-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded-xl transition-all duration-300"><i data-lucide="x" class="w-4 h-4 sm:w-5 sm:h-5"></i></button>
            </div>
            <div class="p-4 sm:p-6 overflow-y-auto flex-1 scrollable-modal-content space-y-4 sm:space-y-6">
                <!-- Change Password Section -->
                <div>
                    <h4 class="text-xs sm:text-sm font-semibold text-slate-200 mb-3 sm:mb-4 flex items-center gap-2 font-english">
                        <i data-lucide="key" class="w-3 h-3 sm:w-4 sm:h-4 text-blue-400"></i>
                        Change Password
                    </h4>
                    <div class="space-y-3 sm:space-y-4">
                        <div>
                            <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Current Password</label>
                            <input type="password" id="settings-current-pw" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 input-focus-ring font-english" placeholder="Enter current password">
                        </div>
                        <div>
                            <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">New Password</label>
                            <input type="password" id="settings-new-pw" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 input-focus-ring font-english" placeholder="At least 4 characters">
                        </div>
                        <div>
                            <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Confirm New Password</label>
                            <input type="password" id="settings-confirm-pw" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition-all duration-300 input-focus-ring font-english" placeholder="Repeat new password">
                        </div>
                        <div id="settingsError" class="text-[10px] sm:text-xs text-red-400 hidden font-english"></div>
                        <button onclick="changePassword()" class="w-full py-2 sm:py-2.5 bg-blue-600 hover:bg-blue-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-blue-600/10 hover:shadow-blue-600/25 font-english">
                            Update Password
                        </button>
                    </div>
                </div>
                <div class="border-t border-slate-800/60"></div>
                <!-- Path Settings Section -->
                <div>
                    <h4 class="text-xs sm:text-sm font-semibold text-slate-200 mb-3 sm:mb-4 flex items-center gap-2 font-english">
                        <i data-lucide="folder-tree" class="w-3 h-3 sm:w-4 sm:h-4 text-purple-400"></i>
                        Dashboard Paths
                    </h4>
                    <div class="space-y-3 sm:space-y-4">
                        <!-- Dashboard Path -->
                        <div>
                            <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Dashboard Path</label>
                            <div class="flex flex-col sm:flex-row gap-2">
                                <input type="text" id="settings-dashboard-path" class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-purple-500 transition-all duration-300 input-focus-ring-purple font-english" placeholder="/dashboard">
                                <button onclick="updatePath('dashboard')" class="sm:w-auto px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-purple-600/10 hover:shadow-purple-600/25 font-english">Update</button>
                            </div>
                            <p class="text-[9px] sm:text-[10px] text-slate-500 mt-1 font-english">Current: <span id="current-dashboard-path" class="text-slate-400 font-mono font-english">/dashboard</span></p>
                        </div>
                        
                        <!-- Login Path -->
                        <div>
                            <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Login Path</label>
                            <div class="flex flex-col sm:flex-row gap-2">
                                <input type="text" id="settings-login-path" class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-purple-500 transition-all duration-300 input-focus-ring-purple font-english" placeholder="/login">
                                <button onclick="updatePath('login')" class="sm:w-auto px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-purple-600/10 hover:shadow-purple-600/25 font-english">Update</button>
                            </div>
                            <p class="text-[9px] sm:text-[10px] text-slate-500 mt-1 font-english">Current: <span id="current-login-path" class="text-slate-400 font-mono font-english">/login</span></p>
                        </div>
                        
                        <!-- Subscription Path -->
                        <div>
                            <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Subscription Path</label>
                            <div class="flex flex-col sm:flex-row gap-2">
                                <input type="text" id="settings-sub-path" class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-purple-500 transition-all duration-300 input-focus-ring-purple font-english" placeholder="/sub">
                                <button onclick="updatePath('sub')" class="sm:w-auto px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-purple-600/10 hover:shadow-purple-600/25 font-english">Update</button>
                            </div>
                            <p class="text-[9px] sm:text-[10px] text-slate-500 mt-1 font-english">Current: <span id="current-sub-path" class="text-slate-400 font-mono font-english">/sub</span></p>
                        </div>
                        
                        <!-- Setup Path -->
                        <div>
                            <label class="block text-[10px] sm:text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 sm:mb-2 font-english">Setup Path</label>
                            <div class="flex flex-col sm:flex-row gap-2">
                                <input type="text" id="settings-setup-path" class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono text-slate-200 focus:outline-none focus:border-purple-500 transition-all duration-300 input-focus-ring-purple font-english" placeholder="/setup">
                                <button onclick="updatePath('setup')" class="sm:w-auto px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-purple-600/10 hover:shadow-purple-600/25 font-english">Update</button>
                            </div>
                            <p class="text-[9px] sm:text-[10px] text-slate-500 mt-1 font-english">Current: <span id="current-setup-path" class="text-slate-400 font-mono font-english">/setup</span></p>
                        </div>
                        
                        <div id="pathSettingsError" class="text-[10px] sm:text-xs text-red-400 hidden font-english"></div>
                    </div>
                </div>
            </div>
            <div class="p-3 sm:p-4 border-t border-slate-800 bg-slate-950/40 flex items-center justify-end shrink-0">
                <button onclick="toggleModal('settingsModal', false)" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs sm:text-sm font-medium rounded-xl transition-all duration-300 font-english">Close</button>
            </div>
        </div>
    </div>

    <!-- ===== MODAL: ALERT ===== -->
    <div id="customAlert" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80">
        <div class="bg-slate-900 border border-slate-800 w-full max-w-sm rounded-2xl overflow-hidden modal-glow p-4 sm:p-6 text-center space-y-3 sm:space-y-4 transition-all duration-300 transform scale-95 opacity-0 active:scale-100 active:opacity-100">
            <div class="mx-auto w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-blue-500/10 border border-blue-500/30 flex items-center justify-center text-blue-400">
                <i id="alertIcon" data-lucide="info" class="w-5 h-5 sm:w-6 sm:h-6"></i>
            </div>
            <div class="space-y-1">
                <h3 id="alertTitle" class="text-sm sm:text-base font-bold text-slate-100 font-english">Notification</h3>
                <p id="alertMessage" class="text-[11px] sm:text-xs text-slate-400 leading-relaxed px-2 font-english">Pipeline structural modifications updated successfully.</p>
            </div>
            <button onclick="toggleModal('customAlert', false)" class="w-full py-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 text-[10px] sm:text-xs font-semibold rounded-xl transition-all duration-300 font-english">Acknowledge</button>
        </div>
    </div>

    <script>
        lucide.createIcons();

        // ---- Custom confirm ----
        let _confirmResolve = null;

        function customConfirm(message) {
            document.getElementById('confirmMessage').textContent = message;
            toggleModal('confirmModal', true);
            return new Promise((resolve) => { _confirmResolve = resolve; });
        }

        function _confirmYes() {
            toggleModal('confirmModal', false);
            if (_confirmResolve) _confirmResolve(true);
            _confirmResolve = null;
        }

        function _confirmNo() {
            toggleModal('confirmModal', false);
            if (_confirmResolve) _confirmResolve(false);
            _confirmResolve = null;
        }

        // Modal toggles
        function toggleModal(modalId, show) {
            const target = document.getElementById(modalId);
            const modalContent = target.querySelector('.bg-slate-900, .bg-slate-900.border');
            if (show) {
                target.classList.add('active');
                document.body.style.overflow = 'hidden';
                if (modalContent) {
                    modalContent.style.transform = 'scale(1)';
                    modalContent.style.opacity = '1';
                }
                if (modalId === 'databaseModal') {
                    loadDatabaseInfo();
                }
                if (modalId === 'ipScannerModal') {
                    setTimeout(checkDomain, 200);
                    resetIPScannerState();
                }
            } else {
                target.classList.remove('active');
                document.body.style.overflow = '';
                if (modalContent) {
                    modalContent.style.transform = 'scale(0.95)';
                    modalContent.style.opacity = '0';
                }
                if (modalId === 'ipScannerModal') {
                    if (scanInterval) {
                        clearInterval(scanInterval);
                        scanInterval = null;
                    }
                }
            }
            if (modalId === 'settingsModal' && show) {
                loadSettingsPaths();
                document.getElementById('settings-current-pw').value = '';
                document.getElementById('settings-new-pw').value = '';
                document.getElementById('settings-confirm-pw').value = '';
                document.getElementById('settingsError').classList.add('hidden');
                document.getElementById('pathSettingsError').classList.add('hidden');
            }
        }

        // Toast
        function toast(msg, type = '') {
            const el = document.getElementById('toast');
            el.textContent = msg;
            el.className = 'toast show' + (type ? ' ' + type : '');
            clearTimeout(el._timeout);
            el._timeout = setTimeout(() => el.classList.remove('show'), 2500);
        }

        // Copy
        function copyLink(inputId) {
            const inp = document.getElementById(inputId);
            inp.select();
            navigator.clipboard.writeText(inp.value);
            triggerAlert('Token Copied', 'Configuration token copied to clipboard.', 'check-circle');
        }

        // Alert
        function triggerAlert(title, message, iconName) {
            document.getElementById('alertTitle').textContent = title;
            document.getElementById('alertMessage').textContent = message;
            const icon = document.getElementById('alertIcon');
            icon.setAttribute('data-lucide', iconName);
            lucide.createIcons();
            toggleModal('customAlert', true);
        }

        // ===== DATABASE FUNCTIONS =====
        let selectedFile = null;

        function loadDatabaseInfo() {
            fetch('/api/links')
                .then(res => res.json())
                .then(data => {
                    const links = data.links || [];
                    let totalTraffic = 0;
                    let activeCount = 0;
                    
                    links.forEach(l => {
                        totalTraffic += l.used_bytes || 0;
                        if (l.active) activeCount++;
                    });

                    document.getElementById('db-total-configs').textContent = links.length;
                    document.getElementById('db-active-configs').textContent = activeCount;
                    document.getElementById('db-total-traffic').textContent = fmtBytes(totalTraffic);
                    document.getElementById('db-last-saved').textContent = new Date().toLocaleString();

                    const tbody = document.getElementById('dbConfigsBody');
                    if (links.length === 0) {
                        tbody.innerHTML = '<tr><td colspan="6" class="text-center py-4 text-slate-500 font-english">No configurations found</td></tr>';
                    } else {
                        tbody.innerHTML = links.map(l => `
                            <tr class="border-b border-slate-800/30 hover:bg-slate-800/20 transition-colors">
                                <td class="py-2 px-2 text-slate-200 font-medium truncate max-w-[80px] font-english">${l.label || 'Unnamed'}</td>
                                <td class="py-2 px-2 text-slate-400 font-mono text-[10px] truncate max-w-[100px] font-english">${l.uuid.substring(0, 12)}...</td>
                                <td class="py-2 px-2 text-right text-blue-300 font-mono font-english">${fmtBytes(l.used_bytes || 0)}</td>
                                <td class="py-2 px-2 text-right text-amber-300 font-mono font-english">${l.limit_bytes === 0 ? '∞' : fmtBytes(l.limit_bytes)}</td>
                                <td class="py-2 px-2 text-center">
                                    <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] ${l.active ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' : 'bg-red-500/10 text-red-400 border border-red-500/20'} font-english">
                                        <span class="w-1.5 h-1.5 rounded-full ${l.active ? 'bg-emerald-400' : 'bg-red-400'}"></span>
                                        ${l.active ? 'Active' : 'Inactive'}
                                    </span>
                                </td>
                                <td class="py-2 px-2 text-right text-slate-400 font-mono font-english">${l.connected_ips || 0}</td>
                            </tr>
                        `).join('');
                    }
                })
                .catch(err => {
                    console.error('Error loading database info:', err);
                    toast('Failed to load database info', 'error');
                });
        }

        function fmtBytes(b) {
            if (b === 0) return '0 B';
            if (b < 1024) return b + ' B';
            if (b < 1024 ** 2) return (b / 1024).toFixed(1) + ' KB';
            if (b < 1024 ** 3) return (b / 1024 ** 2).toFixed(2) + ' MB';
            return (b / 1024 ** 3).toFixed(2) + ' GB';
        }

        // Download Database
        function downloadDatabase() {
            fetch('/api/database/export')
                .then(res => {
                    if (!res.ok) throw new Error('Failed to export database');
                    return res.json();
                })
                .then(data => {
                    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'mx-ui.json';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                    toast('Database downloaded successfully!', 'success');
                })
                .catch(err => {
                    console.error('Download error:', err);
                    toast('Failed to download database: ' + err.message, 'error');
                });
        }

        // File drop zone handlers
        const dropZone = document.getElementById('dropZone');
        if (dropZone) {
            dropZone.addEventListener('dragover', function(e) {
                e.preventDefault();
                this.classList.add('dragover');
            });
            dropZone.addEventListener('dragleave', function(e) {
                e.preventDefault();
                this.classList.remove('dragover');
            });
            dropZone.addEventListener('drop', function(e) {
                e.preventDefault();
                this.classList.remove('dragover');
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    handleFile(files[0]);
                }
            });
        }

        function handleFileSelect(event) {
            const file = event.target.files[0];
            if (file) {
                handleFile(file);
            }
        }

        function handleFile(file) {
            if (file.name !== 'mx-ui.json') {
                toast('Please select a valid mx-ui.json file', 'error');
                return;
            }
            selectedFile = file;
            document.getElementById('fileName').textContent = file.name + ' (' + (file.size / 1024).toFixed(2) + ' KB)';
            document.getElementById('dropZone').classList.add('has-file');
            document.getElementById('restoreBtn').disabled = false;
            toast('File loaded: ' + file.name, 'info');
        }

        // Restore Database
        function restoreDatabase() {
            if (!selectedFile) {
                toast('Please select a file first', 'error');
                return;
            }

            const reader = new FileReader();
            reader.onload = function(e) {
                try {
                    const data = JSON.parse(e.target.result);
                    
                    if (!data.links) {
                        toast('Invalid database file format', 'error');
                        return;
                    }

                    fetch('/api/database/restore', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(data)
                    })
                    .then(res => {
                        if (!res.ok) throw new Error('Restore failed');
                        return res.json();
                    })
                    .then(result => {
                        if (result.password_reset) {
                            toast('✅ Database restored! Password reset to: MUVIXO', 'success');
                        } else {
                            toast('✅ Database restored successfully!', 'success');
                        }
                        
                        document.getElementById('restoreBtn').disabled = true;
                        document.getElementById('dropZone').classList.remove('has-file');
                        document.getElementById('fileName').textContent = 'No file selected';
                        selectedFile = null;
                        loadDatabaseInfo();
                        loadConfigs();
                        setTimeout(updateStats, 500);
                        
                        if (result.requires_login) {
                            setTimeout(async () => {
                                try {
                                    await fetch('/api/logout', { method: 'POST' });
                                    const paths = await getCurrentPaths();
                                    location.href = paths.login;
                                } catch (e) {
                                    location.href = '/login';
                                }
                            }, 3000);
                        }
                    })
                    .catch(err => {
                        toast('❌ Restore failed: ' + err.message, 'error');
                    });
                } catch (err) {
                    toast('❌ Invalid JSON file: ' + err.message, 'error');
                }
            };
            reader.readAsText(selectedFile);
        }

        // QR Modal
        function openQrModal(label, uriPayload, subUrl) {
            document.getElementById('qrTargetLabel').textContent = label;
            document.getElementById('qrTextPayload').textContent = uriPayload;
            document.getElementById('qrSubPayload').textContent = subUrl;
            
            const qrImg = document.getElementById('qrImage');
            const qrSubImg = document.getElementById('qrSubImage');
            
            fetch(`/api/qr?data=${encodeURIComponent(uriPayload)}&size=300`)
                .then(res => res.json())
                .then(data => {
                    if (data.qr) {
                        qrImg.src = data.qr;
                    }
                })
                .catch(() => {
                    qrImg.src = `/api/qr?data=${encodeURIComponent(uriPayload)}&size=300&format=image`;
                });
            
            fetch(`/api/qr?data=${encodeURIComponent(subUrl)}&size=300`)
                .then(res => res.json())
                .then(data => {
                    if (data.qr) {
                        qrSubImg.src = data.qr;
                    }
                })
                .catch(() => {
                    qrSubImg.src = `/api/qr?data=${encodeURIComponent(subUrl)}&size=300&format=image`;
                });
            
            toggleModal('qrModal', true);
        }

        // Copy text function
        function copyText(text) {
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(text).then(() => {
                    toast('Copied to clipboard!', 'success');
                }).catch(() => {
                    fallbackCopyText(text);
                });
            } else {
                fallbackCopyText(text);
            }
        }

        function fallbackCopyText(text) {
            const textarea = document.createElement('textarea');
            textarea.value = text;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            textarea.style.left = '-9999px';
            document.body.appendChild(textarea);
            textarea.select();
            try {
                document.execCommand('copy');
                toast('Copied to clipboard!', 'success');
            } catch (e) {
                toast('Failed to copy', 'error');
            }
            document.body.removeChild(textarea);
        }

        // Edit modal
        function openEditModal(label, protocol, fingerprint, alpn, limit, expiry, iplimit, speed, unit, uuid) {
            document.getElementById('editNodeTitle').textContent = label;
            document.getElementById('edit-uuid').value = uuid;
            document.getElementById('edit-label').value = label;
            document.getElementById('edit-protocol').value = protocol;
            document.getElementById('edit-fp').value = fingerprint;
            document.getElementById('edit-alpn').value = alpn || '';
            document.getElementById('edit-limit').value = limit;
            document.getElementById('edit-expiry').value = expiry;
            document.getElementById('edit-iplimit').value = iplimit;
            document.getElementById('edit-speed').value = speed;
            document.getElementById('edit-speed-unit').value = unit || 'MBIT';
            toggleModal('editModal', true);
        }

        // Get current paths
        async function getCurrentPaths() {
            try {
                const res = await fetch('/api/current-paths');
                if (!res.ok) throw new Error('Failed to fetch paths');
                const data = await res.json();
                return data;
            } catch (e) {
                console.error('Error fetching paths:', e);
                return { dashboard: '/dashboard', login: '/login', sub: '/sub' };
            }
        }

        // Logout
        async function logout() {
            try {
                const paths = await getCurrentPaths();
                await fetch('/api/logout', { method: 'POST' });
                location.href = paths.login;
            } catch (e) {
                await fetch('/api/logout', { method: 'POST' });
                location.href = '/login';
            }
        }

        // ---- Toggle System Details ----
        let systemDetailsVisible = false;

        function toggleSystemDetails() {
            systemDetailsVisible = !systemDetailsVisible;
            const wrapper = document.getElementById('systemDetailsWrapper');
            const icon = document.getElementById('toggleSystemIcon');
            const text = document.getElementById('toggleSystemText');
            
            if (systemDetailsVisible) {
                wrapper.classList.add('open');
                icon.classList.add('rotated');
                text.textContent = 'Show Less';
                setTimeout(() => {
                    updateSystemDetails();
                }, 100);
            } else {
                wrapper.classList.remove('open');
                icon.classList.remove('rotated');
                text.textContent = 'Show More';
            }
            setTimeout(() => {
                lucide.createIcons();
            }, 50);
        }

        // ---- Update System Details ----
        async function updateSystemDetails() {
            try {
                const res = await fetch('/stats');
                const d = await res.json();
                
                document.getElementById('cpu-load-avg').textContent = d.cpu_percent ? d.cpu_percent.toFixed(1) + '%' : '--';
                document.getElementById('cpu-cores-detail').textContent = d.cpu_cores ? d.cpu_cores + ' Cores' : '--';
                const cpuPct = d.cpu_percent || 0;
                document.getElementById('cpu-user').textContent = (cpuPct * 0.7).toFixed(1) + '%';
                document.getElementById('cpu-system').textContent = (cpuPct * 0.3).toFixed(1) + '%';
                document.getElementById('cpu-idle').textContent = (100 - cpuPct).toFixed(1) + '%';
                
                const ramTotal = d.ram_total_mb || 0;
                const ramUsed = d.ram_used_mb || 0;
                document.getElementById('ram-total-detail').textContent = (ramTotal / 1024).toFixed(2) + ' GB';
                document.getElementById('ram-used-detail').textContent = (ramUsed / 1024).toFixed(2) + ' GB';
                document.getElementById('ram-free-detail').textContent = ((ramTotal - ramUsed) / 1024).toFixed(2) + ' GB';
                document.getElementById('ram-available-detail').textContent = ((ramTotal - ramUsed) / 1024).toFixed(2) + ' GB';
                document.getElementById('ram-cached-detail').textContent = ((ramTotal - ramUsed) * 0.3 / 1024).toFixed(2) + ' GB';
                
                const swapTotal = d.swap_total_mb || 0;
                const swapUsed = d.swap_used_mb || 0;
                document.getElementById('swap-total-detail').textContent = (swapTotal / 1024).toFixed(2) + ' GB';
                document.getElementById('swap-used-detail').textContent = (swapUsed / 1024).toFixed(2) + ' GB';
                document.getElementById('swap-free-detail').textContent = ((swapTotal - swapUsed) / 1024).toFixed(2) + ' GB';
                document.getElementById('swap-usage-detail').textContent = d.swap_percent ? d.swap_percent.toFixed(1) + '%' : '0%';
                
                const diskTotal = d.disk_total_gb || 0;
                const diskUsed = d.disk_used_gb || 0;
                document.getElementById('disk-total-detail').textContent = diskTotal.toFixed(2) + ' TB';
                document.getElementById('disk-used-detail').textContent = diskUsed.toFixed(2) + ' TB';
                document.getElementById('disk-free-detail').textContent = (diskTotal - diskUsed).toFixed(2) + ' TB';
                document.getElementById('disk-usage-detail').textContent = d.disk_percent ? d.disk_percent.toFixed(1) + '%' : '0%';
                
                const totalTraffic = d.total_traffic_mb || 0;
                document.getElementById('network-total').textContent = totalTraffic.toFixed(2) + ' MB';
                document.getElementById('network-requests').textContent = d.total_requests || 0;
                document.getElementById('network-connections').textContent = d.active_connections || 0;
                document.getElementById('network-errors').textContent = d.total_errors || 0;
                
                document.getElementById('sys-uptime').textContent = d.uptime || '00:00:00';
                document.getElementById('sys-active-configs').textContent = d.active_links || 0;
                document.getElementById('sys-total-configs').textContent = d.links_count || 0;
                document.getElementById('sys-expired-configs').textContent = d.expired_links || 0;
                
            } catch (e) {
                console.error('Error updating system details:', e);
            }
        }

        // Change Password - Updated
        async function changePassword() {
            const cur = document.getElementById('settings-current-pw').value;
            const nw = document.getElementById('settings-new-pw').value;
            const confirmPw = document.getElementById('settings-confirm-pw').value;
            const errEl = document.getElementById('settingsError');
            errEl.classList.add('hidden');

            if (!cur || !nw || !confirmPw) {
                errEl.textContent = 'All fields are required.';
                errEl.classList.remove('hidden');
                return;
            }
            if (nw.length < 4) {
                errEl.textContent = 'New password must be at least 4 characters.';
                errEl.classList.remove('hidden');
                return;
            }
            if (nw !== confirmPw) {
                errEl.textContent = 'New password and confirmation do not match.';
                errEl.classList.remove('hidden');
                return;
            }

            try {
                const res = await fetch('/api/change-password', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ current_password: cur, new_password: nw })
                });
                const data = await res.json().catch(() => ({}));
                if (!res.ok) throw new Error(data.detail || 'Failed to update password');

                toggleModal('settingsModal', false);
                triggerAlert('Password Updated', 'Your password has been changed successfully. You will be logged out.', 'check-circle');

                setTimeout(async () => {
                    try {
                        await fetch('/api/logout', { method: 'POST' });
                        const paths = await getCurrentPaths();
                        location.href = paths.login;
                    } catch (e) {
                        location.href = '/login';
                    }
                }, 2000);

            } catch (e) {
                errEl.textContent = e.message;
                errEl.classList.remove('hidden');
            }
        }

        // ---- Settings: update paths ----
        async function updatePath(type) {
            const errEl = document.getElementById('pathSettingsError');
            errEl.classList.add('hidden');

            let pathInput;
            if (type === 'dashboard') {
                pathInput = document.getElementById('settings-dashboard-path');
            } else if (type === 'login') {
                pathInput = document.getElementById('settings-login-path');
            } else if (type === 'sub') {
                pathInput = document.getElementById('settings-sub-path');
            } else if (type === 'setup') {
                pathInput = document.getElementById('settings-setup-path');
            }

            let newPath = pathInput.value.trim();
            if (!newPath) {
                errEl.textContent = 'Path cannot be empty.';
                errEl.classList.remove('hidden');
                return;
            }
            if (!newPath.startsWith('/')) {
                newPath = '/' + newPath;
            }
            if (!/^\/[a-zA-Z0-9\-_/]*$/.test(newPath)) {
                errEl.textContent = 'Path must start with / and contain only letters, numbers, hyphens, underscores, and slashes.';
                errEl.classList.remove('hidden');
                return;
            }

            try {
                const res = await fetch('/api/update-path', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ path_type: type, new_path: newPath })
                });
                const data = await res.json().catch(() => ({}));
                if (!res.ok) throw new Error(data.detail || 'Failed to update path');

                document.getElementById('current-' + type + '-path').textContent = newPath;
                pathInput.value = '';
                triggerAlert('Path Updated', type.charAt(0).toUpperCase() + type.slice(1) + ' path changed to: ' + newPath, 'check-circle');

                if (type === 'dashboard') {
                    setTimeout(() => {
                        location.href = newPath;
                    }, 1500);
                }
                if (type === 'setup') {
                    setTimeout(() => {
                        location.href = newPath;
                    }, 1500);
                }
            } catch (e) {
                errEl.textContent = e.message;
                errEl.classList.remove('hidden');
            }
        }

        // ---- Load current paths ----
        async function loadSettingsPaths() {
            try {
                const res = await fetch('/api/get-paths');
                const data = await res.json();

                document.getElementById('current-dashboard-path').textContent = data.dashboard_path || '/dashboard';
                document.getElementById('current-login-path').textContent = data.login_path || '/login';
                document.getElementById('current-sub-path').textContent = data.sub_path || '/sub';
                document.getElementById('current-setup-path').textContent = data.setup_path || '/setup';

                const dashboardInput = document.getElementById('settings-dashboard-path');
                const loginInput = document.getElementById('settings-login-path');
                const subInput = document.getElementById('settings-sub-path');
                const setupInput = document.getElementById('settings-setup-path');

                if (dashboardInput) dashboardInput.placeholder = data.dashboard_path || '/dashboard';
                if (loginInput) loginInput.placeholder = data.login_path || '/login';
                if (subInput) subInput.placeholder = data.sub_path || '/sub';
                if (setupInput) setupInput.placeholder = data.setup_path || '/setup';
            } catch (e) {
                console.error('Error loading paths:', e);
            }
        }

        // ---- Reset Traffic ----
        async function resetTraffic(uuid) {
            const ok = await customConfirm('Reset traffic for this configuration?');
            if (!ok) return;
            try {
                const res = await fetch('/api/links/' + uuid + '/reset-traffic', { method: 'POST' });
                if (!res.ok) throw new Error('Failed');
                toast('Traffic reset successfully', 'success');
                loadConfigs();
            } catch (e) {
                toast('Error resetting traffic', 'error');
            }
        }

        // ---- Toggle Config Status ----
        async function toggleConfigStatus(uuid, enabled) {
            try {
                const res = await fetch('/api/links/' + uuid + '/toggle', {
                    method: 'PATCH',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ active: enabled })
                });
                if (!res.ok) throw new Error('Failed to toggle status');
                const data = await res.json();
                
                const row = document.querySelector(`.config-row[data-uuid="${uuid}"]`);
                if (row) {
                    const statusSpan = row.querySelector('.text-emerald-400, .text-red-400');
                    const statusDot = statusSpan?.querySelector('.status-dot');
                    
                    if (statusSpan && statusDot) {
                        if (enabled) {
                            statusSpan.className = 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20 text-[8px] sm:text-[10px] px-1.5 py-0.5 rounded font-medium shrink-0 font-english';
                            statusSpan.innerHTML = `<span class="status-dot active"></span>Active`;
                            statusDot.className = 'status-dot active';
                        } else {
                            statusSpan.className = 'text-red-400 bg-red-500/10 border-red-500/20 text-[8px] sm:text-[10px] px-1.5 py-0.5 rounded font-medium shrink-0 font-english';
                            statusSpan.innerHTML = `<span class="status-dot inactive"></span>Inactive`;
                            statusDot.className = 'status-dot inactive';
                        }
                    }
                    
                    const toggleLabel = row.querySelector('.group .toggle-label');
                    if (toggleLabel) {
                        toggleLabel.textContent = enabled ? 'Enabled' : 'Disabled';
                    }
                }
                
                toast('Config ' + (enabled ? 'enabled' : 'disabled'), 'success');
            } catch (e) {
                toast('Error toggling status', 'error');
                const checkbox = document.querySelector(`.config-row[data-uuid="${uuid}"] input[type="checkbox"]`);
                if (checkbox) {
                    checkbox.checked = !enabled;
                }
            }
        }

        // ===== IP SCANNER FUNCTIONS =====
        let selectedIP = null;
        let scanResults = [];
        let scanInterval = null;

        function resetIPScannerState() {
            document.getElementById('scanProgressContainer').classList.add('hidden');
            document.getElementById('scanResultsContainer').classList.add('hidden');
            document.getElementById('scanStartBtn').disabled = false;
            document.getElementById('scanStartBtn').innerHTML = '<i data-lucide="play" class="w-4 h-4"></i> Start Scan';
            document.getElementById('scanCancelBtn').classList.add('hidden');
            if (scanInterval) {
                clearInterval(scanInterval);
                scanInterval = null;
            }
            selectedIP = null;
            document.getElementById('applyIPBtn').disabled = true;
            document.getElementById('applyIPBtn').innerHTML = '<i data-lucide="check" class="w-3.5 h-3.5"></i> Apply Selected';
            document.getElementById('applyStatus').textContent = 'Select an IP to apply';
            document.getElementById('scanProgressBar').style.width = '0%';
            document.getElementById('scanProgressPercent').textContent = '0%';
            document.getElementById('scanStats').textContent = 'Found: 0 IPs';
            document.getElementById('scanStatus').textContent = 'Idle';
            setTimeout(lucide.createIcons, 50);
        }

        async function checkDomain() {
            try {
                const res = await fetch('/api/ipscanner/check-domain');
                const data = await res.json();
                
                const icon = document.getElementById('domainCheckIcon');
                const text = document.getElementById('domainCheckText');
                
                if (data.is_railway) {
                    icon.innerHTML = '<i data-lucide="alert-triangle" class="w-4 h-4 text-amber-400"></i>';
                    text.textContent = data.message || '⚠️ Cannot modify IP on railway.app domain';
                    text.className = 'text-xs font-mono text-amber-400 font-english';
                    document.getElementById('applyIPBtn').disabled = true;
                } else {
                    icon.innerHTML = '<i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i>';
                    text.textContent = data.message || '✅ Domain is suitable for IP modification';
                    text.className = 'text-xs font-mono text-emerald-400 font-english';
                    document.getElementById('applyIPBtn').disabled = false;
                }
                lucide.createIcons();
            } catch (e) {
                console.error('Domain check failed:', e);
                const text = document.getElementById('domainCheckText');
                text.textContent = '❌ Failed to check domain: ' + e.message;
                text.className = 'text-xs font-mono text-red-400 font-english';
            }
        }

        async function startIPScan() {
            const ranges = document.getElementById('scan-ranges').value;
            const count = parseInt(document.getElementById('scan-count').value) || 100;
            const portsStr = document.getElementById('scan-ports').value;
            const ports = portsStr.split(',').map(p => parseInt(p.trim()));
            const workers = parseInt(document.getElementById('scan-workers').value) || 100;
            const timeout = parseFloat(document.getElementById('scan-timeout').value) || 3;
            
            if (count < 1 || count > 10000) {
                toast('IP count must be between 1 and 10000', 'error');
                return;
            }
            
            const btn = document.getElementById('scanStartBtn');
            const cancelBtn = document.getElementById('scanCancelBtn');
            const container = document.getElementById('scanProgressContainer');
            const resultsContainer = document.getElementById('scanResultsContainer');
            
            btn.disabled = true;
            btn.innerHTML = '<div class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div> Scanning...';
            cancelBtn.classList.remove('hidden');
            container.classList.remove('hidden');
            resultsContainer.classList.add('hidden');
            document.getElementById('scanProgressBar').style.width = '0%';
            document.getElementById('scanProgressPercent').textContent = '0%';
            document.getElementById('scanStats').textContent = 'Found: 0 IPs';
            document.getElementById('scanStatus').textContent = 'Starting...';
            lucide.createIcons();
            
            try {
                const res = await fetch('/api/ipscanner/scan', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        ip_range: ranges,
                        count_per_range: count,
                        ports: ports,
                        workers: workers,
                        timeout: timeout
                    })
                });
                
                if (!res.ok) {
                    const err = await res.json();
                    throw new Error(err.detail || 'Scan failed');
                }
                
                const data = await res.json();
                toast('Scan started: ' + data.message, 'info');
                
                if (scanInterval) clearInterval(scanInterval);
                scanInterval = setInterval(pollScanStatus, 1000);
                
            } catch (e) {
                toast('Error: ' + e.message, 'error');
                btn.disabled = false;
                btn.innerHTML = '<i data-lucide="play" class="w-4 h-4"></i> Start Scan';
                cancelBtn.classList.add('hidden');
                lucide.createIcons();
            }
        }

        async function pollScanStatus() {
            try {
                const res = await fetch('/api/ipscanner/status');
                const data = await res.json();
                
                document.getElementById('scanProgressBar').style.width = data.progress + '%';
                document.getElementById('scanProgressPercent').textContent = Math.round(data.progress) + '%';
                document.getElementById('scanStats').textContent = `Found: ${data.found} IPs`;
                document.getElementById('scanStatus').textContent = data.status_message || 'Scanning...';
                
                if (!data.is_running) {
                    clearInterval(scanInterval);
                    scanInterval = null;
                    
                    document.getElementById('scanStartBtn').disabled = false;
                    document.getElementById('scanStartBtn').innerHTML = '<i data-lucide="play" class="w-4 h-4"></i> Start Scan';
                    document.getElementById('scanCancelBtn').classList.add('hidden');
                    document.getElementById('scanStatus').textContent = 'Scan complete!';
                    lucide.createIcons();
                    
                    await loadScanResults();
                }
            } catch (e) {
                console.error('Status poll error:', e);
            }
        }

        async function loadScanResults() {
            try {
                const res = await fetch('/api/ipscanner/results?limit=10');
                const data = await res.json();
                
                const container = document.getElementById('scanResultsContainer');
                const tbody = document.getElementById('scanResultsBody');
                
                if (!data.results || data.results.length === 0) {
                    tbody.innerHTML = '<tr><td colspan="7" class="text-center py-4 text-slate-500 font-english">No results found</td></tr>';
                    container.classList.remove('hidden');
                    return;
                }
                
                scanResults = data.results;
                document.getElementById('totalFoundLabel').textContent = `Total: ${data.total_found} IPs`;
                
                tbody.innerHTML = data.results.map((r, idx) => {
                    const rankEmoji = idx === 0 ? '🥇' : idx === 1 ? '🥈' : idx === 2 ? '🥉' : `#${r.rank}`;
                    const ratingClass = r.rating ? r.rating.toLowerCase() : '';
                    const ratingDisplay = r.rating || 'N/A';
                    const pingColor = r.ping && r.ping < 30 ? 'text-emerald-400' : 
                                     r.ping && r.ping < 60 ? 'text-amber-400' : 'text-red-400';
                    
                    return `
                        <tr class="ip-result-row border-b border-slate-800/30 hover:bg-slate-800/20 transition-colors" 
                            onclick="selectIPResult('${r.ip}', ${r.port}, ${idx})"
                            id="ip-row-${idx}">
                            <td class="py-2 px-2 text-slate-400 font-mono font-english">${rankEmoji}</td>
                            <td class="py-2 px-2 text-slate-200 font-mono font-english">${r.ip}</td>
                            <td class="py-2 px-2 text-amber-400 font-mono font-english">${r.port}</td>
                            <td class="py-2 px-2 ${pingColor} font-mono font-english">${r.ping ? r.ping.toFixed(1) : 'N/A'}</td>
                            <td class="py-2 px-2 text-slate-300 font-mono font-english">${r.speed ? r.speed.toFixed(1) : 'N/A'}</td>
                            <td class="py-2 px-2">
                                <span class="rating-badge ${ratingClass} font-english">${ratingDisplay}</span>
                            </td>
                            <td class="py-2 px-2 text-center">
                                <button onclick="event.stopPropagation(); selectIPResult('${r.ip}', ${r.port}, ${idx})" 
                                        class="ip-select-btn px-2 py-0.5 rounded text-[10px] bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 hover:bg-cyan-500/20 transition font-english">
                                    Select
                                </button>
                            </td>
                        </tr>
                    `;
                }).join('');
                
                container.classList.remove('hidden');
                lucide.createIcons();
                
            } catch (e) {
                console.error('Load results error:', e);
                toast('Failed to load results', 'error');
            }
        }

        function selectIPResult(ip, port, idx) {
            document.querySelectorAll('#scanResultsBody tr').forEach(el => {
                el.classList.remove('selected');
            });
            
            const row = document.getElementById(`ip-row-${idx}`);
            if (row) {
                row.classList.add('selected');
            }
            
            selectedIP = { ip, port };
            document.getElementById('applyIPBtn').disabled = false;
            document.getElementById('applyIPBtn').innerHTML = `<i data-lucide="check" class="w-3.5 h-3.5"></i> Apply ${ip}:${port}`;
            document.getElementById('applyStatus').textContent = `Selected: ${ip}:${port}`;
            setTimeout(lucide.createIcons, 50);
        }

        function cancelIPScan() {
            if (scanInterval) {
                clearInterval(scanInterval);
                scanInterval = null;
            }
            
            document.getElementById('scanStartBtn').disabled = false;
            document.getElementById('scanStartBtn').innerHTML = '<i data-lucide="play" class="w-4 h-4"></i> Start Scan';
            document.getElementById('scanCancelBtn').classList.add('hidden');
            document.getElementById('scanStatus').textContent = 'Cancelled';
            toast('Scan cancelled', 'info');
            lucide.createIcons();
        }

        async function applySelectedIP() {
            if (!selectedIP) {
                toast('Please select an IP first', 'error');
                return;
            }
            
            const domainRes = await fetch('/api/ipscanner/check-domain');
            const domainData = await domainRes.json();
            if (domainData.is_railway) {
                toast('Cannot modify IP on railway.app domain', 'error');
                return;
            }
            
            const configs = await fetch('/api/links').then(r => r.json());
            const links = configs.links || [];
            
            if (links.length === 0) {
                toast('No configurations available', 'error');
                return;
            }
            
            const target = links.find(l => !l.is_default);
            if (!target) {
                toast('No config available for IP modification', 'error');
                return;
            }
            
            const confirmApply = await customConfirm(
                `Apply IP ${selectedIP.ip}:${selectedIP.port} to config "${target.label || 'Unnamed'}"?`
            );
            
            if (!confirmApply) return;
            
            try {
                const res = await fetch('/api/ipscanner/apply', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        uuid: target.uuid,
                        new_ip: selectedIP.ip,
                        new_port: selectedIP.port
                    })
                });
                
                if (!res.ok) {
                    const err = await res.json();
                    throw new Error(err.detail || 'Failed to apply IP');
                }
                
                const data = await res.json();
                toast(`✅ Applied ${selectedIP.ip}:${selectedIP.port} to config`, 'success');
                
                loadConfigs();
                
                document.querySelectorAll('#scanResultsBody tr').forEach(el => {
                    el.classList.remove('selected');
                });
                selectedIP = null;
                document.getElementById('applyIPBtn').disabled = true;
                document.getElementById('applyIPBtn').innerHTML = '<i data-lucide="check" class="w-3.5 h-3.5"></i> Apply Selected';
                document.getElementById('applyStatus').textContent = 'Select an IP to apply';
                setTimeout(lucide.createIcons, 50);
                
            } catch (e) {
                toast('Error: ' + e.message, 'error');
            }
        }

        // ---- Fetch and render configs ----
        async function loadConfigs() {
            try {
                const res = await fetch('/api/links');
                if (!res.ok) throw new Error('Unauthorized');
                const data = await res.json();
                const links = data.links || [];
                const container = document.getElementById('config-list');
                if (!links.length) {
                    container.innerHTML = '<div class="p-6 text-center text-slate-400 text-sm font-english">No configurations yet. Click "Add Config" to create one.</div>';
                    return;
                }
                container.innerHTML = links.map(l => {
                    const protoLabels = {
                        'vless-ws': 'VLESS',
                        'xhttp-packet-up': 'XHTTP',
                        'xhttp-stream-up': 'XHTTP'
                    };
                    const proto = l.protocol || 'vless-ws';
                    const label = l.label || 'Unnamed';
                    const isDefault = l.is_default || false;
                    const active = l.active && !l.expired;
                    const limit = l.limit_bytes === 0 ? '∞' : fmtBytes(l.limit_bytes);
                    const used = fmtBytes(l.used_bytes || 0);
                    const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
                    const color = pct > 90 ? '#ef4444' : pct > 70 ? '#f59e0b' : '#3b82f6';
                    let speedDisplay = '∞';
                    if (l.speed_limit_bytes && l.speed_limit_bytes > 0) {
                        speedDisplay = (l.speed_limit_bytes * 8 / 1024 / 1024).toFixed(1) + ' Mbps';
                    }
                    const statusDot = active ? 'status-dot active' : 'status-dot inactive';
                    const statusText = active ? 'Active' : 'Inactive';
                    const statusClass = active ? 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20' :
                        'text-red-400 bg-red-500/10 border-red-500/20';

                    const actionButtons = isDefault ? `
                        <span class="text-[10px] text-amber-400 bg-amber-500/10 px-2 py-1 rounded border border-amber-500/20 font-english" title="Default configuration - cannot be modified">
                            <i data-lucide="shield" class="w-3 h-3 inline mr-1"></i>Protected
                        </span>
                    ` : `
                        <button onclick="openEditModal('${label}','${proto}','${l.fingerprint||'chrome'}','${l.alpn||''}',${l.limit_bytes ? (l.limit_bytes / 1024 / 1024) : 0},${l.expires_at ? Math.ceil((new Date(l.expires_at) - Date.now()) / (86400000)) : 0},${l.ip_limit||0},${l.speed_limit_bytes ? (l.speed_limit_bytes * 8 / 1024 / 1024) : 0},'${l.speed_limit_unit || 'MBIT'}','${l.uuid}')" class="p-1.5 sm:p-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 rounded-xl transition-all duration-300" title="Edit"><i data-lucide="edit-3" class="w-3 h-3 sm:w-4 sm:h-4"></i></button>
                        <button onclick="resetTraffic('${l.uuid}')" class="p-1.5 sm:p-2 bg-blue-800/20 hover:bg-blue-800/40 border border-blue-700/30 text-blue-300 rounded-xl transition-all duration-300" title="Reset Traffic"><i data-lucide="rotate-ccw" class="w-3 h-3 sm:w-4 sm:h-4"></i></button>
                        <button onclick="deleteConfig('${l.uuid}')" class="p-1.5 sm:p-2 bg-red-800/20 hover:bg-red-800/40 border border-red-700/30 text-red-300 rounded-xl transition-all duration-300" title="Delete"><i data-lucide="trash-2" class="w-3 h-3 sm:w-4 sm:h-4"></i></button>
                    `;

                    const toggleHtml = isDefault ? `
                        <label class="relative inline-flex items-center cursor-not-allowed group shrink-0 opacity-60">
                            <input type="checkbox" class="sr-only" ${active ? 'checked' : ''} disabled>
                            <div class="w-9 h-5 bg-slate-600 rounded-full after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all ${active ? 'after:translate-x-full' : ''}"></div>
                            <span class="toggle-label transition-all duration-300 font-english">${active ? 'Enabled' : 'Disabled'}</span>
                        </label>
                    ` : `
                        <label class="relative inline-flex items-center cursor-pointer group shrink-0">
                            <input type="checkbox" class="sr-only peer" ${active ? 'checked' : ''} onchange="toggleConfigStatus('${l.uuid}', this.checked)">
                            <div class="w-9 h-5 bg-slate-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-emerald-600 peer-checked:border-emerald-600"></div>
                            <span class="toggle-label transition-all duration-300 group-hover:text-slate-200 font-english">${active ? 'Enabled' : 'Disabled'}</span>
                        </label>
                    `;

                    const defaultBadge = isDefault ? `<span class="text-[8px] bg-amber-500/20 text-amber-400 px-1.5 py-0.5 rounded font-mono font-english">Default</span>` : '';

                    return `
                    <div class="p-4 sm:p-6 config-row transition-all duration-200 hover:bg-slate-800/20 ${isDefault ? 'border-l-2 border-amber-500/50' : ''}" data-uuid="${l.uuid}">
                        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 lg:gap-6">
                            <div class="flex items-start space-x-3 sm:space-x-4 min-w-0">
                                <span class="inline-flex items-center px-2 sm:px-3 py-0.5 sm:py-1 rounded-md text-[9px] sm:text-xs font-bold bg-blue-500/10 text-blue-400 border border-blue-500/20 uppercase tracking-wide mt-0.5 font-mono shrink-0 font-english">${protoLabels[proto] || proto}</span>
                                <div class="min-w-0 flex-1">
                                    <div class="flex flex-wrap items-center gap-2">
                                        <h3 class="text-sm sm:text-base font-semibold text-slate-200 truncate font-mixed">${label}</h3>
                                        ${defaultBadge}
                                        <span class="text-[8px] sm:text-[10px] px-1.5 py-0.5 rounded font-medium ${statusClass} shrink-0 transition-all duration-300 font-english">
                                            <span class="${statusDot}"></span>${statusText}
                                        </span>
                                    </div>
                                    <div class="grid grid-cols-2 sm:grid-cols-3 gap-x-4 gap-y-0.5 mt-1 text-[10px] sm:text-xs text-slate-400">
                                        <div class="font-english">Network: <span class="text-slate-300 font-mono font-english">${proto.includes('ws') ? 'ws' : 'tcp'}</span></div>
                                        <div class="font-english">Security: <span class="text-slate-300 font-mono font-english">tls</span></div>
                                        <div class="col-span-2 sm:col-span-1 font-english">Expiry: <span class="text-slate-300 font-mono font-english">${l.expires_at ? new Date(l.expires_at).toISOString().slice(0,10) : 'Unlimited'}</span></div>
                                    </div>
                                    <div class="mt-1 flex flex-wrap items-center gap-2 sm:gap-4 text-[10px] sm:text-xs text-slate-400">
                                        <span class="font-english">Usage: <span class="text-slate-300 font-mono font-english">${used} / ${limit}</span></span>
                                        <span class="font-english">IP: <span class="text-slate-300 font-mono font-english">${l.ip_limit || '∞'}</span></span>
                                        <span class="font-english">Speed: <span class="text-slate-300 font-mono font-english">${speedDisplay}</span></span>
                                    </div>
                                    <div class="w-full max-w-xs mt-1.5 h-1.5 bg-slate-800/60 rounded-full overflow-hidden">
                                        <div class="h-full rounded-full transition-all duration-500" style="width: ${pct}%; background: ${color};"></div>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-wrap items-center gap-1.5 sm:gap-2 lg:justify-end">
                                ${toggleHtml}
                                
                                <div class="relative flex-grow sm:flex-grow-0 min-w-[180px] sm:min-w-[220px] max-w-full sm:max-w-xs">
                                    <input type="text" id="uri-${l.uuid}" readonly value="${l.vless_link}" class="w-full bg-slate-950 border border-slate-800/80 rounded-xl px-2 sm:px-3 py-1.5 sm:py-2 pr-7 sm:pr-10 text-[8px] sm:text-[10px] font-mono text-slate-400 focus:outline-none select-all truncate font-english">
                                    <button onclick="copyLink('uri-${l.uuid}')" class="absolute right-1.5 sm:right-2 top-1/2 -translate-y-1/2 p-0.5 sm:p-1 text-slate-500 hover:text-slate-300 transition-all duration-300"><i data-lucide="copy" class="w-3 h-3 sm:w-4 sm:h-4"></i></button>
                                </div>
                                <button onclick="openQrModal('${label}', '${l.vless_link}', '${l.sub_url}')" class="p-1.5 sm:p-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 rounded-xl transition-all duration-300" title="QR"><i data-lucide="qr-code" class="w-3 h-3 sm:w-4 sm:h-4"></i></button>
                                <button onclick="window.open('/sub/user?uuid=${l.uuid}', '_blank')" class="p-1.5 sm:p-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 rounded-xl transition-all duration-300" title="Subscription"><i data-lucide="external-link" class="w-3 h-3 sm:w-4 sm:h-4"></i></button>
                                ${actionButtons}
                            </div>
                        </div>
                    </div>`;
                }).join('');
                lucide.createIcons();
                updateStats();
                if (systemDetailsVisible) {
                    updateSystemDetails();
                }
            } catch (e) {
                if (e.message.includes('Unauthorized')) location.href = '/login';
            }
        }

        async function updateStats() {
            try {
                const res = await fetch('/stats');
                const d = await res.json();
                document.getElementById('uptime-display').textContent = d.uptime || '00:00:00';

                document.getElementById('total-traffic').textContent = d.total_traffic_mb ? d.total_traffic_mb.toFixed(1) +
                    ' MB' : '0 MB';
                document.getElementById('total-usage').textContent = d.total_traffic_mb ? (d.total_traffic_mb / 1024).toFixed(
                    2) + ' GB' : '0 GB';
                document.getElementById('total-inbounds').textContent = d.links_count || 0;
                document.getElementById('active-connections').textContent = d.active_connections || 0;

                const cpuPct = d.cpu_percent || 0;
                const cpuCores = d.cpu_cores || 0;
                document.getElementById('ring-cpu-val').textContent = cpuCores + ' Cores';
                document.getElementById('ring-cpu-pct').textContent = cpuPct.toFixed(1) + '%';
                const cpuCircle = document.querySelector('.text-blue-500.circle-chart');
                if (cpuCircle) cpuCircle.setAttribute('stroke-dasharray', Math.round(cpuPct) + ', 100');

                const ramUsed = d.ram_used_mb || 0;
                const ramTotal = d.ram_total_mb || 1;
                const ramPct = d.ram_percent || 0;
                document.getElementById('ring-ram-val').textContent = (ramUsed / 1024).toFixed(2) + ' / ' + (ramTotal /
                    1024).toFixed(2) + ' GB';
                document.getElementById('ring-ram-pct').textContent = ramPct.toFixed(1) + '%';
                const ramCircle = document.querySelector('.text-indigo-500.circle-chart');
                if (ramCircle) ramCircle.setAttribute('stroke-dasharray', Math.round(ramPct) + ', 100');

                const swapUsed = d.swap_used_mb || 0;
                const swapTotal = d.swap_total_mb || 1;
                const swapPct = d.swap_percent || 0;
                document.getElementById('ring-swap-val').textContent = (swapUsed / 1024).toFixed(2) + ' / ' + (swapTotal /
                    1024).toFixed(2) + ' GB';
                document.getElementById('ring-swap-pct').textContent = swapPct.toFixed(1) + '%';
                const swapCircle = document.querySelector('.text-amber-500.circle-chart');
                if (swapCircle) swapCircle.setAttribute('stroke-dasharray', Math.round(swapPct) + ', 100');

                const diskUsed = d.disk_used_gb || 0;
                const diskTotal = d.disk_total_gb || 1;
                const diskPct = d.disk_percent || 0;
                document.getElementById('ring-disk-val').textContent = diskUsed.toFixed(2) + ' / ' + diskTotal.toFixed(
                    2) + ' TB';
                document.getElementById('ring-disk-pct').textContent = diskPct.toFixed(1) + '%';
                const diskCircle = document.querySelector('.text-rose-500.circle-chart');
                if (diskCircle) diskCircle.setAttribute('stroke-dasharray', Math.round(diskPct) + ', 100');
            } catch (e) { console.error(e); }
        }

        async function createConfig() {
            const label = document.getElementById('new-label').value.trim() || 'New Config';
            const protocol = document.getElementById('new-protocol').value;
            const fp = document.getElementById('new-fp').value;
            const alpn = document.getElementById('new-alpn').value.trim();
            const limitMB = parseFloat(document.getElementById('new-limit').value) || 0;
            const expiryDays = parseInt(document.getElementById('new-expiry').value) || 0;
            const ipLimit = parseInt(document.getElementById('new-iplimit').value) || 0;
            const speedVal = parseFloat(document.getElementById('new-speed').value) || 0;
            const speedUnit = document.getElementById('new-speed-unit').value;

            const body = {
                label,
                protocol,
                fingerprint: fp,
                alpn,
                limit_value: limitMB,
                limit_unit: 'MB',
                expires_days: expiryDays,
                ip_limit: ipLimit,
                speed_limit_value: speedVal,
                speed_limit_unit: speedUnit
            };

            try {
                const res = await fetch('/api/links', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(body)
                });
                if (!res.ok) throw new Error('Failed');
                toggleModal('inboundModal', false);
                toast('Config created successfully', 'success');
                loadConfigs();
                document.getElementById('new-label').value = '';
                document.getElementById('new-alpn').value = '';
                document.getElementById('new-speed').value = '0';
                document.getElementById('new-limit').value = '0';
                document.getElementById('new-expiry').value = '0';
                document.getElementById('new-iplimit').value = '0';
            } catch (e) {
                toast('Error creating config', 'error');
            }
        }

        async function saveEdit() {
            const uuid = document.getElementById('edit-uuid').value;
            const label = document.getElementById('edit-label').value.trim();
            const protocol = document.getElementById('edit-protocol').value;
            const fp = document.getElementById('edit-fp').value;
            const alpn = document.getElementById('edit-alpn').value.trim();
            const limitMB = parseFloat(document.getElementById('edit-limit').value) || 0;
            const expiryDays = parseInt(document.getElementById('edit-expiry').value) || 0;
            const ipLimit = parseInt(document.getElementById('edit-iplimit').value) || 0;
            const speedVal = parseFloat(document.getElementById('edit-speed').value) || 0;
            const speedUnit = document.getElementById('edit-speed-unit').value;

            const body = {
                label,
                protocol,
                fingerprint: fp,
                alpn,
                limit_value: limitMB,
                limit_unit: 'MB',
                expires_days: expiryDays,
                ip_limit: ipLimit,
                speed_limit_value: speedVal,
                speed_limit_unit: speedUnit
            };

            try {
                const res = await fetch('/api/links/' + uuid, {
                    method: 'PATCH',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(body)
                });
                if (!res.ok) throw new Error('Failed');
                toggleModal('editModal', false);
                toast('Config updated', 'success');
                loadConfigs();
            } catch (e) {
                toast('Error updating config', 'error');
            }
        }

        async function deleteConfig(uuid) {
            const ok = await customConfirm('Delete this configuration? This action cannot be undone.');
            if (!ok) return;
            try {
                const res = await fetch('/api/links/' + uuid, { method: 'DELETE' });
                if (!res.ok) throw new Error('Failed');
                toast('Config deleted', 'success');
                loadConfigs();
            } catch (e) {
                toast('Error deleting', 'error');
            }
        }

        // Initial load
        loadConfigs();
        setInterval(() => {
            updateStats();
            if (systemDetailsVisible) {
                updateSystemDetails();
            }
        }, 5000);
        setInterval(loadConfigs, 15000);

        // Close modals on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                document.querySelectorAll('.custom-modal-overlay.active').forEach(modal => {
                    toggleModal(modal.id, false);
                });
            }
        });

        // Close modals on overlay click
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('custom-modal-overlay')) {
                toggleModal(e.target.id, false);
            }
        });
    </script>
</body>
</html>"""
# ---------- SUB_USER_HTML (for /sub/user with Persian font support) ----------
SUB_USER_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.5, user-scalable=yes">
    <title>Subscription · MX-UI</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Vazirmatn:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'Vazirmatn', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{
            background-color: #070a13;
        }}
        .glow-effect {{
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.12);
        }}
        .status-dot {{
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-right: 6px;
            flex-shrink: 0;
        }}
        .status-dot.active {{
            background-color: #22c55e;
        }}
        .status-dot.inactive {{
            background-color: #ef4444;
        }}
        .copy-btn {{
            transition: all 0.2s ease;
            min-height: 36px;
            min-width: 36px;
        }}
        .copy-btn:active {{
            transform: scale(0.95);
        }}
        .progress-bar-fill {{
            transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .qr-container {{
            transition: all 0.3s ease;
            background: white;
            border-radius: 12px;
        }}
        .qr-container:active {{
            transform: scale(0.98);
        }}
        .detail-row {{
            transition: background-color 0.15s ease;
        }}
        .detail-row:hover {{
            background-color: rgba(30, 41, 59, 0.3);
        }}
        @keyframes pulse-dot {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.3; }}
        }}
        .updating {{
            animation: pulse-dot 0.8s ease-in-out 3;
        }}
        .toast {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%) translateY(20px);
            background: #0f172a;
            border: 1px solid #1e293b;
            color: #e2e8f0;
            padding: 8px 18px;
            border-radius: 12px;
            font-size: 13px;
            font-family: 'Inter', 'Vazirmatn', sans-serif;
            opacity: 0;
            transition: opacity 0.25s, transform 0.25s;
            z-index: 9999;
            pointer-events: none;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            max-width: 90vw;
            text-align: center;
        }}
        .toast.show {{
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }}
        .toast.success {{
            border-color: #22c55e;
            color: #86efac;
        }}
        .toast.error {{
            border-color: #ef4444;
            color: #fca5a5;
        }}
        .toast.info {{
            border-color: #3b82f6;
            color: #93c5fd;
        }}
        .status-badge {{
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.025em;
            transition: all 0.3s ease;
        }}
        .status-badge.active {{
            background-color: rgba(34, 197, 94, 0.1);
            color: #4ade80;
            border: 1px solid rgba(34, 197, 94, 0.2);
        }}
        .status-badge.inactive {{
            background-color: rgba(239, 68, 68, 0.1);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.2);
        }}
        .status-badge.loading {{
            background-color: rgba(59, 130, 246, 0.1);
            color: #60a5fa;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }}
        .qr-image {{
            max-width: 100%;
            height: auto;
            transition: all 0.3s ease;
        }}
        .qr-image.loading {{
            opacity: 0.5;
            filter: blur(2px);
        }}
        .update-indicator {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 10px;
            color: #64748b;
            transition: all 0.3s ease;
        }}
        .update-indicator.updating {{
            color: #60a5fa;
        }}
        .update-spinner {{
            display: inline-block;
            width: 12px;
            height: 12px;
            border: 2px solid #1e293b;
            border-top-color: #3b82f6;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }}
        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}
        .timer-ring {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            border: 2px solid #1e293b;
            font-size: 11px;
            font-weight: 600;
            font-family: 'JetBrains Mono', monospace;
            color: #94a3b8;
            transition: all 0.3s ease;
            background: rgba(15, 23, 42, 0.5);
        }}
        .timer-ring.warning {{
            border-color: #f59e0b;
            color: #fbbf24;
        }}
        .timer-ring.critical {{
            border-color: #ef4444;
            color: #f87171;
            animation: pulse-timer 1s ease-in-out infinite;
        }}
        @keyframes pulse-timer {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
        }}
        @media (max-width: 640px) {{
            .mobile-stack {{
                flex-direction: column;
                align-items: stretch;
            }}
            .mobile-text-center {{
                text-align: center;
            }}
            .mobile-padding {{
                padding-left: 0.75rem;
                padding-right: 0.75rem;
            }}
            .mobile-gap {{
                gap: 0.5rem;
            }}
            .qr-image {{
                width: 160px;
                height: 160px;
            }}
            .timer-ring {{
                width: 24px;
                height: 24px;
                font-size: 9px;
            }}
        }}
        @media (max-width: 480px) {{
            .xs-text-xs {{
                font-size: 0.65rem;
            }}
            .xs-padding {{
                padding: 0.5rem;
            }}
            .qr-image {{
                width: 140px;
                height: 140px;
            }}
            .detail-label {{
                font-size: 0.6rem;
            }}
            .detail-value {{
                font-size: 0.65rem;
            }}
        }}
        .input-focus-ring:focus {{
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
        }}
        /* Persian font support - Vazirmatn for Persian characters */
        .font-persian {{
            font-family: 'Vazirmatn', 'Inter', sans-serif;
        }}
        .font-english {{
            font-family: 'Inter', 'Vazirmatn', sans-serif;
        }}
        .font-mixed {{
            font-family: 'Inter', 'Vazirmatn', sans-serif;
        }}
    </style>
</head>
<body class="font-sans text-slate-200 min-h-screen flex flex-col justify-between relative antialiased tracking-tight">
    
    <div class="toast" id="toast"></div>
    
    <div class="max-w-2xl w-full mx-auto px-3 sm:px-4 py-6 sm:py-10 flex-grow mobile-padding">
        <div class="bg-slate-900/80 border border-slate-800/80 rounded-2xl p-5 sm:p-8 backdrop-blur-xl glow-effect transition-all duration-300 hover:border-slate-700/80">
            
            <!-- Header -->
            <div class="flex items-center gap-3 mb-4">
                <div class="bg-blue-600 p-2 rounded-xl text-white glow-effect flex-shrink-0">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 sm:w-5 sm:h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                        <polyline points="9 12 11 14 15 10"/>
                    </svg>
                </div>
                <div class="flex-1 min-w-0">
                    <span class="font-bold text-base sm:text-lg tracking-wide bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent block truncate font-english">MX-UI PANEL</span>
                    <span class="text-[10px] sm:text-xs text-slate-500 font-medium block truncate font-english">v1.0.0</span>
                </div>
                <!-- Auto-Update Indicator with Timer -->
                <div class="flex items-center gap-2">
                    <div class="update-indicator" id="updateIndicator">
                        <span class="update-spinner" id="updateSpinner"></span>
                        <span id="updateText" class="font-english">Auto</span>
                    </div>
                    <div class="timer-ring" id="timerRing">30</div>
                </div>
            </div>

            <!-- Title Section -->
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 mb-4 sm:mb-6">
                <div class="min-w-0">
                    <h2 class="text-xl sm:text-2xl font-bold text-slate-100 truncate font-english">Subscription Info</h2>
                    <p class="text-xs sm:text-sm text-slate-400 truncate font-english">Live updates every 30 seconds</p>
                </div>
                <span id="status-badge" class="status-badge loading shrink-0 self-start sm:self-center font-english">
                    <span class="status-dot" style="background-color: #60a5fa;"></span>
                    Loading...
                </span>
            </div>

            <!-- QR Code - Clean without text -->
            <div class="mb-5 sm:mb-6 flex justify-center">
                <div class="qr-container p-2 sm:p-3 shadow-lg border-2 border-slate-700/50 transition-all duration-300 hover:border-blue-500/50">
                    <img src="{qr_url}" alt="QR Code" class="qr-image w-36 h-36 sm:w-48 sm:h-48 object-contain" id="qrImage">
                </div>
            </div>

            <!-- Details Grid -->
            <div class="space-y-1.5 sm:space-y-2 mb-5 sm:mb-6" id="detailsGrid">
                <!-- Label -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Label</span>
                    <span class="detail-value text-xs sm:text-sm font-mixed text-slate-200 font-semibold truncate" id="labelValue">{label}</span>
                </div>
                
                <!-- Subscription ID -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Subscription ID</span>
                    <span class="detail-value text-[10px] sm:text-xs font-mono text-slate-200 truncate font-english" id="uuidValue">{uuid}</span>
                </div>
                
                <!-- Status -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Status</span>
                    <span class="detail-value text-xs sm:text-sm font-mono font-semibold font-english" id="statusValue">{status}</span>
                </div>
                
                <!-- Downloaded -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Downloaded</span>
                    <span class="detail-value text-xs sm:text-sm font-mono text-blue-300 font-semibold font-english" id="downloadedValue">{downloaded}</span>
                </div>
                
                <!-- Uploaded -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Uploaded</span>
                    <span class="detail-value text-xs sm:text-sm font-mono text-purple-300 font-semibold font-english" id="uploadedValue">{uploaded}</span>
                </div>
                
                <!-- Usage -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Usage</span>
                    <span class="detail-value text-xs sm:text-sm font-mono text-amber-300 font-semibold font-english" id="usageValue">{usage} / {total_quota}</span>
                </div>
                
                <!-- Total Quota -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Total Quota</span>
                    <span class="detail-value text-xs sm:text-sm font-mono text-slate-200 font-semibold font-english" id="totalQuotaValue">{total_quota}</span>
                </div>
                
                <!-- Remained -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Remained</span>
                    <span class="detail-value text-xs sm:text-sm font-mono text-emerald-300 font-semibold font-english" id="remainedValue">{remained}</span>
                </div>
                
                <!-- Last Online -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Last Online</span>
                    <span class="detail-value text-xs sm:text-sm font-mono text-slate-300 font-english" id="lastOnlineValue">{last_online}</span>
                </div>
                
                <!-- Expiry -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">Expiry</span>
                    <span class="detail-value text-xs sm:text-sm font-mono text-rose-300 font-semibold font-english" id="expiryValue">{expiry}</span>
                </div>
                
                <!-- IPs Connected -->
                <div class="detail-row flex flex-col sm:flex-row sm:justify-between sm:items-center border-b border-slate-800/60 py-2 px-1 rounded-lg gap-1 sm:gap-0">
                    <span class="detail-label text-[10px] sm:text-xs text-slate-400 font-medium uppercase tracking-wider font-english">IP(s) Connected</span>
                    <span class="detail-value text-xs sm:text-sm font-mono text-cyan-300 font-english" id="ipsValue">{ips}</span>
                </div>
            </div>

            <!-- Progress Bar Section -->
            <div class="mt-5 sm:mt-6 p-4 sm:p-5 bg-slate-950/60 border border-slate-800/60 rounded-xl">
                <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-1 sm:gap-0 mb-2">
                    <span class="text-xs sm:text-sm text-slate-300 font-medium truncate font-mixed" id="progressLabel">{label}</span>
                    <span class="text-[10px] sm:text-xs text-slate-400 font-mono font-english" id="progressText">{used_fmt} / {limit_fmt}</span>
                </div>
                <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                    <div class="h-full bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full progress-bar-fill" id="progressBar" style="width: {usage_pct}%;"></div>
                </div>
                <div class="flex flex-col xs:flex-row xs:justify-between gap-0.5 xs:gap-0 mt-1.5">
                    <span class="text-[10px] sm:text-xs text-slate-500 font-english" id="usagePercent">{usage_pct}% used</span>
                    <span class="text-[10px] sm:text-xs text-slate-500 font-english" id="remainedText">{remained} remaining</span>
                </div>
            </div>

            <!-- VLESS Link -->
            <div class="mt-5 sm:mt-6 p-3 sm:p-4 bg-slate-950/60 border border-slate-800/60 rounded-xl">
                <p class="text-[10px] sm:text-xs text-slate-400 mb-2 flex items-center gap-2 font-english">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 sm:w-4 sm:h-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
                        <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
                    </svg>
                    <span class="truncate font-english">VLESS Link (copy to client):</span>
                </p>
                <div class="flex items-center gap-2 mobile-stack">
                    <input type="text" readonly value="{vless_link}" id="vless-link-input" class="flex-1 min-w-0 bg-slate-950 border border-slate-800/80 rounded-xl px-2 sm:px-3 py-1.5 sm:py-2 text-[8px] sm:text-[10px] font-mono text-slate-400 focus:outline-none select-all truncate input-focus-ring font-english">
                    <button onclick="copyToClipboard('{vless_link}')" class="copy-btn px-3 sm:px-4 py-1.5 sm:py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl transition shadow-lg shadow-blue-600/20 flex items-center justify-center gap-1.5 shrink-0 font-english">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"/>
                            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>
                        </svg>
                        <span class="hidden xs:inline text-[10px] sm:text-xs font-english">Copy</span>
                    </button>
                </div>
            </div>

            <!-- Auto-Update Status Footer with Timer -->
            <div class="mt-4 flex flex-col sm:flex-row items-center justify-between gap-2 text-[9px] sm:text-[10px] text-slate-500 border-t border-slate-800/60 pt-3">
                <span class="font-english">Last updated: <span id="lastUpdateTime" class="font-english">just now</span></span>
                <div class="flex items-center gap-3">
                    <span class="font-english">Next update in: <span id="timerDisplay" class="font-mono text-blue-400 font-english">30</span>s</span>
                    <button onclick="manualUpdate()" class="text-blue-400 hover:text-blue-300 transition-colors px-2 py-0.5 rounded border border-blue-500/20 hover:border-blue-500/40 text-[9px] font-english">
                        ↻ Refresh
                    </button>
                </div>
            </div>

            <!-- Footer -->
            <div class="mt-2 text-center text-[10px] sm:text-xs text-slate-500 font-english">
                {watermark}
            </div>
        </div>
    </div>

    <script>
        // Store current UUID for updates
        const CURRENT_UUID = '{uuid}';
        let updateInterval = null;
        let timerInterval = null;
        let isUpdating = false;
        let countdown = 30;
        let isPaused = false;
        let isFirstLoad = true;
        let lastUpdateTime = Date.now();
        let timerStartTime = Date.now();
        let timerLastTick = Date.now();
        let accumulatedTime = 0;

        // Toast notification system
        function showToast(message, type) {{
            const toast = document.getElementById('toast');
            toast.textContent = message;
            toast.className = 'toast show' + (type ? ' ' + type : '');
            clearTimeout(toast._timeout);
            toast._timeout = setTimeout(() => {{
                toast.classList.remove('show');
            }}, 3000);
        }}

        // Copy to clipboard with fallback
        function copyToClipboard(text) {{
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText(text).then(() => {{
                    showToast('Copied to clipboard!', 'success');
                }}).catch(() => {{
                    fallbackCopy(text);
                }});
            }} else {{
                fallbackCopy(text);
            }}
        }}

        function fallbackCopy(text) {{
            const textarea = document.createElement('textarea');
            textarea.value = text;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            textarea.style.left = '-9999px';
            textarea.style.top = '-9999px';
            document.body.appendChild(textarea);
            textarea.select();
            try {{
                document.execCommand('copy');
                showToast('Copied to clipboard!', 'success');
            }} catch (e) {{
                showToast('Failed to copy', 'error');
            }}
            document.body.removeChild(textarea);
        }}

        // Format bytes
        function fmtBytes(b) {{
            if (b === 0) return '0 B';
            if (b < 1024) return b + ' B';
            if (b < 1024 ** 2) return (b / 1024).toFixed(1) + ' KB';
            if (b < 1024 ** 3) return (b / 1024 ** 2).toFixed(2) + ' MB';
            return (b / 1024 ** 3).toFixed(2) + ' GB';
        }}

        // Update timer display with rounded integer
        function updateTimer() {{
            const timerDisplay = document.getElementById('timerDisplay');
            const timerRing = document.getElementById('timerRing');
            
            // Round to nearest integer for display
            const displayCountdown = Math.round(countdown);
            
            if (timerDisplay) {{
                timerDisplay.textContent = displayCountdown;
            }}
            
            if (timerRing) {{
                timerRing.textContent = displayCountdown;
                timerRing.classList.remove('warning', 'critical');
                if (displayCountdown <= 5) {{
                    timerRing.classList.add('critical');
                }} else if (displayCountdown <= 10) {{
                    timerRing.classList.add('warning');
                }}
            }}
        }}

        // Manual update trigger
        function manualUpdate() {{
            // Reset countdown to exactly 30
            countdown = 30;
            timerStartTime = Date.now();
            timerLastTick = Date.now();
            accumulatedTime = 0;
            updateTimer();
            // Force update
            updateSubscriptionData();
            showToast('Refreshing...', 'info');
        }}

        // Update ONLY the data (not the whole page)
        async function updateSubscriptionData() {{
            if (isUpdating) return;
            isUpdating = true;

            const indicator = document.getElementById('updateIndicator');
            const spinner = document.getElementById('updateSpinner');
            const text = document.getElementById('updateText');
            const qrImage = document.getElementById('qrImage');

            // Show updating state
            indicator.classList.add('updating');
            spinner.style.display = 'inline-block';
            text.textContent = 'Updating...';
            if (qrImage) qrImage.classList.add('loading');

            try {{
                // Fetch ONLY the data from API
                const response = await fetch('/api/link-status/' + CURRENT_UUID + '?_t=' + Date.now());
                
                if (!response.ok) {{
                    throw new Error('Failed to fetch updates');
                }}

                const data = await response.json();
                
                // Update ONLY the data fields
                const usedBytes = data.used_bytes || 0;
                const limitBytes = data.limit_bytes || 0;
                const usagePercent = data.usage_percent || 0;
                const isActive = data.active || false;

                // Format values
                const usedFormatted = fmtBytes(usedBytes);
                const limitFormatted = limitBytes === 0 ? '∞' : fmtBytes(limitBytes);
                const remainedFormatted = limitBytes === 0 ? '∞' : fmtBytes(Math.max(0, limitBytes - usedBytes));

                // Update Downloaded
                const downloadedEl = document.getElementById('downloadedValue');
                if (downloadedEl) downloadedEl.textContent = usedFormatted;

                // Update Usage
                const usageEl = document.getElementById('usageValue');
                if (usageEl) usageEl.textContent = usedFormatted + ' / ' + limitFormatted;

                // Update Remained
                const remainedEl = document.getElementById('remainedValue');
                if (remainedEl) remainedEl.textContent = remainedFormatted;

                // Update Progress Bar
                const progressBar = document.getElementById('progressBar');
                if (progressBar) progressBar.style.width = usagePercent + '%';

                // Update Progress Text
                const progressText = document.getElementById('progressText');
                if (progressText) progressText.textContent = usedFormatted + ' / ' + limitFormatted;

                // Update Usage Percent
                const usagePercentEl = document.getElementById('usagePercent');
                if (usagePercentEl) usagePercentEl.textContent = usagePercent.toFixed(1) + '% used';

                // Update Remained Text
                const remainedText = document.getElementById('remainedText');
                if (remainedText) remainedText.textContent = remainedFormatted + ' remaining';

                // Update Status Badge
                const statusBadge = document.getElementById('status-badge');
                const statusValue = document.getElementById('statusValue');
                if (statusBadge && statusValue) {{
                    if (isActive) {{
                        statusBadge.className = 'status-badge active';
                        statusBadge.innerHTML = '<span class="status-dot active"></span> Active';
                        statusValue.textContent = 'Active';
                        statusValue.className = 'detail-value text-xs sm:text-sm font-mono text-emerald-400 font-semibold font-english';
                    }} else {{
                        statusBadge.className = 'status-badge inactive';
                        statusBadge.innerHTML = '<span class="status-dot inactive"></span> Inactive';
                        statusValue.textContent = 'Inactive';
                        statusValue.className = 'detail-value text-xs sm:text-sm font-mono text-red-400 font-semibold font-english';
                    }}
                }}

                // Update last update time
                lastUpdateTime = Date.now();
                document.getElementById('lastUpdateTime').textContent = new Date().toLocaleTimeString();

                // Reset countdown to exactly 30 after successful update
                countdown = 30;
                timerStartTime = Date.now();
                timerLastTick = Date.now();
                accumulatedTime = 0;
                updateTimer();

            }} catch (error) {{
                console.error('Update error:', error);
                if (!isFirstLoad) {{
                    showToast('Update failed: ' + error.message, 'error');
                }}
            }} finally {{
                isUpdating = false;
                isFirstLoad = false;
                indicator.classList.remove('updating');
                spinner.style.display = 'none';
                text.textContent = 'Auto';
                if (qrImage) qrImage.classList.remove('loading');
            }}
        }}

        // Timer countdown function - Uses REAL time with proper rounding
        function startTimer() {{
            if (timerInterval) clearInterval(timerInterval);
            
            timerStartTime = Date.now();
            timerLastTick = Date.now();
            accumulatedTime = 0;
            
            timerInterval = setInterval(() => {{
                if (isPaused) return;
                
                // Calculate elapsed time since last tick
                const now = Date.now();
                const elapsedSeconds = (now - timerLastTick) / 1000;
                timerLastTick = now;
                
                // Decrease countdown by elapsed seconds
                countdown = Math.max(0, countdown - elapsedSeconds);
                
                // If countdown reached 0 or below, trigger update
                if (countdown <= 0) {{
                    countdown = 30;
                    timerStartTime = Date.now();
                    timerLastTick = Date.now();
                    accumulatedTime = 0;
                    updateTimer();
                    updateSubscriptionData();
                }} else {{
                    updateTimer();
                }}
            }}, 100); // Check every 100ms for accuracy
        }}

        // Start auto-update
        function startAutoUpdate() {{
            isPaused = false;
            timerLastTick = Date.now();
            startTimer();
        }}

        // Stop auto-update
        function stopAutoUpdate() {{
            isPaused = true;
            if (timerInterval) {{
                clearInterval(timerInterval);
                timerInterval = null;
            }}
        }}

        // Resume auto-update - Continue from where we left off
        function resumeAutoUpdate() {{
            isPaused = false;
            timerLastTick = Date.now();
            startTimer();
        }}

        // Auto-select input on click
        document.addEventListener('DOMContentLoaded', function() {{
            const input = document.getElementById('vless-link-input');
            if (input) {{
                input.addEventListener('click', function() {{
                    this.select();
                }});
                input.addEventListener('focus', function() {{
                    this.select();
                }});
            }}

            // Set initial status badge
            const statusBadge = document.getElementById('status-badge');
            const statusValue = document.getElementById('statusValue');
            if (statusValue) {{
                const isActive = statusValue.textContent.trim().toLowerCase().includes('active');
                if (isActive) {{
                    statusBadge.className = 'status-badge active';
                    statusBadge.innerHTML = '<span class="status-dot active"></span> Active';
                }} else {{
                    statusBadge.className = 'status-badge inactive';
                    statusBadge.innerHTML = '<span class="status-dot inactive"></span> Inactive';
                }}
            }}

            // Start auto-update
            startAutoUpdate();
        }});

        // Keyboard shortcuts
        document.addEventListener('keydown', function(e) {{
            // Ctrl+U or Cmd+U to manually update
            if ((e.ctrlKey || e.metaKey) && e.key === 'u') {{
                e.preventDefault();
                manualUpdate();
            }}
            // Ctrl+C or Cmd+C to copy VLESS link
            if ((e.ctrlKey || e.metaKey) && e.key === 'c') {{
                const input = document.getElementById('vless-link-input');
                if (document.activeElement === input) {{
                    copyToClipboard(input.value);
                }}
            }}
            // Space to pause/resume
            if (e.key === ' ' && !e.target.matches('input, textarea, button')) {{
                e.preventDefault();
                if (isPaused) {{
                    resumeAutoUpdate();
                    showToast('Auto-update resumed', 'info');
                }} else {{
                    stopAutoUpdate();
                    showToast('Auto-update paused', 'info');
                }}
            }}
        }});

        // Handle page visibility change - Timer CONTINUES in background
        // When tab is hidden, we just pause UI updates but timer continues
        let hiddenStartTime = 0;
        let hiddenElapsed = 0;

        document.addEventListener('visibilitychange', function() {{
            if (document.hidden) {{
                // Tab is hidden - mark time and pause UI updates
                hiddenStartTime = Date.now();
                isPaused = true;
            }} else {{
                // Tab is visible again - resume UI updates
                // Calculate how long we were hidden
                const hiddenDuration = (Date.now() - hiddenStartTime) / 1000;
                
                // Apply the hidden time to countdown (timer continued in background)
                countdown = Math.max(0, countdown - hiddenDuration);
                
                // If countdown reached 0 or below while hidden, trigger update now
                if (countdown <= 0) {{
                    countdown = 30;
                    timerStartTime = Date.now();
                    timerLastTick = Date.now();
                    accumulatedTime = 0;
                    updateTimer();
                    updateSubscriptionData();
                }} else {{
                    updateTimer();
                }}
                
                // Resume timer
                isPaused = false;
                timerLastTick = Date.now();
                startTimer();
            }}
        }});

        // Clean up on page unload
        window.addEventListener('beforeunload', function() {{
            if (timerInterval) clearInterval(timerInterval);
        }});

        // Touch feedback for copy button
        document.querySelector('.copy-btn')?.addEventListener('touchstart', function() {{
            this.style.transform = 'scale(0.95)';
        }}, {{ passive: true }});
        
        document.querySelector('.copy-btn')?.addEventListener('touchend', function() {{
            this.style.transform = 'scale(1)';
        }}, {{ passive: true }});
    </script>
</body>
</html>"""

# ---------- SETUP_HTML (Setup Page - No Loader) ----------
SETUP_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Setup · MX-UI</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Vazirmatn:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        persian: ['Vazirmatn', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #070a13;
        }
        .glow-effect {
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.12);
        }
        .input-focus-ring:focus {
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
        }
        .font-persian {
            font-family: 'Vazirmatn', sans-serif;
        }
        .font-english {
            font-family: 'Inter', sans-serif;
        }
        .font-mixed {
            font-family: 'Inter', sans-serif;
        }
        @media (max-width: 640px) {
            .mobile-padding {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
        .strength-bar {
            height: 3px;
            border-radius: 2px;
            transition: all 0.3s ease;
        }
        .strength-bar.weak {
            background: #ef4444;
            width: 25%;
        }
        .strength-bar.medium {
            background: #f59e0b;
            width: 50%;
        }
        .strength-bar.strong {
            background: #22c55e;
            width: 75%;
        }
        .strength-bar.very-strong {
            background: #22c55e;
            width: 100%;
        }
        .strength-text {
            font-size: 10px;
            transition: all 0.3s ease;
        }
        .strength-text.weak { color: #ef4444; }
        .strength-text.medium { color: #f59e0b; }
        .strength-text.strong { color: #22c55e; }
        .strength-text.very-strong { color: #22c55e; }
        .btn-transition {
            transition: all 0.2s ease;
        }
        .btn-transition:active {
            transform: scale(0.97);
        }
    </style>
</head>
<body class="font-sans text-slate-200 min-h-screen flex items-center justify-center bg-[#070a13] relative antialiased tracking-tight p-4 mobile-padding">
    
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_0%,rgba(59,130,246,0.08),transparent_70%)] pointer-events-none"></div>
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_60%_40%_at_50%_100%,rgba(99,102,241,0.05),transparent_70%)] pointer-events-none"></div>
    <div class="absolute inset-0 opacity-[0.03] pointer-events-none" style="background-image: radial-gradient(circle at 1px 1px, #3b82f6 1px, transparent 0); background-size: 24px 24px;"></div>
    
    <div class="w-full max-w-md relative z-10">
        <div class="bg-slate-900/80 border border-slate-800/80 rounded-2xl p-6 sm:p-8 backdrop-blur-xl glow-effect transition-all duration-300 hover:border-slate-700/80">
            
            <!-- Logo & Brand -->
            <div class="flex items-center gap-3 mb-6">
                <div class="bg-blue-600 p-2 rounded-xl text-white glow-effect flex-shrink-0">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                        <polyline points="9 12 11 14 15 10"/>
                    </svg>
                </div>
                <div class="flex-1 min-w-0">
                    <span class="font-bold text-lg tracking-wide bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent block truncate font-english">MX-UI PANEL</span>
                    <span class="text-xs text-slate-500 font-medium font-english">v1.0.0 • Setup</span>
                </div>
            </div>
            
            <!-- Title -->
            <h1 class="text-xl font-bold text-slate-100 mb-1 font-english">Welcome! 👋</h1>
            <p class="text-sm text-slate-400 mb-6 font-english">Set your admin password to secure the panel</p>
            
            <!-- Default Password Suggestion -->
            <div class="bg-blue-500/10 border border-blue-500/20 rounded-xl p-4 mb-5">
                <div class="flex items-start gap-3">
                    <div class="bg-blue-500/20 p-1.5 rounded-lg flex-shrink-0 mt-0.5">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                            <polyline points="9 12 11 14 15 10"/>
                        </svg>
                    </div>
                    <div>
                        <p class="text-xs text-slate-300 font-english">Default password is <span class="font-mono font-bold text-blue-400 bg-blue-500/20 px-2 py-0.5 rounded font-english">MUVIXO</span></p>
                        <p class="text-[10px] text-slate-400 mt-1 font-english">You can use it or set your own custom password below</p>
                    </div>
                </div>
            </div>
            
            <!-- Setup Form -->
            <form id="setupForm">
                <div class="mb-3">
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2 font-english">New Password</label>
                    <input type="password" id="new-pw" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition input-focus-ring font-english" placeholder="Enter your password (min 4 chars)" autofocus required minlength="4">
                </div>
                <div class="mb-1">
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2 font-english">Confirm Password</label>
                    <input type="password" id="confirm-pw" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition input-focus-ring font-english" placeholder="Confirm your password" required minlength="4">
                </div>
                
                <!-- Password Strength Indicator -->
                <div class="mt-3 mb-4">
                    <div class="flex items-center justify-between gap-2">
                        <div class="flex-1 h-1 bg-slate-800 rounded-full overflow-hidden">
                            <div class="strength-bar" id="strengthBar"></div>
                        </div>
                        <span class="strength-text font-english" id="strengthText">—</span>
                    </div>
                </div>
                
                <div class="flex gap-3 mb-4">
                    <button type="button" onclick="useDefaultPassword()" class="flex-1 py-2.5 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 text-sm font-medium rounded-xl transition-all duration-300 btn-transition font-english">
                        Use Default
                    </button>
                    <button type="submit" id="setupButton" class="flex-1 py-2.5 bg-blue-600 hover:bg-blue-500 text-white text-sm font-medium rounded-xl transition-all duration-300 shadow-lg shadow-blue-600/10 hover:shadow-blue-600/25 flex items-center justify-center gap-2 btn-transition font-english">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/>
                            <polyline points="10 17 15 12 10 7"/>
                            <line x1="15" y1="12" x2="3" y2="12"/>
                        </svg>
                        Set Password
                    </button>
                </div>
                
                <div id="errorMsg" class="text-sm text-red-400 hidden font-english"></div>
                <div id="successMsg" class="text-sm text-emerald-400 hidden font-english"></div>
            </form>
            
            <!-- Footer -->
            <div class="mt-6 pt-4 border-t border-slate-800/60 text-center text-xs text-slate-500 font-english">
                Created by Muvixo
            </div>
        </div>
    </div>

    <script>
        // Password strength checker
        function checkPasswordStrength(password) {
            let score = 0;
            if (password.length >= 4) score++;
            if (password.length >= 8) score++;
            if (/[a-z]/.test(password) && /[A-Z]/.test(password)) score++;
            if (/\d/.test(password)) score++;
            if (/[^a-zA-Z0-9]/.test(password)) score++;
            return score;
        }

        function updateStrengthIndicator(password) {
            const bar = document.getElementById('strengthBar');
            const text = document.getElementById('strengthText');
            
            if (password.length === 0) {
                bar.className = 'strength-bar';
                text.textContent = '—';
                text.className = 'strength-text font-english';
                return;
            }
            
            const score = checkPasswordStrength(password);
            
            bar.className = 'strength-bar';
            text.className = 'strength-text font-english';
            
            if (score <= 1) {
                bar.classList.add('weak');
                text.classList.add('weak');
                text.textContent = 'Weak';
            } else if (score === 2) {
                bar.classList.add('medium');
                text.classList.add('medium');
                text.textContent = 'Medium';
            } else if (score === 3) {
                bar.classList.add('strong');
                text.classList.add('strong');
                text.textContent = 'Strong';
            } else {
                bar.classList.add('very-strong');
                text.classList.add('very-strong');
                text.textContent = 'Very Strong';
            }
        }

        document.getElementById('new-pw').addEventListener('input', function() {
            updateStrengthIndicator(this.value);
        });

        function useDefaultPassword() {
            document.getElementById('new-pw').value = 'MUVIXO';
            document.getElementById('confirm-pw').value = 'MUVIXO';
            updateStrengthIndicator('MUVIXO');
            document.getElementById('setupForm').dispatchEvent(new Event('submit'));
        }

        document.getElementById('setupForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const btn = document.getElementById('setupButton');
            const err = document.getElementById('errorMsg');
            const success = document.getElementById('successMsg');
            
            err.classList.add('hidden');
            success.classList.add('hidden');
            btn.disabled = true;
            
            const originalText = btn.innerHTML;
            btn.innerHTML = 'Setting...';
            
            const password = document.getElementById('new-pw').value;
            const confirm = document.getElementById('confirm-pw').value;
            
            if (password.length < 4) {
                err.textContent = 'Password must be at least 4 characters';
                err.classList.remove('hidden');
                btn.disabled = false;
                btn.innerHTML = originalText;
                return;
            }
            
            if (password !== confirm) {
                err.textContent = 'Passwords do not match';
                err.classList.remove('hidden');
                btn.disabled = false;
                btn.innerHTML = originalText;
                return;
            }
            
            try {
                const res = await fetch('/api/setup', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ password: password })
                });
                
                if (!res.ok) {
                    const data = await res.json();
                    throw new Error(data.detail || 'Setup failed');
                }
                
                success.textContent = '✅ Password set successfully! Redirecting...';
                success.classList.remove('hidden');
                
                btn.innerHTML = '✅ Done!';
                
                setTimeout(() => {
                    location.href = '/login';
                }, 1500);
                
            } catch (e) {
                err.textContent = e.message || 'Setup failed. Please try again.';
                err.classList.remove('hidden');
                btn.disabled = false;
                btn.innerHTML = originalText;
            }
        });

        document.getElementById('new-pw').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                document.getElementById('confirm-pw').focus();
            }
        });
        
        document.getElementById('confirm-pw').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                document.getElementById('setupForm').dispatchEvent(new Event('submit'));
            }
        });

        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(() => {
                document.getElementById('new-pw').focus();
            }, 300);
        });
    </script>
</body>
</html>"""
# Helper function for SUB_INFO_HTML's status display
def _status_display(active):
    return 'Active' if active else 'Inactive'