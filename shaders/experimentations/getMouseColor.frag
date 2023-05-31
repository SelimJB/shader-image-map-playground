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
    
    float dist=distance(uv,u_mouse/u_resolution);
    float circle=smoothstep(.3,.0,dist);
    
    vec4 mousePixelColor=texture2D(u_texture_0,u_mouse/u_resolution);
    vec4 v=mix(texColor,mousePixelColor,circle);
    
    vec4 texColor2=texture2D(u_texture_1,uv);
    
    gl_FragColor=v;
}