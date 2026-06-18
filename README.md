##  🏮 lavalampy 🐍
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/5d4dbb55-0920-43a1-ab69-edb437014d94" />

A lightweight (near-zero resource-hunger), procedural lava lamp-inspired visualizer built with Python and GLSL shaders. Yeah, kind of a screensaver, really.

Instead of rendering heavy 3D graphics or looping a video, this application calculates organic, morphing fluid dynamics mathematically on your GPU in real-time. It features a lightweight, floating Tkinter control panel to adjust the speed and color mood on the fly.

Relax and enjoy the organic patterns - leave them as an ambient lighting device on your office while chilling, working or studying.

### 🧰 Prerequisites
You will need **Python 3.x** installed on your system. 
* **Windows:** Download from the official Python website.

	(Make sure to check the box that says "Add Python to PATH" during installation).
	
* **Mac:** Download from the official website, or install via Homebrew: `brew install python`.

* **Linux:** Python usually comes pre-installed. You may also need the Tkinter package (e.g., `sudo apt install python3-tk` on Ubuntu/Debian).

### 🖲️ Installation & Setup

It is highly recommended to run this inside a Virtual Environment to keep the dependencies contained.

1. Clone or download this repository and open your terminal/command prompt inside the folder.

2. Create a Virtual Environment:
* Windows: `python -m venv venv`
* Mac/Linux: `python3 -m venv venv`

3. Activate the Virtual Environment:
* Windows: `venv\Scripts\activate`
* Mac/Linux: `source venv/bin/activate`

4. Install Dependencies:
Once your environment is active (you'll see `(venv)` in your terminal prompt), install the required libraries:
`pip install moderngl moderngl-window numpy`

### 🏃 How to Run
Put one foot in front of another, in standing position. Repeat as fast as you can, leaving as much linear space between feet as possible.

Make sure your virtual environment is active, then simply run:
`python lava.py`
*(On Mac/Linux, you might need to use `python3 lava.py`).*

A window will open alongside a small, floating settings panel.
* **flow speed:** Controls how fast the fluid moves and morphs.
* **mood:** Slides smoothly across the entire color spectrum to set the vibe.

You can close the settings window safely after you're good with that you see or leave it behind the main one. Hitting the fullscreen shortcut of your system while lavalamp is active will make it take over the display.

### 🚓 Trouble-shooting-the-black (screen)

**Blank/Black Screen or Crashing?**
This app requires OpenGL 3.3 support. 
* **Linux Users:** If you experience very low framerates or the terminal logs say `renderer: llvmpipe`, your system is falling back to CPU rendering. You may need to install appropriate open-source drivers (like `mesa-utils` and `libgl1-mesa-dri`).
* **Mac Users:** macOS has deprecated OpenGL, but ModernGL natively supports up to GL 4.1 on Mac, so this application will still run perfectly without modification.
* **Any other problems should come up**: Sod off, I don't work for you. Figure it out.

Oh and I guess you can fiddle with the .py and see what happens. Shaders are a whole realm. Check out the juxtopposed video on them.
<img width="1366" height="768" alt="2026-06-18_12-50_1" src="https://github.com/user-attachments/assets/a9872409-43bf-40d9-901e-bdc24cadac4b" />
<img width="1366" height="768" alt="2026-06-18_12-50" src="https://github.com/user-attachments/assets/1b642641-b68e-446a-9f7c-585c837b719b" />
<img width="1366" height="768" alt="2026-06-18_12-49" src="https://github.com/user-attachments/assets/9e832d6d-efdb-42b8-b5fe-7596c8aab358" />
