#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;

void main()
{
    // Normalize pixel coordinates (from 0 to 1)
    vec2 uv = gl_FragCoord.xy / u_resolution;

    // Calculate the distance between the current pixel and the mouse position
    float dist = distance(uv, u_mouse/u_resolution);

    // Create a circle based on the distance
    float circle = smoothstep(0.4, 0.2342, dist);

    // Set the output color based on the circle and the mouse position
    gl_FragColor = mix(vec4(0.0627, 0.0118, 0.0118, 1.0), vec4(0.0, 0.0, 1.0, 1.0), circle);
}
