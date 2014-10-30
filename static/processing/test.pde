void setup(){
  size(displayHeight, displayHeight);
}

class Ant{
  int dir, x, y;
  Ant(){
    dir = 0;
    x = y = 50;
  }
  void step(){
    switch(dir){
      case 0:
        x++;
        break;
      case 1:
        y++;
        break;
      case 2:
        x--;
        break;
      case 3:
        y--;
        break;
    }
    x += 100;
    y += 100;
    x %= 100;
    y %= 100;
  }
}
void rdraw(int[][] cells){
  for (int i = 0; i < cells.length; i++) {
    for(int j = 0; j < cells[0].length; j++){
      switch(cells[i][j]){
        case 0:
          fill(0,0,0);
          break;
        case 1:
          fill(255,255,0);
          break;
        case 2:
          fill(255,0,255);
          break;
        case 3:
          fill(255,0,0);
          break;
        case 4:
          fill(0, 255, 255);
          break;
        case 5:
          fill(20, 255, 0);
          break;
      }
      stroke(0);
      rect(i*(displayHeight/100),j*(displayHeight/100),displayHeight/100,displayHeight/100);
    }
  }
}
Ant ant = new Ant();
int[][] field = new int[100][100];
void draw(){
  int pos = field[ant.x%100][ant.y%100];
  if(pos == 1 || pos==0 || pos == 4 || pos == 5)
    ant.dir = (ant.dir+5)%4;
  else
    ant.dir = (ant.dir+3)%4;
  ant.step();
  field[ant.x%100][ant.y%100]++;
  field[ant.x%100][ant.y%100] %= 6;
  rdraw(field);
}
