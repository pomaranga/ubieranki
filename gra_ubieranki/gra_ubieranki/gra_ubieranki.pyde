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
    global webImg,wlosybrazImg, start,flaga_wlosy, quit, starthover, quithover, wyjscieImg, resetImg, characterImg, dress, dress_x, dress_y, is_dragging, mouse_offsetdress, mouse_offsethair, hair, hair_x, hair_y, hair2Img, shoesImg, spodnicaniebieskaImg, bluzkarozowaImg, klapkirozoweImg, wlosyblondImg, wlosyczarne, sukienkaczarna, koszulkaczarna, sukienkamagenta,barImg,button_dressImg,button_heelsImg,button_haircolorImg,dress_shadowImg,heels_shadowImg,haircolor_shadowImg,skirt_shadow,skirt,b_dress,b_wlosy,b_heels,b_skirt
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
    dress = loadImage("dress.PNG")
    dress_x = width / 2 - dress.width / 2
    dress_y = height / 2 - dress.height / 2
    is_dragging = False
    mouse_offsetdress = PVector(0, 0)  #Wladiskowacz
    hair = loadImage("hair.PNG")  
    hair_x = width / 2 - hair.width / 2
    hair_y = height / 2 - hair.height / 2
    is_dragging2 = False 
    mouse_offsethair = PVector(0, 0) #Pshenychniak
    hairImg = loadImage("hair.PNG")  #Wladiskowacz
    hair2Img = loadImage("hair2.PNG")  #Wladiskowacz
    shoesImg = loadImage("shoes.PNG")  #Wladiskowacz
    spodnicaniebieskaImg = loadImage("spodnicaniebieskaImg.png") #Patrycja Leśniak
    bluzkarozowaImg = loadImage("bluzkarozowaImg.png") #Patrycja Leśniak
    klapkirozoweImg = loadImage("klapkirozoweImg.png") #Patrycja Leśniak
    #wlosyblondImg = loadImage("wlosyblondImg.png") #Patrycja Leśniak
    wlosyczarne = loadImage("wlosy_czarne.png") #Kornecka
    koszulkaczarna = loadImage("koszulka_czarna.png") #Kornecka
    sukienkaczarna = loadImage("sukienka_czarna.png") #Kornecka
    sukienkamagenta = loadImage("sukienka_magenta.png") #Kornecka
    
    
    barImg = loadImage("rectangle.png") #Zadorozhnyi
    button_dressImg = loadImage("dress1.png") #Zadorozhnyi
    button_heelsImg = loadImage("heels.png") #Zadorozhnyi
    button_haircolorImg = loadImage("haircolor.png") #Zadorozhnyi
    dress_shadowImg = loadImage("dress_shadow.png") #Zadorozhnyi
    heels_shadowImg = loadImage("heels_shadow.png") #Zadorozhnyi
    haircolor_shadowImg = loadImage("haircolor_shadow.png") #Zadorozhnyi
    skirt_shadow = loadImage("skirt_shadow.png") #Zadorozhnyi
    skirt = loadImage("skirt.png")#Zadorozhnyi
   
   
   
    wlosyblondImg = loadImage("wlosyblondImg.png")
    wlosybrazImg =  loadImage("wlosybrazImg.png")
    
    b_dress = True
    b_wlosy = True
    flaga_wlosy = True 
    b_heels = True
    b_skirt = True
    
    

    
    
    
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
    #image(wlosyczarne, -150, -400) #Kornecka
    image(koszulkaczarna, -140, -250) #Kornecka
    image(sukienkaczarna, 600, -400) #Kornecka
    image(sukienkamagenta, 460, -100) #Kornecka
    fill(30,30,30, 200)
    rect(20, 100, 300, 600, 10)    
    fill(400,400,400, 400)
    rect(600, 200, 150, 450, 10)

    fill(255,255,255)

  
    text("hat", width//2-500, height//2-200, 40)   
    text("dress", width//2-500, height//2-150, 80)
    text("hair", width//2-500, height//2-150, 80)  #Vitalii Pshenychniak
    text("Hair_2", width//2-500, height//2-50, 80)  #Wladiskowacz
    text("Shoes", width//2-500, height//2-0, 80)  #Wladiskowacz
    image(wyjscieImg, 10, 10, 120, 60)  #Wladiskowacz
    image(resetImg, 135, 5, 130, 70)  #Wladiskowacz
    image(characterImg, 600, 200, 150, 430)  #Wladiskowacz
    image(dress, dress_x, dress_y)
    image(hair, hair_x, hair_y) #Pshenychniak
    image(hair2Img, 600, 200, 150, 450)  #Wladiskowacz
    image(shoesImg, 600, 180, 150, 450)  #Wladiskowacz
    image(spodnicaniebieskaImg, 600, 196, 150, 450) #Patrycja Leśniak
    image(bluzkarozowaImg, 600, 196, 150, 450) #Patrycja Leśniak
    image(klapkirozoweImg, 600, 182, 150, 450) #Patrycja Leśniak
    #image(wlosyblondImg, 250, 100, 150, 450) #Patrycja Leśniak
    image(barImg, 400,690) #Zadorozhnyi
    
    #image(button_dressImg,410,696) #Zadorozhnyi
    #image(dress_shadowImg,410,696) #Zadorozhnyi
    
    #image(heels_shadowImg,525,696) #Zadorozhnyi
    #image(button_heelsImg,525,696) #Zadorozhnyi
    
    #image(button_haircolorImg,635,696) #Zadorozhnyi
    #image(haircolor_shadowImg,635,696) #Zadorozhnyi

    #image(skirt_shadow, 750,696) #Zadorozhnyi
    #image(skirt,750,696) #Zadorozhnyi
    
    #image(button_dressImg, 410, 696) 
    #image(dress_shadowImg, 410, 696)

    if b_skirt:
        image(skirt_shadow, 750,696)
    else:
        image(skirt,750,696)
        
    if b_heels:
        image(heels_shadowImg,525,696)
    else:
        image(button_heelsImg,525,696)

    if b_dress:
        image(dress_shadowImg, 410, 696)
    else:
        image(button_dressImg, 410, 696)
        
    if b_wlosy:
        image(haircolor_shadowImg,635,696)
    else:
        image(button_haircolorImg, 635, 696)
    
    if flaga_wlosy:
        image(wlosyblondImg, 250, 100, 150, 450)
    else:
        image(wlosybrazImg,250, 100, 150, 450)
        
        
        
        
        
def mouseClicked():  #Wladiskowacz (prawdopodobnie po kliknięciu przycisku „sukienka” pojawia się na ekranie(dodac))
    global reset, flaga_wlosy, b_dress, b_wlosy, b_heels,b_skirt
    if mouseX > 137 and mouseX < 260 and mouseY > 5 and mouseY < 75:
        reset()
    if mouseX > 5 and mouseX < 130 and mouseY > 5 and mouseY < 75:
        exit()
    if mouseX < 300 and mouseY<300 :   #alex
      flaga_wlosy =  not flaga_wlosy
    if mouseX > 400 and mouseX < 500  and mouseY > 680 and mouseY < 1100:
        b_dress = not b_dress
    if mouseX > 635 and mouseX < 730  and mouseY > 680 and mouseY < 1100:
        b_wlosy = not b_wlosy
    if mouseX > 525 and mouseX < 620  and mouseY > 680 and mouseY < 1100:
        b_heels = not b_heels
    if mouseX > 755 and mouseX < 875  and mouseY > 680 and mouseY < 1100:
        b_skirt = not b_skirt


def mousePressed():
    global is_dragging, is_dragging2, mouse_offsetdress, mouse_offsethair
    if dress_x <= mouseX <= dress_x + dress.width and dress_y <= mouseY <= dress_y + dress.height:
        is_dragging = True
        mouse_offsetdress.x = dress_x - mouseX
        mouse_offsetdress.y = dress_y - mouseY
    if hair_x <= mouseX <= hair_x + hair.width and hair_y <= mouseY <= hair_y + hair.height:
        is_dragging2 = True
        mouse_offsethair.x = hair_x - mouseX
        mouse_offsethair.y = hair_y - mouseY

        
        
def mouseReleased():
    global is_dragging, is_dragging2
    is_dragging = False
    is_dragging2 = False

def mouseDragged():
    global dress_x, dress_y, hair_x, hair_y
    if is_dragging:
        dress_x = mouseX + mouse_offsetdress.x
        dress_y = mouseY + mouse_offsetdress.y
    if is_dragging2:
        hair_x = mouseX + mouse_offsethair.x
        hair_y = mouseY + mouse_offsethair.y
      


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
