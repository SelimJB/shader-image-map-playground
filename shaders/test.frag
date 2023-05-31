#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

uniform sampler2D u_texture_10;
uniform sampler2D u_texture_11;
uniform sampler2D u_texture_12;
uniform sampler2D u_texture_13;

void main(){
    vec2 uv=gl_FragCoord.xy/u_resolution.xy;
    vec4 texColor=texture2D(u_texture_10,uv);
    gl_FragColor=texColor;
}