precision mediump float;

uniform vec2 u_resolution;
uniform sampler2D u_texture_1;
uniform sampler2D u_texture_2;
uniform float u_arraySize;
uniform float u_floatArr[256];
uniform vec2 u_mouse;

float quantizedGrayscale(vec3 color,float numLevels){
    float grayscale=dot(color,vec3(.299,.587,.114));
    return floor(grayscale*numLevels)/numLevels;
}

float quantizedPinkScale(vec4 color,float numLevels){
    return floor(color.b*numLevels);
}

void main(){
    vec2 uv=gl_FragCoord.xy/u_resolution.xy;
    uv.y=1.-uv.y;
    vec4 map=texture2D(u_texture_1,uv);
    vec4 colorMap=texture2D(u_texture_2,uv);
    vec4 cursorColor=texture2D(u_texture_2,u_mouse/u_resolution.xy);

    vec4 coco = vec4(0.0,0.0,quantizedPinkScale(cursorColor,13.0)/13.0,1.0);
    // vec4 coco = vec4(1.0,0.0,0.0,1.0);
    float d=smoothstep(0.,.5,distance(uv,u_mouse/u_resolution.xy));

    gl_FragColor=colorMap+ coco;
}