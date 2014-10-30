void setup(){
  size(200,200);
}
void draw(){
  int centerX = width/2;
  int centerY = height/2;
  makeTriangle(centerX, centerY, 50);
  ellipse(centerX, centerY, 5, 5);
  noLoop();
}
void makeTriangle(int centerX, int centerY, int tSize){
  triangle(centerX, centerY-tSize, centerX-(tSize * cos(radians(60))), centerY + (tSize * sin(radians(60))), centerX+(tSize * cos(radians(60))), centerY + (tSize * sin(radians(60))));
}
