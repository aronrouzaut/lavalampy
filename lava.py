import moderngl
import moderngl_window as mglw
import tkinter as tk
import numpy as np
from threading import Thread

# Shared dictionary to pass live configuration data between windows safely
PARAMS = {
    'speed': 0.4,
    'hue': 0.6  # Default to a calming blue/purple
}

class LavaApp(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "lavalampy"
    window_size = (1280, 720)
    aspect_ratio = None
    resizable = True

    # High-performance procedural noise shader
    fragment_shader = """
    #version 330
    uniform float u_time;
    uniform float u_speed;
    uniform float u_hue;
    uniform vec2 u_resolution;
    out vec4 fragColor;

    // Pseudo-random hash function for noise generation
    float hash(vec2 p) {
        return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453123);
    }

    // 2D Smooth Value Noise
    float noise(vec2 p) {
        vec2 i = floor(p);
        vec2 f = fract(p);
        vec2 u = f * f * (3.0 - 2.0 * f);
        return mix(mix(hash(i + vec2(0.0,0.0)), hash(i + vec2(1.0,0.0)), u.x),
                   mix(hash(i + vec2(0.0,1.0)), hash(i + vec2(1.0,1.0)), u.x), u.y);
    }

    // Fast GPU conversion from HSV color space to standard RGB
    vec3 hsv2rgb(vec3 c) {
        vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
        vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
        return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
    }

    void main() {
        // Normalize aspect ratio so shapes don't stretch
        vec2 uv = gl_FragCoord.xy / u_resolution.xy;
        vec2 st = uv * vec2(3.0 * (u_resolution.x / u_resolution.y), 3.0);
        
        float t = u_time * u_speed * 0.6;
        
        // Distort and layer two noise maps to simulate morphing liquid blobs
        float n1 = noise(st + vec2(t * 0.5, t * 0.3));
        float n2 = noise(st - vec2(t * 0.3, t * 0.5) + vec2(n1 * 1.2));
        
        // Lock visual bounds: never fully black (0.15), never fully blown-out white (0.85)
        float liquid = mix(0.10, 0.90, n2);
        
        // Calculate Dynamic Analogous Palette
        // Primary Base Color
        vec3 baseColor = hsv2rgb(vec3(u_hue, 0.75, liquid));
        // Analogous Highlight (shifted down the wheel slightly by 0.08)
        vec3 analogColor = hsv2rgb(vec3(fract(u_hue + 0.08), 0.80, liquid * 1.1));
        
        // Blend colors seamlessly where blobs cross paths
        vec3 final_color = mix(baseColor, analogColor, n1);
        
        fragColor = vec4(final_color, 1.0);
    }
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prog = self.ctx.program(
            vertex_shader="""
                #version 330
                in vec2 in_vert;
                void main() { gl_Position = vec4(in_vert, 0.0, 1.0); }
            """,
            fragment_shader=self.fragment_shader
        )
        
        vertices = np.array([
            -1.0, -1.0,  1.0, -1.0, -1.0,  1.0,
            -1.0,  1.0,  1.0, -1.0,  1.0,  1.0,
        ], dtype='f4')
        
        self.vbo = self.ctx.buffer(vertices.tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert')
        
        # Link uniforms
        self.u_time = self.prog['u_time']
        self.u_speed = self.prog['u_speed']
        self.u_hue = self.prog['u_hue']
        self.u_resolution = self.prog['u_resolution']

    def on_render(self, time, frametime):
        self.u_time.value = time
        self.u_speed.value = PARAMS['speed']
        self.u_hue.value = PARAMS['hue']
        self.u_resolution.value = self.window_size
        
        self.vao.render()

# Native Tkinter Controller Window
def open_menu():
    root = tk.Tk()
    root.title("lavalampy controls")
    root.geometry("300x150")
    root.attributes('-topmost', True)

    def update_speed(val): PARAMS['speed'] = float(val)
    def update_hue(val): PARAMS['hue'] = float(val)

    tk.Scale(root, label="flow speed", from_=0.0, to=2.0, resolution=0.05, 
             orient="horizontal", command=update_speed).pack(fill="x", padx=10, pady=5)
    
    hue_slider = tk.Scale(root, label="mood", from_=0.0, to=1.0, resolution=0.01, 
             orient="horizontal", command=update_hue)
    hue_slider.pack(fill="x", padx=10, pady=5)
    
    hue_slider.set(PARAMS['hue'])

    root.mainloop()

if __name__ == '__main__':
    Thread(target=open_menu, daemon=True).start()
    mglw.run_window_config(LavaApp)
