precision mediump float;

uniform vec2 resolution;
uniform sampler2D uMainSampler;
uniform vec3 u_color;
uniform float u_intensity;
varying vec2 outTexCoord;

void main(){
    vec4 sum=vec4(0.);
    float uBlurSize=30.;
    float blurSize=uBlurSize/resolution.x;
    vec2 uv=gl_FragCoord.xy/resolution.xy;
    uv.y=1.-uv.y;
    vec4 color=texture2D(uMainSampler,uv);
    
    // TODO ROTATION
    sum+=texture2D(uMainSampler,vec2(outTexCoord.x-2.*blurSize,outTexCoord.y))*.15;
    sum+=texture2D(uMainSampler,vec2(outTexCoord.x-blurSize,outTexCoord.y))*.2;
    sum+=texture2D(uMainSampler,outTexCoord)*.3;
    sum+=texture2D(uMainSampler,vec2(outTexCoord.x+blurSize,outTexCoord.y))*.2;
    sum+=texture2D(uMainSampler,vec2(outTexCoord.x+2.*blurSize,outTexCoord.y))*.15;
    
    vec4 coco=vec4(1.,0.,0.,sum.a);
    coco.rgb*=coco.a;// Pre-multiply RGB channels by alpha
    gl_FragColor=mix(color,coco,1.-color.a);
}

void rot(){
    vec2 uv=gl_FragCoord.xy/resolution.xy;
    vec4 color = texture2D(uMainSampler, uv);

    float radius = 0.03;
    const int samples = 8;
    vec2 offset=vec2(0.,0.);
    vec4 blurredColor = vec4(0.0, 0.0, 0.0, 0.0);
    for(int i=0;i<samples;i++){
        float angle=2.*3.1415926535897932384626433832795*float(i)/float(samples);
        offset.x=radius*cos(angle);
        offset.y=radius*sin(angle);
        blurredColor+=texture2D(uMainSampler,uv+offset);
    }
}