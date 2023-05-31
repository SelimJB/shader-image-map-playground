precision mediump float;

uniform vec2 u_resolution;
uniform sampler2D u_texture_0;
uniform vec2 u_mouse;
uniform float u_time;

// Glow
vec3 uGlowColor=vec3(1.,1.,0.);
float uGlowRadius=.03;
float uGlowPulsationRadius=.01;
float uGlowPulsationPeriod=.5;

// TODO better easing
float easing(float t){
    return(sin(t)+1.)/2.;
}

void main(){
    vec2 uv=gl_FragCoord.xy/u_resolution.xy;
    vec4 color=texture2D(u_texture_0,uv);
    
    // GLOWING
    float radius=uGlowPulsationRadius*easing(u_time/uGlowPulsationPeriod)+uGlowRadius;
    
    vec4 sum=vec4(0.,0.,0.,0.);
    vec2 offset=vec2(0.,0.);
    const int sample=64;
    
    for(int i=0;i<sample;i++){
        float angle=360.*float(i)/float(sample);
        
        offset.x=radius*cos(radians(angle));
        offset.y=radius*sin(radians(angle));
        
        float threshold=.003;
        sum+=texture2D(u_texture_0,clamp(offset+uv,vec2(0.+threshold),vec2(1.-threshold)));
        sum+=texture2D(u_texture_0,clamp(offset*.9+uv,vec2(0.+threshold),vec2(1.-threshold)));
        sum+=texture2D(u_texture_0,clamp(offset*.8+uv,vec2(0.+threshold),vec2(1.-threshold)));
        sum+=texture2D(u_texture_0,clamp(offset*.7+uv,vec2(0.+threshold),vec2(1.-threshold)));
        sum+=texture2D(u_texture_0,clamp(offset*.6+uv,vec2(0.+threshold),vec2(1.-threshold)));
    }
    sum/=float(sample*6);// should divide by 5 but 6 looks better
    
    vec4 glowTemp=vec4(uGlowColor,sum.a);
    glowTemp.rgb*=glowTemp.a;// Pre-multiply RGB channels by alpha
    
    vec4 glow=mix(glowTemp,vec4(0.,0.,0.,0.),color.a);
    
    // Add glow
    gl_FragColor=color + glow;
}
