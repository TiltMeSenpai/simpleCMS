size(400,400);

float x;
float y;

for (int i = 0; i < 100; i = i+1) {
  x = random(360);
  y = random(360);
  fill(random(255), random(255), random(255));
  ellipse(x+20, y+20, 20,20);
} 
