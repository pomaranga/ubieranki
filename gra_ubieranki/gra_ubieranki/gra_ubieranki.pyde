PImage backgroundImg;
PImage characterImg;
PImage dressImg;
PImage shoesImg;
PImage hairImg;

int characterX, characterY;
int hairX, hairY;
int dressX, dressY;
int shoesX, shoesY;

void setup() {
  size(800, 600);
  
  // Wczytaj obrazy
  backgroundImg = loadImage("background.jpg");
  dressImg = loadImage("dress.PNG");
  shoesImg = loadImage("shoes.PNG");
  hairImg = loadImage("hair.PNG");
  }

#Patrycja Leśniak (linijki odpowiadające za kursor)    
def draw(): #ta funkcja odpowiada za kursor
    if mousePressed:
        cursor(HAND)
    else: 
        cursor(ARROW)
