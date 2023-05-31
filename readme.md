Boilerplate project with a set of tools to quickly draft fragment shaders and produce assets for shaders

# Shaders

They are located in the `./shaders` folder. The purpose is to be able to do quick draft and experimentations.

![image-20230531110246649](./doc/assets/image-20230531110246649.png)

### How ?  

    > Show glslcanvas

### Args :
- u_time: a float representing elapsed time in seconds.
- u_resolution: a vec2 representing the dimensions of the viewport.
- u_mouse: a vec2 representing the position of the mouse, defined in Javascript with .setMouse({x:[value],y:[value]).
- u_texture_[number]: a sampler2D containing textures loaded with the data-textures attribute. (cf settings "glsl-canvas.textures")

### Doc :  
- https://github.com/actarian/glsl-canvas

### Extensions :
- glsl-canvas
- glsl lint
- shader languages support for vscode

### Tools :
- https://github.com/KhronosGroup/glslang/releases -> to use glsl lint




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

## ShaderMapGeneration

`./scripts/shader_map_generation` : set of notebooks and basic image operations to produce shader assets. 

The process is different for each images. `map_image_processing_template.ipynb` is a template that can be used as a basis for asset generation.

**Example** 

From :

![image-20230531111542957](./doc/assets/image-20230531111542957.png)

We can obtain :

![image-20230531111633923](./doc/assets/image-20230531111633923.png)
![image-20230531111555960](./doc/assets/image-20230531111555960.png)
![image-20230531111607607](./doc/assets/image-20230531111607607.png)
![image-20230531111619209](./doc/assets/image-20230531111619209.png)
![image-20230531111708819](./doc/assets/image-20230531112547638.png)

With which we can achieve these effect :

![image-20230531111708819](./doc/assets/effect.gif)
