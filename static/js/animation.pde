ArrayList poop;
color[] palette = { 
  #42d1f4, #a142f4, #50217a, #213e7a, #f74a33, #f2eccd
}; 
int distance =50;
boolean flag=true;
void setup()
{
  size(500, 500);
  smooth();
  poop = new ArrayList();
  for (int i=0;i<120;i++) {
    PVector PD = new PVector(random(-150, 150), random(-150, 150));
    Dots D = new Dots(PD);
    poop.add(D);
  }
}

void draw()
{
  background(255);
  translate(width/2, height/2);
  pushStyle();

  popStyle();
  //----------------
  for (int i=0;i<poop.size();i++) {
    Dots dots1 = (Dots) poop.get(i);
    dots1.display();
    dots1.update();
    for (int j=i+1;j<poop.size();j++) {
      Dots dots2 = (Dots) poop.get(j);
      dots2.update();
      if (dist(dots1.location.x, dots1.location.y, dots2.location.x, dots2.location.y)<distance) {
        for (int k=j+1;k<poop.size();k++) {
          Dots dots3 = (Dots) poop.get(k);
          dots3.update();
          if (flag) {
            fill(palette[dots3.c], 50);
            noStroke();
          }
          else
          {
            noFill();
            stroke(255,50);
          }
          if (dist(dots3.location.x, dots3.location.y, dots2.location.x, dots2.location.y)<distance) {
            beginShape();
            vertex(dots3.location.x, dots3.location.y);
            vertex(dots2.location.x, dots2.location.y);
            vertex(dots1.location.x, dots1.location.y);
            endShape();
          }
        }
      }
    }
  }
  //----------------
}
class Dots {
  PVector location;
  PVector velocity;
  int c;
  int radius=200;
  Dots(PVector _PV)
  {
    location = _PV;
    c = (int) random(palette.length);
    float xt = random(-0.003, 0.003);
    float yt = random(-0.003, 0.003);
    velocity = new PVector(xt, yt );
  }

  void display()
  {
    fill(palette[c]);
    noStroke();
    ellipse(location.x, location.y, 2, 2);
  }
  void update()
  {
    if (dist(location.x, location.y, 0, 0)>radius) {
      velocity.mult(-1);
      location.add(velocity);
    }
    else {
      location.add(velocity);
    }
  }
}
