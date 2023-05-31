precision mediump float;

uniform vec2 u_resolution;
uniform sampler2D u_texture_0;
uniform vec3 u_color;
uniform float u_intensity;

void rot(){
    vec2 uv=gl_FragCoord.xy/u_resolution.xy;
    vec4 color=texture2D(u_texture_0,uv);
    
    float radius=.03;
    const int samples=8;
    vec2 offset=vec2(0.,0.);
    vec4 blurredColor=vec4(0.,0.,0.,0.);
    for(int i=0;i<samples;i++){
        float angle=2.*3.1415926535897932384626433832795*float(i)/float(samples);
        offset.x=radius*cos(angle);
        offset.y=radius*sin(angle);
        blurredColor+=texture2D(u_texture_0,uv+offset);
    }
}

void main(){
    vec4 sum=vec4(0.);
    float uBlurSize=30.;
    float blurSize=uBlurSize/u_resolution.x;
    vec2 uv=gl_FragCoord.xy/u_resolution.xy;
    uv.y=1.-uv.y;
    vec4 color=texture2D(u_texture_0,uv);
    
    sum+=texture2D(u_texture_0,vec2(uv.x-2.*blurSize,uv.y))*.15;
    sum+=texture2D(u_texture_0,vec2(uv.x-blurSize,uv.y))*.2;
    sum+=texture2D(u_texture_0,uv)*.3;
    sum+=texture2D(u_texture_0,vec2(uv.x+blurSize,uv.y))*.2;
    sum+=texture2D(u_texture_0,vec2(uv.x+2.*blurSize,uv.y))*.15;
    
    vec4 coco=vec4(1.,0.,0.,sum.a);
    coco.rgb*=coco.a;// Pre-multiply RGB channels by alpha
    gl_FragColor=mix(color,coco,1.-color.a);
}

