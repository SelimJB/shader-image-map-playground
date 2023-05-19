#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;
uniform sampler2D u_texture_0;

void main(){
    vec2 uv=gl_FragCoord.xy/u_resolution.xy;
    vec4 texColor=texture2D(u_texture_0,uv);
    gl_FragColor=texColor;
}