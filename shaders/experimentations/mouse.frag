#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;

void main()
{
    vec2 uv = gl_FragCoord.xy / u_resolution;
    float dist = distance(uv, u_mouse/u_resolution);
    float circle = smoothstep(0.4, 0.2342, dist);
    gl_FragColor = mix(vec4(0.0627, 0.0118, 0.0118, 1.0), vec4(0.0, 0.0, 1.0, 1.0), circle);
}
