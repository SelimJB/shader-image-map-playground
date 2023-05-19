#ifdef GL_ES
precision mediump float;
#endif

uniform sampler2D u_texture_1;
uniform sampler2D u_texture_2;
uniform vec2 u_resolution;
uniform vec2 u_mouse;

void main(){
    vec2 uv=gl_FragCoord.xy/u_resolution.xy;
    vec4 color=texture2D(u_texture_1,uv);
    vec4 backgroundColor=texture2D(u_texture_2,uv);

    vec4 cursorColor = texture2D(u_texture_2, u_mouse/u_resolution);

    if (cursorColor == backgroundColor)
        gl_FragColor=color + backgroundColor;
    else
        gl_FragColor=color;
}