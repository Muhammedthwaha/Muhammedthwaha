import os

def generate_svg(mode):
    # Colors
    if mode == 'dark':
        bg_color = "#030712"
        panel_color = "#0F172A"
        border_color = "rgba(255,255,255,0.08)"
        text_color = "#F8FAFC"
        muted_color = "#94A3B8"
        accent1 = "#7C3AED"
        accent2 = "#22D3EE"
        accent3 = "#10B981"
        glow_opacity = "0.4"
    else:
        bg_color = "#FFFFFF"
        panel_color = "#F8FAFC"
        border_color = "rgba(15,23,42,0.08)"
        text_color = "#0F172A"
        muted_color = "#475569"
        accent1 = "#2563EB"
        accent2 = "#06B6D4"
        accent3 = "#10B981"
        glow_opacity = "0.2"

    ascii_art = [
        "      :::   :::   ::::::::::: :::    ::: ",
        "    :+:+: :+:+:      :+:     :+:    :+:  ",
        "  +:+ +:+:+ +:+     +:+     +:+    +:+   ",
        " +#+  +:+  +#+     +#+     +#+    +:+    ",
        "+#+       +#+     +#+     +#+    +#+     ",
        "#+#       #+#     #+#     #+#    #+#     ",
        "###       ###     ###      ########      ",
        "                                         ",
        "         01010011 01011001 01010011      ",
        "         01010100 01000101 01001101      "
    ]

    skills = [
        "Python", "HTML5", "CSS3", "AWS", "MySQL", 
        "Postgres", "Figma", "Canva", "Pandas", 
        "Numpy", "Matplotlib", "Git", "Power BI"
    ]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap');
            
            .bg {{ fill: {bg_color}; }}
            .panel {{ fill: {panel_color}; stroke: {border_color}; stroke-width: 1.5; rx: 16; }}
            .text-primary {{ fill: {text_color}; font-family: 'Inter', sans-serif; }}
            .text-muted {{ fill: {muted_color}; font-family: 'Inter', sans-serif; }}
            .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
            
            /* Glassmorphism filter base */
            .glass {{ filter: drop-shadow(0 4px 16px rgba(0,0,0,{0.3 if mode=='dark' else 0.05})); }}
            
            /* Skills Hover Effects */
            .skill-pill {{ cursor: pointer; transition: all 0.3s ease; }}
            .skill-pill:hover {{ transform: scale(1.05); stroke: url(#accent-grad); }}
            
            /* Typing animation classes */
            .type-line {{ overflow: hidden; white-space: nowrap; }}
        </style>
        
        <linearGradient id="accent-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{accent1}">
                <animate attributeName="stop-color" values="{accent1};{accent2};{accent3};{accent1}" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="50%" stop-color="{accent2}">
                <animate attributeName="stop-color" values="{accent2};{accent3};{accent1};{accent2}" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{accent3}">
                <animate attributeName="stop-color" values="{accent3};{accent1};{accent2};{accent3}" dur="8s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <radialGradient id="bg-glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{accent2}" stop-opacity="{glow_opacity}">
                <animate attributeName="stop-color" values="{accent1};{accent2};{accent3};{accent1}" dur="12s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{bg_color}" stop-opacity="0" />
        </radialGradient>
        
        <radialGradient id="bg-glow-2" cx="20%" cy="80%" r="50%">
            <stop offset="0%" stop-color="{accent1}" stop-opacity="{glow_opacity}">
                <animate attributeName="stop-color" values="{accent3};{accent1};{accent2};{accent3}" dur="15s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{bg_color}" stop-opacity="0" />
        </radialGradient>
        
        <!-- Noise filter -->
        <filter id="noise">
            <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/>
            <feColorMatrix type="matrix" values="1 0 0 0 0, 0 1 0 0 0, 0 0 1 0 0, 0 0 0 0.05 0" />
        </filter>
        
        <clipPath id="typing-mask-1">
            <rect x="0" y="0" width="0" height="30">
                <animate attributeName="width" from="0" to="600" begin="1s" dur="1.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" />
            </rect>
        </clipPath>
        <clipPath id="typing-mask-2">
            <rect x="0" y="0" width="0" height="30">
                <animate attributeName="width" from="0" to="600" begin="2.8s" dur="1.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" />
            </rect>
        </clipPath>
        <clipPath id="typing-mask-3">
            <rect x="0" y="0" width="0" height="30">
                <animate attributeName="width" from="0" to="600" begin="4.6s" dur="1s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" />
            </rect>
        </clipPath>
        <clipPath id="typing-mask-4">
            <rect x="0" y="0" width="0" height="30">
                <animate attributeName="width" from="0" to="600" begin="6.0s" dur="1s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" />
            </rect>
        </clipPath>
    </defs>

    <!-- Background -->
    <rect width="100%" height="100%" class="bg" rx="20"/>
    
    <!-- Floating radial gradients for subtle glow -->
    <circle cx="20%" cy="30%" r="400" fill="url(#bg-glow)">
        <animateTransform attributeName="transform" type="translate" values="0,0; 50,-50; 0,0" dur="10s" repeatCount="indefinite"/>
    </circle>
    <circle cx="80%" cy="70%" r="400" fill="url(#bg-glow-2)">
        <animateTransform attributeName="transform" type="translate" values="0,0; -50,50; 0,0" dur="12s" repeatCount="indefinite"/>
    </circle>
    
    <!-- Noise texture overlay -->
    <rect width="100%" height="100%" filter="url(#noise)" opacity="0.4" rx="20" style="mix-blend-mode: overlay;"/>

    <!-- LEFT SIDE (38% = 448px) -->
    <g transform="translate(30, 30)">
        <rect width="400" height="550" class="panel glass" />
        
        <!-- Inner glowing border for left panel -->
        <rect width="398" height="548" x="1" y="1" rx="15" fill="none" stroke="url(#accent-grad)" stroke-width="1" opacity="0.3">
            <animate attributeName="opacity" values="0.2;0.6;0.2" dur="4s" repeatCount="indefinite" />
        </rect>

        <!-- Floating ASCII Container -->
        <g transform="translate(50, 160)">
            <animateTransform attributeName="transform" type="translate" values="50,160; 50,150; 50,160" dur="6s" repeatCount="indefinite"/>
            
            <text class="font-mono" font-size="14" font-weight="bold" fill="url(#accent-grad)" style="letter-spacing: 2px;">
"""
    
    # Generate ASCII lines with staggered opacity reveals
    for i, line in enumerate(ascii_art):
        svg += f'                <tspan x="0" dy="24" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{i*0.2}s" dur="0.5s" fill="freeze" />{line.replace(" ", "&#160;")}</tspan>\n'
        
    svg += f"""
            </text>
            
            <!-- Moving scanline over ASCII -->
            <rect x="-20" y="0" width="340" height="4" fill="url(#accent-grad)" opacity="0.5" filter="blur(2px)">
                <animateTransform attributeName="transform" type="translate" values="0,-20; 0,260; 0,-20" dur="4s" repeatCount="indefinite" />
            </rect>
        </g>
        
        <!-- Terminal Decorators left side -->
        <circle cx="20" cy="20" r="5" fill="#EF4444" opacity="0.8"/>
        <circle cx="40" cy="20" r="5" fill="#F59E0B" opacity="0.8"/>
        <circle cx="60" cy="20" r="5" fill="#10B981" opacity="0.8"/>
    </g>

    <!-- RIGHT SIDE (62% = 732px space available) -->
    <g transform="translate(450, 30)">
        <rect width="700" height="550" class="panel glass" />
        
        <!-- Header -->
        <text x="40" y="65" class="text-primary" font-size="36" font-weight="700">Hi 👋 I'm Muhammed Thaha Uwais</text>
        
        <!-- Typing Terminal -->
        <g transform="translate(40, 110)">
            <text class="font-mono text-muted" font-size="18">
                <tspan x="0" dy="0" fill="url(#accent-grad)" font-weight="bold">&gt; </tspan>
                <tspan clip-path="url(#typing-mask-1)" class="text-primary">Computer Science Engineering graduate</tspan>
                
                <tspan x="0" dy="30" fill="url(#accent-grad)" font-weight="bold"><animate attributeName="opacity" values="0;1;1" keyTimes="0;0.9;1" dur="2.7s" fill="freeze"/>&gt; </tspan>
                <tspan clip-path="url(#typing-mask-2)" class="text-primary">IT Support Analyst &amp; QA Tester</tspan>
                
                <tspan x="0" dy="30" fill="url(#accent-grad)" font-weight="bold"><animate attributeName="opacity" values="0;1;1" keyTimes="0;0.9;1" dur="4.5s" fill="freeze"/>&gt; </tspan>
                <tspan clip-path="url(#typing-mask-3)" class="text-primary">Full Stack Developer</tspan>
                
                <tspan x="0" dy="30" fill="url(#accent-grad)" font-weight="bold"><animate attributeName="opacity" values="0;1;1" keyTimes="0;0.9;1" dur="5.9s" fill="freeze"/>&gt; </tspan>
                <tspan clip-path="url(#typing-mask-4)" class="text-primary">Data Enthusiast</tspan>
                
                <!-- Blinking cursor -->
                <tspan class="text-primary" font-weight="bold">
                    _
                    <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
                </tspan>
            </text>
        </g>
        
        <!-- Details Reveal -->
        <g transform="translate(40, 260)" class="text-muted" font-size="16">
            <text x="0" y="0" opacity="0">
                <animate attributeName="opacity" to="1" begin="7s" dur="0.5s" fill="freeze"/>
                <tspan font-weight="600" class="text-primary">📍 Location:</tspan> Calicut, Kerala, India
            </text>
            <text x="0" y="30" opacity="0">
                <animate attributeName="opacity" to="1" begin="7.3s" dur="0.5s" fill="freeze"/>
                <tspan font-weight="600" class="text-primary">🎓 Education:</tspan> B.Tech in CSE (First Class)
            </text>
            <text x="0" y="60" opacity="0">
                <animate attributeName="opacity" to="1" begin="7.6s" dur="0.5s" fill="freeze"/>
                <tspan font-weight="600" class="text-primary">🎯 Focus:</tspan> QA, IT Support, Data Science, Python
            </text>
            <text x="0" y="90" opacity="0">
                <animate attributeName="opacity" to="1" begin="7.9s" dur="0.5s" fill="freeze"/>
                <tspan font-weight="600" class="text-primary">✉️ Email:</tspan> muhammedthahauwais@gmail.com
            </text>
        </g>

        <!-- Skills Section -->
        <g transform="translate(40, 390)">
            <text x="0" y="0" class="text-primary" font-size="20" font-weight="700" opacity="0">
                <animate attributeName="opacity" to="1" begin="8.2s" dur="0.5s" fill="freeze"/>
                Tech Stack
            </text>
            
            <g transform="translate(0, 20)">
"""
    # Generate glowing skill pills
    x_pos = 0
    y_pos = 0
    row_height = 40
    max_width = 620
    
    delay = 8.5
    for skill in skills:
        # Approximate width based on characters
        width = len(skill) * 10 + 30
        if x_pos + width > max_width:
            x_pos = 0
            y_pos += row_height
            
        svg += f"""
                <g transform="translate({x_pos}, {y_pos})" class="skill-pill" opacity="0">
                    <animate attributeName="opacity" to="1" begin="{delay}s" dur="0.4s" fill="freeze" />
                    <!-- Base rect -->
                    <rect width="{width}" height="30" rx="15" fill="{bg_color}" stroke="{border_color}" stroke-width="1.5">
                        <animate attributeName="stroke" values="{border_color};{accent2};{border_color}" begin="{delay}s" dur="2s" />
                    </rect>
                    <!-- Text -->
                    <text x="{width/2}" y="20" class="text-primary font-mono" font-size="13" font-weight="500" text-anchor="middle">{skill}</text>
                </g>
"""
        x_pos += width + 10
        delay += 0.1

    svg += f"""
            </g>
        </g>
        
        <!-- Social Icons (Minimal) -->
        <g transform="translate(40, 500)" opacity="0">
            <animate attributeName="opacity" to="1" begin="9.5s" dur="0.8s" fill="freeze"/>
            <text x="0" y="20" class="text-muted font-mono" font-size="14">Connect &gt;</text>
            
            <!-- GitHub -->
            <g transform="translate(100, 0)">
                <rect width="90" height="30" rx="6" fill="transparent" stroke="{border_color}"/>
                <text x="45" y="19" class="text-primary font-mono" font-size="12" text-anchor="middle">GitHub</text>
            </g>
            <!-- LinkedIn -->
            <g transform="translate(200, 0)">
                <rect width="90" height="30" rx="6" fill="transparent" stroke="{border_color}"/>
                <text x="45" y="19" class="text-primary font-mono" font-size="12" text-anchor="middle">LinkedIn</text>
            </g>
            <!-- Portfolio -->
            <g transform="translate(300, 0)">
                <rect width="90" height="30" rx="6" fill="transparent" stroke="{border_color}"/>
                <text x="45" y="19" class="text-primary font-mono" font-size="12" text-anchor="middle">Portfolio</text>
            </g>
            
            <!-- Glowing line at bottom -->
            <rect x="0" y="40" width="620" height="1" fill="url(#accent-grad)" opacity="0.3">
                <animate attributeName="opacity" values="0.1;0.5;0.1" dur="3s" repeatCount="indefinite" />
            </rect>
        </g>
    </g>
</svg>"""
    
    with open(f"C:\\Users\\mthah\\.gemini\\antigravity\\scratch\\github_hero\\{mode}.svg", "w", encoding='utf-8') as f:
        f.write(svg)

generate_svg('dark')
generate_svg('light')
print("Generated SVGs successfully.")
