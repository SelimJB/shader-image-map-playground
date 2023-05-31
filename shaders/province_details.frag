#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

uniform sampler2D u_texture_30;
uniform sampler2D u_texture_31;
uniform sampler2D u_texture_32;
uniform sampler2D u_texture_33;

// Initialisation
float uQuantizationLevelAmount=26.;
int uProvinceCount=20;
vec4 uProvinceColors[512];

// Update
vec3 uCurrentProvinceColor;
int uCurrentQuantization=20;
vec2 uMousePos;

// Debug
bool uUseDebug=false;
int uDebugIndex=0;
vec4 uDebugColor=vec4(1.,0.,0.,1.);

float quantizedColorLevel(vec4 color){
    float r=floor(color.r*uQuantizationLevelAmount);
    float g=floor(color.g*uQuantizationLevelAmount);
    float b=floor(color.b*uQuantizationLevelAmount);
    
    if(r==0.||g==0.||g==uQuantizationLevelAmount||b!=1.||color.a<1.){
        return 0.;
    }
    
    return g+(uQuantizationLevelAmount-r)*100.;
}

float easing(float t){
    return(sin(t)+1.)/2.;
}

vec4 getColor(int index)
{
    int ind=index-(13*(index/13));
    vec3 colors[13];
    colors[0]=vec3(1.,0.,0.);
    colors[1]=vec3(1.,.5,0.);
    colors[2]=vec3(1.,1.,0.);
    colors[3]=vec3(.5,1.,0.);
    colors[4]=vec3(0.,1.,0.);
    colors[5]=vec3(0.,1.,.5);
    colors[6]=vec3(0.,1.,1.);
    colors[7]=vec3(0.,.5,1.);
    colors[8]=vec3(0.,0.,1.);
    colors[9]=vec3(.5,0.,1.);
    colors[10]=vec3(1.,0.,1.);
    colors[11]=vec3(1.,0.,.5);
    colors[12]=vec3(1.,1.,1.);
    
    for(int i=0;i<13;++i){
        if(i==ind){
            return vec4(colors[i].rgb,1.);
        }
    }
    
    return vec4(colors[0].rgb,1.);
}

void main(){
    vec2 pos=gl_FragCoord.xy;
    vec2 uv=gl_FragCoord.xy/u_resolution.xy;
    
    vec4 map=texture2D(u_texture_30,uv);
    vec4 colorMap=texture2D(u_texture_31,uv);
    vec4 colorGlowMap=texture2D(u_texture_33,uv);
    vec4 colorBorders=texture2D(u_texture_32,uv);
    
    vec4 cursorPixelColor=texture2D(u_texture_31,u_mouse/u_resolution);
    int cursorQuantization=int(quantizedColorLevel(cursorPixelColor));
    float cursorQuantizationF=quantizedColorLevel(cursorPixelColor);
    vec4 currentColor=getColor(cursorQuantization);
    
    int fragmentQuant=int(quantizedColorLevel(colorMap));
    vec4 fragmentColor=getColor(fragmentQuant);
    
    if(uUseDebug&&uDebugIndex!=0){
        if(uDebugIndex==2)
        gl_FragColor=map;
        if(uDebugIndex==3)
        gl_FragColor=colorMap;
        if(uDebugIndex==4)
        gl_FragColor=colorGlowMap;
        if(uDebugIndex==5)
        gl_FragColor=colorBorders;
        if(uDebugIndex==6)
        gl_FragColor=uDebugColor;
        
        return;
    }
    
    vec4 provinceColor;
    
    if(cursorQuantization==fragmentQuant&&uCurrentQuantization!=0){
        provinceColor=mix(fragmentColor,map,.54);
    }
    else{
        int index=fragmentQuant;
        if(index==0){
            provinceColor=map;
        }
        else{
            provinceColor=mix(fragmentColor,map,.94);
        }
    }
    
    gl_FragColor=provinceColor;
    
    // Alpha blend
    gl_FragColor=mix(gl_FragColor,colorBorders,colorBorders.a);
    
    // Cursor
    vec2 mousePosition=u_mouse/u_resolution;
    float d=smoothstep(0.,.05,distance(uv,mousePosition));
    gl_FragColor+=(1.-d)*vec4(currentColor.rgb,1.)*.47;
}
