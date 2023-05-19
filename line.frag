#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;
uniform sampler2D u_texture_0;
uniform sampler2D u_texture_3;
uniform vec2 u_mouse;
const float PI=3.14;

float pointLineDistance(vec2 point,vec2 linePoint1,vec2 linePoint2){
    vec2 lineDirection=normalize(linePoint2-linePoint1);
    vec2 pointToLinePoint1=point-linePoint1;
    float t=dot(pointToLinePoint1,lineDirection);
    
    vec2 projection=linePoint1+lineDirection*t;
    return distance(point,projection);
}

vec2 rotation(vec2 point,float degrees){
    float angle=radians(degrees);
    float s=sin(angle);
    float c=cos(angle);
    mat2 rotationMatrix=mat2(c,-s,s,c);
    return rotationMatrix*point;
}

void main(){
    vec2 uv=gl_FragCoord.xy/u_resolution;
    uv.y=1.-uv.y;
    vec4 texColor=texture2D(u_texture_0,uv);
    vec4 texColor2=texture2D(u_texture_3,uv);
    // vec4 color=vec4(.85,.4,.6,1.);
    
    float dist=pointLineDistance(uv,vec2(.5,.5),vec2(.5,.7));
    // float dist2=pointLineDistance(rotation(uv,0.),vec2(.5,.5),vec2(.5,.7));
    float line=1.-smoothstep(.1, .4,dist);
    // float line2=1.-step(.1,dist2);
    
    if(int(line)==0)
    gl_FragColor=vec4(texColor.r,0.,texColor2.g,texColor2.a);
    else
    gl_FragColor=vec4(1.);
}