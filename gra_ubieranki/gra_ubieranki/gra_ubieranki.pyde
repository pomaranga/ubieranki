#Anhelina Hlushanok
class Item: #klasa dla rzeczy w szafie
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
class Wardrobe: #klasa dla szafy 
    def __init__(self):
        self.items = []
        
    def add_items(self, item): #funkcja zeby dodac rzeczy do szafy
        self.items.append(item) 

class Character(): #klasa postaci
    def __init__(self,name):
        self.name = name

class Character():
    def __init__(self,x,y):
        self.rect.x = x
        self.rect.y = y

def menu_start():
    global start, quit, starthover, quithover
    image(start,100,300) #B.Rząd
    image(quit,650,300) #B.Rząd
    if(mouseX > 100 and mouseX < 535 and mouseY > 310 and mouseY < 492):
        image(starthover,100,300)
    if(mouseX > 665 and mouseX < 1100 and mouseY > 310 and mouseY < 492):
        image(quithover,650,300)
    if(mousePressed and mouseX > 665 and mouseX < 1100 and mouseY > 310 and mouseY < 492):
        clear()
        exit()










hat_selected = False
dress_selected = False
shoes_selected = False 

def nazwij_postac():
# Możliwość nazwania postaci (Joanna Baran)
    name_character = input(u"Wpisz nazwę postaci: ")
    if name_character:
        print(u"Miło mi Cię poznać, jestem:", name_character)
    else:
        print(u"Nie wpisano nazwy postaci.")



# Przesunięcie wybranych elementów ubioru za pomocą myszy
if hat_selected:
        hair_x = mouse_x - hair_img.get_width() // 2
        hair_y = mouse_y - hair_img.get_height() // 2
if dress_selected:
        dress_x = mouse_x - dress_img.get_width() // 2
        dress_y = mouse_y - dress_img.get_height() // 2
if shoes_selected:
        shoes_x = mouse_x - shoes_img.get_width() // 2
        shoes_y = mouse_y - shoes_img.get_height() // 2



def setup():
    global webImg, start, quit, starthover, quithover, wyjscieImg, resetImg, characterImg, dressImg, hairImg, hair2Img, shoesImg, spodnicaniebieskaImg, bluzkarozowaImg, klapkirozoweImg, wlosyblondImg
    size(1200,800)
    textSize(50) 
    #img = loadImage('C:/Users/user_x/Desktop/ubierani/ubieranki/postasc.hair2.PNG')
    url = 'https://kartinki.pibig.info/uploads/posts/2023-04/1682411811_kartinki-pibig-info-p-garderobnaya-kartinki-arti-instagram-2.jpg'
    webImg = loadImage(url, "jpg")
    start = loadImage("star_img.png") #B.Rząd
    quit = loadImage("quit_img.png") #B.Rząd
    starthover = loadImage("star_hover_img.png") #B.Rząd
    quithover = loadImage("quit_hover_img.png") #B.Rząd
    wyjscieImg = loadImage("exit.png")  #Wladiskowacz
    resetImg = loadImage("reset.png")  #Wladiskowacz
    characterImg = loadImage("character.PNG")  #Wladiskowacz
    dressImg = loadImage("dress.PNG")  #Wladiskowacz
    hairImg = loadImage("hair.PNG")  #Wladiskowacz
    hair2Img = loadImage("hair2.PNG")  #Wladiskowacz
    shoesImg = loadImage("shoes.PNG")  #Wladiskowacz
    spodnicaniebieskaImg = loadImage("spodnicaniebieskaImg.png")
    bluzkarozowaImg = loadImage("bluzkarozowaImg.png")
    klapkirozoweImg = loadImage("klapkirozoweImg.png")
    wlosyblondImg = loadImage("wlosyblondImg.png")
    
def draw():
    if mousePressed: #ta konstrukcja odpowiada za kursor (Patrycja Leśniak)
        cursor(HAND)
    else: 
        cursor(ARROW)
        background(0)
        image(webImg,0,0)
    menu_start()
    background(0)
    image(webImg,0,0)
    fill(30,30,30, 200)
    rect(20, 100, 300, 600, 10)

    fill(255,255,255)

  
    text("hat", width//2-500, height//2-200, 40)   
    text("dress", width//2-500, height//2-150, 80)
    text("Hair", width//2-500, height//2-100, 80)  #Wladiskowacz
    text("Hair_2", width//2-500, height//2-50, 80)  #Wladiskowacz
    text("Shoes", width//2-500, height//2-0, 80)  #Wladiskowacz
    image(wyjscieImg, 10, 10, 120, 60)  #Wladiskowacz
    image(resetImg, 135, 5, 130, 70)  #Wladiskowacz
    image(characterImg, 600, 200, 150, 430)  #Wladiskowacz
    image(dressImg, 600, 200, 150, 450)  #Wladiskowacz
    image(hairImg, -200, 200, 150, 450)  #Wladiskowacz
    image(hair2Img, 600, 200, 150, 450)  #Wladiskowacz
    image(shoesImg, 600, 180, 150, 450)  #Wladiskowacz
    image(spodnicaniebieskaImg, 250, 180, 150, 450) #Patrycja Leśniak
    image(bluzkarozowaImg, 250, 160, 150, 450) #Patrycja Leśniak
    image(klapkirozoweImg, 250, 140, 150, 450) #Patrycja Leśniak
    image(wlosyblondImg, 250, 100, 150, 450) #Patrycja Leśniak

def mouseClicked():  #Wladiskowacz (prawdopodobnie po kliknięciu przycisku „sukienka” pojawia się na ekranie(dodac))
    global reset
    if mouseX > 137 and mouseX < 260 and mouseY > 5 and mouseY < 75:
        reset()
    if mouseX > 5 and mouseX < 130 and mouseY > 5 and mouseY < 75:
        exit()

def reset():  #Wladiskowacz (prawdopodobnie po kliknięciu znika z ekranu)
 global x, y
    imageMode(CENTER)
    image(dressImg, -200, -200) #Nie dziala :(
    

    
 #   Hair.x = -100
 #   Hair.y = -100
    
 #   Hair2.x = -100
 #   Hair2.y = -100

#    Shoes.x = -100
#    Shoes.y = -100
