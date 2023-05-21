# Shaders

### How ?  
            
    > Show glslcanvas

### Args :
- u_time: a float representing elapsed time in seconds.
- u_resolution: a vec2 representing the dimensions of the viewport.
- u_mouse: a vec2 representing the position of the mouse, defined in Javascript with .setMouse({x:[value],y:[value]).
- u_tex[number]: a sampler2D containing textures loaded with the data-textures attribute. (cf settings "glsl-canvas.textures")

### Doc :  
- https://github.com/patriciogonzalezvivo/glslCanvas

### Extensions :
- glsl-canvas
- glsl lint
- shader languages support for vscode

### Tools :
- https://github.com/KhronosGroup/glslang/releases -> to use glsl lint



### Todo :
- Scaling
- Deformation 
- Rotations
- Distance functions


# OpenCV