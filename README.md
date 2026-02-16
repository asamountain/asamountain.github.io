# 📟 Embedded Learning Visuals

Interactive 3D and 2D visualizations designed to help students understand the hidden logic of Bare-Metal C++ on the ATmega328P (Arduino Uno).

## 🚀 Live Demo
**[View the Interactive 3D Timer Visualizer](https://asamountain.github.io/Embedded-Learning-Visuals/)**

## 📂 Project Contents
- **`index.html`**: A Three.js interactive 3D simulation of Timer1 (Clock -> Prescaler -> Register -> LED).
- **`embeddedPractice.cpp`**: Bare-metal C++ source code implementing a 1-second blink using Timer1 CTC mode.
- **`timer_diagram.png`**: A high-level schematic mapping the flow of frequencies.

## 🛠 How to use the 3D Visualizer
1. Open the live link above.
2. **Rotate**: Left-click and drag.
3. **Zoom**: Scroll or pinch.
4. **Observe**: Watch how the 16MHz crystal pulses are reduced by the 1024 prescaler to fill the 16-bit register (the green tank) up to the 15,625 target.

---
*Created with Gemini CLI to bridge the gap between abstract code and physical hardware.*