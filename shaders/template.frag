#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;
uniform sampler2D u_texture_0;
uniform sampler2D u_texture_1;
uniform vec2 u_mouse;

void main(){
    vec2 uv=gl_FragCoord.xy/u_resolution.xy;
    vec4 texColor=texture2D(u_texture_0,uv);
    
    float dist = distance(uv, u_mouse/u_resolution);
    float circle = smoothstep(0.1, 0.12, dist);
    
    vec4 v = mix(vec4(0.1373, 0.1098, 0.1098, 1.0), vec4(0.0, 0.0, 1.0, 1.0), circle);
    gl_FragColor=texColor;
}