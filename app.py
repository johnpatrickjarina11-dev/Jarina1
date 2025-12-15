import streamlit as st
import streamlit.components.v1 as components

# 1. Configure the Streamlit Page settings
st.set_page_config(
    page_title="Purrfect Fit | BMI Companion",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Add custom CSS to remove Streamlit's default padding and UI elements
# This makes the app look full-screen and cleaner.
st.markdown("""
    <style>
        /* Remove default padding from the main block */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        /* Hide the Streamlit hamburger menu and footer */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header { visibility: hidden; }
        
        /* Ensure the iframe container fills the width */
        iframe {
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

# 3. Your Complete HTML/CSS/JS Code
# I have embedded it exactly as provided.
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>Purrfect Fit | BMI Companion</title>
    <!-- Font Awesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
    
    <style>
        /* --- CSS VARIABLES & THEME --- */
        :root {
            --primary: #FF8FA3;
            --primary-dark: #FF6B8B;
            --secondary: #A09BE7;
            --bg-body: #E0E5EC;
            --bg-card: #E0E5EC;
            --text-main: #4A4A4A;
            --text-light: #9CA3AF;
            --shadow-light: #ffffff;
            --shadow-dark: #a3b1c6;
            --glass: rgba(255, 255, 255, 0.25);
            --radius-xl: 30px;
            --radius-md: 15px;
            --danger: #ff6b6b;
        }

        * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }

        body {
            font-family: 'Nunito', sans-serif;
            background-color: #2d3436; /* Dark background for desktop contrast */
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: hidden; /* Prevent double scrollbars */
        }

        /* --- MOBILE SIMULATION CONTAINER --- */
        .app-shell {
            width: 375px;
            height: 812px; /* iPhone X height standard */
            background-color: var(--bg-body);
            position: relative;
            overflow: hidden;
            border-radius: 45px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            border: 8px solid #1a1a1a;
        }

        @media (max-width: 480px) {
            body { background-color: var(--bg-body); }
            /* On actual mobile, fill the screen */
            .app-shell { width: 100vw; height: 100vh; border: none; border-radius: 0; box-shadow: none; }
        }

        /* --- NEUMORPHIC UTILITIES --- */
        .neu-flat {
            background: var(--bg-card);
            box-shadow: 9px 9px 16px var(--shadow-dark), -9px -9px 16px var(--shadow-light);
            border-radius: var(--radius-md);
            border: 1px solid rgba(255,255,255,0.2);
        }

        .neu-pressed {
            background: var(--bg-card);
            box-shadow: inset 6px 6px 10px var(--shadow-dark), inset -6px -6px 10px var(--shadow-light);
            border-radius: var(--radius-md);
        }

        .neu-btn {
            background: linear-gradient(145deg, var(--primary), var(--primary-dark));
            color: white;
            box-shadow: 5px 5px 15px rgba(255, 107, 139, 0.4);
            transition: transform 0.1s ease;
        }
        .neu-btn:active { transform: scale(0.96); }

        /* Danger Button Variant */
        .btn-danger {
            background: var(--bg-card);
            color: var(--danger);
            border: 1px solid var(--danger);
            box-shadow: 5px 5px 10px var(--shadow-dark), -5px -5px 10px var(--shadow-light);
        }
        .btn-danger:active {
            background: var(--danger);
            color: white;
        }

        /* --- SCREEN MANAGEMENT --- */
        .screen {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            display: flex; flex-direction: column;
            padding: 30px 24px;
            background: var(--bg-body);
            opacity: 0; pointer-events: none;
            transition: opacity 0.4s ease, transform 0.4s ease;
            transform: scale(0.95);
            overflow-y: auto;
            /* Hide scrollbar for cleaner look */
            -ms-overflow-style: none; 
            scrollbar-width: none;  
        }
        .screen::-webkit-scrollbar { display: none; }
        
        .screen.active {
            opacity: 1; pointer-events: all;
            transform: scale(1);
            z-index: 10;
        }

        /* --- TYPOGRAPHY & ELEMENTS --- */
        h1, h2, h3 { color: var(--text-main); margin: 0; font-family: 'Quicksand', sans-serif; }
        p { color: var(--text-light); font-size: 0.9rem; }
        
        .cat-mascot {
            width: 140px; height: 140px;
            background-image: url('https://cdn-icons-png.flaticon.com/512/616/616430.png'); 
            background-size: cover;
            margin: 0 auto 20px;
            filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1));
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }

        /* INPUTS */
        .input-group { position: relative; margin-bottom: 20px; }
        .input-field {
            width: 100%; padding: 16px;
            border: none; outline: none;
            color: var(--text-main);
            font-weight: 600;
        }
        .input-group i {
            position: absolute; right: 15px; top: 50%; transform: translateY(-50%);
            color: var(--primary);
        }

        /* BUTTONS */
        .btn-main {
            width: 100%; padding: 18px;
            border-radius: var(--radius-xl);
            border: none; font-size: 1rem; font-weight: 800;
            letter-spacing: 0.5px; cursor: pointer;
            margin-top: auto;
        }

        /* DASHBOARD */
        .dash-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
        .user-avatar { width: 50px; height: 50px; border-radius: 50%; border: 2px solid white; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
        
        .action-card {
            display: flex; justify-content: space-between; align-items: center;
            padding: 25px; margin-bottom: 20px;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        .action-card::after {
            content: ''; position: absolute; top:0; left:0; width: 5px; height: 100%;
            background: var(--primary);
        }

        /* CALCULATOR UI */
        .controls-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }
        
        .gender-option {
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            padding: 20px; cursor: pointer; transition: all 0.3s;
            color: var(--text-light);
        }
        .gender-option.active {
            color: var(--primary);
            box-shadow: inset 4px 4px 8px var(--shadow-dark), inset -4px -4px 8px var(--shadow-light);
            border: 1px solid var(--bg-body);
        }

        .range-wrapper { padding: 25px; text-align: center; margin-bottom: 20px; }
        input[type=range] {
            width: 100%; -webkit-appearance: none; background: transparent; margin-top: 15px;
        }
        input[type=range]::-webkit-slider-thumb {
            -webkit-appearance: none; height: 24px; width: 24px;
            border-radius: 50%; background: var(--primary);
            cursor: pointer; margin-top: -10px;
            box-shadow: 0 0 10px rgba(255, 143, 163, 0.5);
        }
        input[type=range]::-webkit-slider-runnable-track {
            width: 100%; height: 6px; cursor: pointer;
            background: #d1d9e6; border-radius: 10px;
        }

        .counter-box { text-align: center; padding: 15px; }
        .counter-controls { display: flex; justify-content: center; align-items: center; gap: 15px; margin-top: 10px; }
        .round-btn {
            width: 35px; height: 35px; border-radius: 50%; border: none;
            background: var(--bg-body); color: var(--text-main); font-weight: bold;
            box-shadow: 5px 5px 10px var(--shadow-dark), -5px -5px 10px var(--shadow-light);
            cursor: pointer;
        }
        .round-btn:active { box-shadow: inset 3px 3px 5px var(--shadow-dark), inset -3px -3px 5px var(--shadow-light); }

        /* RESULTS & SVG GAUGE */
        .gauge-container {
            width: 250px; height: 250px; margin: 0 auto 30px;
            position: relative;
        }
        .gauge-svg { width: 100%; height: 100%; transform: rotate(-90deg); }
        .gauge-bg { fill: none; stroke: #eee; stroke-width: 15; }
        .gauge-progress {
            fill: none; stroke: var(--primary); stroke-width: 15; stroke-linecap: round;
            stroke-dasharray: 630; stroke-dashoffset: 630;
            transition: stroke-dashoffset 1.5s ease-out, stroke 0.5s;
        }
        .gauge-center {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            text-align: center;
        }

        /* SETTINGS LIST */
        .settings-item {
            display: flex; justify-content: space-between; align-items: center;
            padding: 20px; margin-bottom: 15px;
        }
        .settings-label { display: flex; align-items: center; gap: 15px; font-weight: 600; color: var(--text-main); }
        .settings-icon { width: 30px; text-align: center; color: var(--primary); }
        
        /* BOTTOM NAV */
        .nav-bar {
            position: absolute; bottom: 30px; left: 24px; right: 24px;
            height: 70px; display: flex; justify-content: space-around; align-items: center;
            z-index: 20;
        }
        .nav-item { font-size: 1.2rem; color: var(--text-light); transition: color 0.3s; cursor: pointer; }
        .nav-item.active { color: var(--primary); transform: scale(1.1); }

    </style>
</head>
<body>

    <div class="app-shell">
        
        <!-- 1. SPLASH / WELCOME SCREEN -->
        <div id="screen-welcome" class="screen active" style="justify-content: center; text-align: center;">
            <div class="cat-mascot"></div>
            <h1 style="font-size: 2rem; margin-bottom: 10px;">Purrfect Fit</h1>
            <p style="margin-bottom: 40px;">Stay healthy, for you and your furry friend.</p>
            <button class="neu-btn btn-main" onclick="Router.to('screen-auth')">Get Started</button>
        </div>

        <!-- 2. AUTH SCREEN -->
        <div id="screen-auth" class="screen">
            <h2 style="margin-top: 40px;">Who are you?</h2>
            <p style="margin-bottom: 40px;">Create a profile to track your progress.</p>
            
            <div class="input-group neu-pressed">
                <input type="text" id="input-name" class="input-field" style="background:transparent;" placeholder="Your Name">
                <i class="fas fa-user"></i>
            </div>
            
            <div class="input-group neu-pressed">
                <input type="email" class="input-field" style="background:transparent;" placeholder="Email (Optional)">
                <i class="fas fa-envelope"></i>
            </div>

            <button class="neu-btn btn-main" onclick="Auth.signUp()">Enter App</button>
            <p style="text-align: center; margin-top: 20px; font-size: 0.8rem;">By entering, you agree to our <span style="color:var(--primary)">Terms</span></p>
        </div>

        <!-- 3. DASHBOARD -->
        <div id="screen-dashboard" class="screen">
            <div class="dash-header">
                <div>
                    <p style="font-weight:700; font-size: 0.8rem; letter-spacing: 1px;">WELCOME BACK</p>
                    <h2 id="display-username">Human</h2>
                </div>
                <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix" class="user-avatar" alt="Avatar">
            </div>

            <!-- Last Result Card -->
            <div id="last-result-card" class="neu-flat action-card" style="display:none; background: #fff0f3;">
                <div>
                    <p style="color: var(--primary-dark); font-weight: bold;">Last BMI</p>
                    <h2 id="dash-last-bmi" style="color: var(--primary);">22.5</h2>
                </div>
                <i class="fas fa-history" style="font-size: 1.5rem; color: var(--primary-dark); opacity: 0.5;"></i>
            </div>

            <!-- Main Calculator Entry -->
            <div class="neu-flat action-card" onclick="Router.to('screen-calc')">
                <div>
                    <h3>BMI Calculator</h3>
                    <p>Check your body stats now</p>
                </div>
                <div style="width: 40px; height: 40px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white;">
                    <i class="fas fa-arrow-right"></i>
                </div>
            </div>

            <!-- Cat Fact Card -->
            <div class="neu-flat action-card" style="flex-direction: column; align-items: flex-start;">
                <h3 style="margin-bottom: 10px; font-size: 1rem;"><i class="fas fa-paw" style="color: var(--secondary)"></i> Daily Cat Fact</h3>
                <p id="cat-fact-text" style="font-style: italic;">"Cats spend 70% of their lives sleeping."</p>
            </div>
        </div>

        <!-- 4. CALCULATOR -->
        <div id="screen-calc" class="screen">
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                <i class="fas fa-arrow-left" style="font-size: 1.2rem; cursor: pointer; padding: 10px;" onclick="Router.to('screen-dashboard')"></i>
                <h3 style="margin-left: 10px;">Calculator</h3>
            </div>

            <!-- Gender -->
            <div class="controls-grid">
                <div class="neu-flat gender-option active" id="btn-male" onclick="Calculator.setGender('male')">
                    <i class="fas fa-mars" style="font-size: 1.8rem; margin-bottom: 8px;"></i>
                    <span>Male</span>
                </div>
                <div class="neu-flat gender-option" id="btn-female" onclick="Calculator.setGender('female')">
                    <i class="fas fa-venus" style="font-size: 1.8rem; margin-bottom: 8px;"></i>
                    <span>Female</span>
                </div>
            </div>

            <!-- Height -->
            <div class="neu-flat range-wrapper">
                <p style="font-weight: 700;">HEIGHT (CM)</p>
                <h2 id="height-val" style="color: var(--primary); font-size: 2rem;">170</h2>
                <input type="range" min="100" max="250" value="170" oninput="Calculator.updateHeight(this.value)">
            </div>

            <!-- Weight & Age -->
            <div class="controls-grid">
                <div class="neu-flat counter-box">
                    <p style="font-weight: 700;">WEIGHT</p>
                    <h2 id="weight-val">65</h2>
                    <div class="counter-controls">
                        <button class="round-btn" onclick="Calculator.updateWeight(-1)">-</button>
                        <button class="round-btn" onclick="Calculator.updateWeight(1)">+</button>
                    </div>
                </div>
                <div class="neu-flat counter-box">
                    <p style="font-weight: 700;">AGE</p>
                    <h2 id="age-val">25</h2>
                    <div class="counter-controls">
                        <button class="round-btn" onclick="Calculator.updateAge(-1)">-</button>
                        <button class="round-btn" onclick="Calculator.updateAge(1)">+</button>
                    </div>
                </div>
            </div>

            <button class="neu-btn btn-main" onclick="Calculator.calculate()">Calculate</button>
        </div>

        <!-- 5. RESULTS -->
        <div id="screen-result" class="screen" style="text-align: center;">
            <h3 style="margin-bottom: 30px; margin-top: 20px;">Your Result</h3>

            <div class="gauge-container">
                <svg class="gauge-svg" viewBox="0 0 220 220">
                    <circle class="gauge-bg" cx="110" cy="110" r="100"></circle>
                    <circle class="gauge-progress" id="bmi-progress" cx="110" cy="110" r="100"></circle>
                </svg>
                <div class="gauge-center">
                    <h1 id="bmi-score" style="font-size: 3rem; color: var(--text-main);">0.0</h1>
                    <p id="bmi-status" style="font-weight: bold; color: var(--primary);">...</p>
                </div>
            </div>

            <div class="neu-flat" style="padding: 20px; text-align: left; margin-bottom: 20px;">
                <p style="margin-bottom: 10px;"><strong>Recommendation:</strong></p>
                <p id="bmi-advice">Eat healthy and stay active like a zoomie cat!</p>
            </div>

            <button class="neu-btn btn-main" onclick="Router.to('screen-dashboard')">Back Home</button>
        </div>

        <!-- 6. SETTINGS (NEW ADDITION) -->
        <div id="screen-settings" class="screen">
            <div style="display: flex; align-items: center; margin-bottom: 30px;">
                <i class="fas fa-arrow-left" style="font-size: 1.2rem; cursor: pointer; padding: 10px;" onclick="Router.to('screen-dashboard')"></i>
                <h3 style="margin-left: 10px;">Settings</h3>
            </div>

            <div style="margin-bottom: 30px;">
                <p style="font-weight: 700; margin-bottom: 15px; margin-left: 5px;">ACCOUNT</p>
                <div class="neu-flat settings-item">
                    <div class="settings-label"><i class="fas fa-user settings-icon"></i> <span id="settings-name">User</span></div>
                    <i class="fas fa-pen" style="font-size: 0.8rem; color: var(--text-light)"></i>
                </div>
            </div>

            <div style="margin-bottom: 30px;">
                <p style="font-weight: 700; margin-bottom: 15px; margin-left: 5px;">APP INFO</p>
                <div class="neu-flat settings-item">
                    <div class="settings-label"><i class="fas fa-info-circle settings-icon"></i> Version</div>
                    <span style="color: var(--text-light)">1.0.2</span>
                </div>
                <div class="neu-flat settings-item">
                    <div class="settings-label"><i class="fas fa-palette settings-icon"></i> Theme</div>
                    <span style="color: var(--text-light)">Light</span>
                </div>
            </div>

            <div style="margin-top: auto;">
                <button class="neu-btn btn-main btn-danger" onclick="Settings.resetApp()">
                    <i class="fas fa-trash-alt" style="margin-right: 10px;"></i> Reset All Data
                </button>
                <p style="text-align: center; margin-top: 20px; font-size: 0.75rem;">This will delete your name and BMI history.</p>
            </div>
        </div>

        <!-- NAVIGATION BAR (Visible on Dash) -->
        <div class="neu-flat nav-bar" id="bottom-nav" style="display: none;">
            <div class="nav-item active" onclick="Router.to('screen-dashboard')"><i class="fas fa-home"></i></div>
            <div class="nav-item" onclick="Router.to('screen-calc')"><i class="fas fa-calculator"></i></div>
            <div class="nav-item" onclick="Router.to('screen-settings')"><i class="fas fa-cog"></i></div>
        </div>

    </div>

    <script>
        /**
         * Purrfect Fit - Logic
         * Uses LocalStorage, Custom Event Handling, and SVG Manipulation
         */

        const AppData = {
            user: localStorage.getItem('purrfect_user') || null,
            gender: 'male',
            height: 170,
            weight: 65,
            age: 25,
            facts: [
                "Cats can jump up to 6 times their length.",
                "A house cat's genome is 95.6% tiger.",
                "Cats use their whiskers to determine if they can fit.",
                "Purring promotes bone density healing!"
            ]
        };

        // --- ROUTER SYSTEM ---
        const Router = {
            to: (screenId) => {
                document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
                document.getElementById(screenId).classList.add('active');

                // Toggle Bottom Nav visibility
                const nav = document.getElementById('bottom-nav');
                if(screenId === 'screen-dashboard') {
                    nav.style.display = 'flex';
                    UI.loadCatFact();
                } else {
                    nav.style.display = 'none';
                }
            }
        };

        // --- AUTH SYSTEM ---
        const Auth = {
            init: () => {
                if(AppData.user) {
                    document.getElementById('display-username').innerText = AppData.user;
                    // Pre-fill settings name
                    document.getElementById('settings-name').innerText = AppData.user;
                    UI.checkLastBMI();
                    Router.to('screen-dashboard');
                }
            },
            signUp: () => {
                const name = document.getElementById('input-name').value;
                if(!name) {
                    alert("Please tell us your name, human!");
                    return;
                }
                AppData.user = name;
                localStorage.setItem('purrfect_user', name);
                document.getElementById('display-username').innerText = name;
                document.getElementById('settings-name').innerText = name;
                Router.to('screen-dashboard');
            }
        };

        // --- CALCULATOR ENGINE ---
        const Calculator = {
            setGender: (g) => {
                AppData.gender = g;
                document.querySelectorAll('.gender-option').forEach(el => el.classList.remove('active'));
                document.getElementById('btn-' + g).classList.add('active');
            },
            updateHeight: (val) => {
                AppData.height = parseInt(val);
                document.getElementById('height-val').innerText = AppData.height;
            },
            updateWeight: (delta) => {
                AppData.weight += delta;
                if(AppData.weight < 1) AppData.weight = 1;
                document.getElementById('weight-val').innerText = AppData.weight;
            },
            updateAge: (delta) => {
                AppData.age += delta;
                if(AppData.age < 1) AppData.age = 1;
                document.getElementById('age-val').innerText = AppData.age;
            },
            calculate: () => {
                const hM = AppData.height / 100;
                const bmi = (AppData.weight / (hM * hM)).toFixed(1);
                
                // Save result
                localStorage.setItem('purrfect_last_bmi', bmi);
                
                // Show Result Screen
                Router.to('screen-result');
                UI.animateGauge(bmi);
                UI.setAdvice(bmi);
                UI.checkLastBMI(); // update dash for next time
            }
        };

        // --- NEW SETTINGS FUNCTIONALITY ---
        const Settings = {
            resetApp: () => {
                if(confirm("Are you sure? This will delete your profile and BMI history.")) {
                    localStorage.removeItem('purrfect_user');
                    localStorage.removeItem('purrfect_last_bmi');
                    
                    // Simple reload to reset state
                    location.reload();
                }
            }
        };

        // --- UI UTILITIES ---
        const UI = {
            animateGauge: (score) => {
                const max = 40; // Max BMI for gauge scaling
                const circle = document.getElementById('bmi-progress');
                const radius = circle.r.baseVal.value;
                const circumference = 2 * Math.PI * radius; // approx 628
                
                // Calculate color & text
                let color, status;
                if (score < 18.5) { color = "#60A5FA"; status = "Underweight"; }
                else if (score < 25) { color = "#4ADE80"; status = "Healthy"; }
                else if (score < 30) { color = "#FACC15"; status = "Overweight"; }
                else { color = "#F87171"; status = "Obese"; }

                // Text Updates
                document.getElementById('bmi-score').innerText = score;
                document.getElementById('bmi-status').innerText = status;
                document.getElementById('bmi-status').style.color = color;
                
                // Reset stroke for animation
                circle.style.strokeDashoffset = circumference;
                circle.style.stroke = color;

                // Animate
                setTimeout(() => {
                    const offset = circumference - ((Math.min(score, max) / max) * circumference);
                    circle.style.strokeDashoffset = offset;
                }, 100);
            },
            setAdvice: (bmi) => {
                const el = document.getElementById('bmi-advice');
                if(bmi < 18.5) el.innerText = "You need some treats! Let's bulk up slightly with more protein.";
                else if(bmi < 25) el.innerText = "Purrfect! You are in great shape. Keep chasing those lasers!";
                else if(bmi < 30) el.innerText = "A bit fluffy! Let's try more playtime and walks.";
                else el.innerText = "Chonky alert! It's time for a diet plan and serious exercise.";
            },
            checkLastBMI: () => {
                const last = localStorage.getItem('purrfect_last_bmi');
                const card = document.getElementById('last-result-card');
                if(last) {
                    document.getElementById('dash-last-bmi').innerText = last;
                    card.style.display = 'flex';
                }
            },
            loadCatFact: () => {
                const random = AppData.facts[Math.floor(Math.random() * AppData.facts.length)];
                document.getElementById('cat-fact-text').innerText = `"${random}"`;
            }
        };

        // Initialize
        window.onload = Auth.init;

    </script>
</body>
</html>
"""

# 4. Render the HTML component
# The height is set to 850px to accommodate the "app-shell" which is 812px high.
components.html(html_code, height=850, scrolling=True)