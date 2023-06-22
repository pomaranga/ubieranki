PImage backgroundImg;
PImage hatImg;
PImage dressImg;
PImage shoesImg;

void setup() {
  size(800, 600);
  
  // Wczytaj obrazy
  backgroundImg = loadImage("background.jpg");
  hatImg = loadImage("hat.png");
  dressImg = loadImage("dress.png");
  shoesImg = loadImage("shoes.png");
}

#Patrycja Leśniak (linijki odpowiadające za kursor)    
def draw(): #ta funkcja odpowiada za kursor
    if mousePressed:
        cursor(HAND)
    else: 
        cursor(ARROW)
