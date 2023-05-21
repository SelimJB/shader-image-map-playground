precision mediump float;

uniform float u_time;

void main(){
    gl_FragColor=vec4(1,1,sin(u_time*2.),1);
}