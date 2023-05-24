Boilerplate project with a set of tools to quickly draft fragment shaders and produce assets for shaders

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


# Image Processing

Using OpenCV to produce assets for shaders

## Concepts
-   Skeletonisation
-   Edge detection
-   Line thinning
-   Noise reduction
-   Morphological operations :
    -   Erosion
    -   Dilatation
    -   Opening
    -   Closing
-   Connected Component Analysis: (on the skeletonized image), will label each separate area of the background (including the holes) with a different number.
    -   Labeling
    -   Filtering
    -   Count holes
    -   Fill holes

## Setup

### Extensions
-   Python v2023.6.1 -> provided the intallations for Pylance and Jupitar
-   Python Image Preview

### Libs
-   pip install opencv-python
-   pip install Pillow
-   pip install matplotlib
-   pip install scikit-image

