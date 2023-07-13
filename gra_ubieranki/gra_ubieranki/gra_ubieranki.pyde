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

class Character(): #klasa postaci #Baran
    def __init__(self,name):
        self.name = name

class Character():
    def __init__(self,x,y):
        self.rect.x = x
        self.rect.y = y

class RzeciRuszanie:
    def __init__(self, image_path, x, y):
        self.image = loadImage(image_path)
        self.x = x
        self.y = y
        self.is_dragging = False
        self.mouse_offset = PVector(0, 0)
        self.scale_factor = 0.8

    def display(self):
        pushMatrix()
        translate(self.x, self.y)
        scale(self.scale_factor)
        image(self.image, 0, 0)
        popMatrix()

    def check_mouse_over(self):
        if (
            mouseX > self.x
            and mouseX < self.x + self.image.width * self.scale_factor
            and mouseY > self.y
            and mouseY < self.y + self.image.height * self.scale_factor
        ):
            return True
        return False

    def mouse_pressed(self):
        if self.check_mouse_over():
            self.is_dragging = True
            self.mouse_offset.x = self.x - mouseX
            self.mouse_offset.y = self.y - mouseY

    def mouse_released(self):
        self.is_dragging = False

    def mouse_dragged(self):
        if self.is_dragging:
            self.x = mouseX + self.mouse_offset.x
            self.y = mouseY + self.mouse_offset.y



def menu_start():
    global start, quit, starthover, quithover
    image(start,100,300) #B.Rząd
    image(quit,650,300) #B.Rząd










hat_selected = False
dress_selected = False
shoes_selected = False 


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
    global webImg,wlosybrazImg, start,flaga_wlosy, quit, starthover, quithover, wyjscieImg, resetImg, characterImg, dress, dress_x, dress_y, is_dragging, mouse_offsetdress, mouse_offsethair, hair, hair_x, hair_y, hair2, shoes, spodnicaniebieskaImg, bluzkarozowaImg, klapkirozoweImg, wlosyblondImg, wlosyczarne, sukienkaczarna, koszulkaczarna, sukienkamagenta,barImg,button_dressImg,button_heelsImg,button_haircolorImg,dress_shadowImg,heels_shadowImg,haircolor_shadowImg,skirt_shadow,skirt,b_dress,b_wlosy,b_heels,b_skirt,bluzkaniebieskaImg,bluzkazielonaImg,spodnicabrazowaImg,spodnicaczerwonaImg,spodnicafioletowaImg,spodnicazielonaImg,klapkirfioletoweImg,klapkizieloneImg,hair3,hair4,hair5,hair6,hair7
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
    dress = RzeciRuszanie("dress.PNG", 600, 200)
    hair = RzeciRuszanie("hair.PNG", -200, 200)
    hair2 = RzeciRuszanie("hair2.PNG", 600, 200)
    shoes = RzeciRuszanie("shoes.PNG", 600, 180)
    mouse_offsethair = PVector(0, 0) #Pshenychniak
    hair2Img = loadImage("hair2.PNG")  #Wladiskowacz
    shoesImg = loadImage("shoes.PNG")  #Wladiskowacz
    spodnicaniebieskaImg = loadImage("spodnicaniebieskaImg.png") #Patrycja Leśniak
    bluzkarozowaImg = loadImage("bluzkarozowaImg.png") #Patrycja Leśniak
    klapkirozoweImg = loadImage("klapkirozoweImg.png") #Patrycja Leśniak
    #wlosyblondImg = loadImage("wlosyblondImg.png") #Patrycja Leśniak
    wlosyczarne = RzeciRuszanie("wlosy_czarne.png", 600, 200) #Kornecka
    koszulkaczarna = RzeciRuszanie("koszulka_czarna.png", 600, 200) #Kornecka
    sukienkaczarna = RzeciRuszanie("sukienka_czarna.png", 600, 200) #Kornecka
    sukienkamagenta = RzeciRuszanie("sukienka_magenta.png", 600, 200) #Kornecka
    
    
    barImg = loadImage("rectangle.png") #Zadorozhnyi
    button_dressImg = loadImage("dress1.png") #Zadorozhnyi
    button_heelsImg = loadImage("heels.png") #Zadorozhnyi
    button_haircolorImg = loadImage("haircolor.png") #Zadorozhnyi
    dress_shadowImg = loadImage("dress_shadow.png") #Zadorozhnyi
    heels_shadowImg = loadImage("heels_shadow.png") #Zadorozhnyi
    haircolor_shadowImg = loadImage("haircolor_shadow.png") #Zadorozhnyi
    skirt_shadow = loadImage("skirt_shadow.png") #Zadorozhnyi
    skirt = loadImage("skirt.png")#Zadorozhnyi
    bluzkaniebieskaImg = loadImage("bluzkaniebieskaImg.png")
    bluzkazielonaImg = loadImage("bluzkazielonaImg.png")
    spodnicabrazowaImg = loadImage("spodnicabrazowaImg.png")
    spodnicaczerwonaImg = loadImage("spodnicaczerwonaImg.png")
    spodnicafioletowaImg = loadImage("spodnicafioletowaImg.png")
    spodnicazielonaImg = loadImage("spodnicazielonaImg.png")
    klapkirfioletoweImg = loadImage("klapkirfioletoweImg.png")
    klapkizieloneImg = loadImage("klapkizieloneImg.png")
    hair3 = loadImage("hair3.png")
    hair4 = loadImage("hair4.png")
    hair5 = loadImage("hair5.png")
    hair6 = loadImage("hair6.png")
    hair7 = loadImage("hair7.png")

    
   
   
   
    wlosyblondImg = loadImage("wlosyblondImg.png")
    wlosybrazImg =  loadImage("wlosybrazImg.png")
    

    flaga_wlosy = True 
    b_heels = 0
    b_skirt = 0
    b_dress = 0
    b_wlosy = 0
    
    

    
    
    
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

    dress.display()
    hair.display()
    hair2.display()
    shoes.display()
    wlosyczarne.display()
    koszulkaczarna.display()
    sukienkaczarna.display()
    sukienkamagenta.display()


    
    if b_wlosy == 0:
        image(hair3,600,200,150,450)
    elif b_wlosy == 2:
        image(hair4,600,200,150,450)
    elif b_wlosy == 3:
        image(hair5,600,200,150,450)
    elif b_wlosy == 4:
        image(hair6,600,200,150,450)
    elif b_wlosy == 5:
        image(hair7,600,200,150,450)

    
    if b_skirt == 0:
        image(spodnicaniebieskaImg, 600, 196, 150, 450) #Patrycja Leśniak
    elif b_skirt == 1:
        image(spodnicabrazowaImg,600,196,150,450)
    elif b_skirt == 2:
        image(spodnicaczerwonaImg,600,196,150,450)
    elif b_skirt == 3:
        image(spodnicafioletowaImg,600,196,150,450)
    elif b_skirt == 4:
        image(spodnicazielonaImg,600,196,150,450)
        
    if b_dress == 0:
        image(bluzkarozowaImg, 600, 196, 150, 450) #Patrycja Leśniak
    elif b_dress == 1:
        image(bluzkaniebieskaImg, 600, 196, 150, 450)
    elif b_dress == 2:
        image(bluzkazielonaImg, 600, 196, 150, 450)
    
    
    
    
    
    if b_heels == 0:
        image(klapkirozoweImg, 600, 182, 150, 450) #Patrycja Leśniak
    elif b_heels == 1:
        image(klapkirfioletoweImg, 600, 182, 150, 450)
    elif b_heels == 2:
        image(klapkizieloneImg, 600, 182, 150, 450)
        
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
    
    
    
    
    
    

    if b_skirt % 2 == 0:
        image(skirt_shadow, 750,696)
    else:
        image(skirt,750,696)
        
    if b_heels % 2 == 0:
        image(heels_shadowImg,525,696)
    else:
        image(button_heelsImg,525,696)

    if b_dress % 2 == 0:
        image(dress_shadowImg, 410, 696)
    else:
        image(button_dressImg, 410, 696)
        
    if b_wlosy % 2 == 0:
        image(haircolor_shadowImg,635,696)
    else:
        image(button_haircolorImg, 635, 696)
    
    if flaga_wlosy:
        image(wlosyblondImg, 250, 100, 150, 450)
    else:
        image(wlosybrazImg,250, 100, 150, 450)
        
        
        
        
        
def mouseClicked():  #Wladiskowacz (prawdopodobnie po kliknięciu przycisku „sukienka” pojawia się na ekranie(dodac))
    global, flaga_wlosy, b_dress, b_wlosy, b_heels,b_skirt
    if mouseX > 137 and mouseX < 260 and mouseY > 5 and mouseY < 75:
        setup()  # nie ma potrzeby pisać funkcji reset, bo zawołanie setup da ten sam efekt
    if mouseX > 5 and mouseX < 130 and mouseY > 5 and mouseY < 75:
        exit()
    if mouseX < 300 and mouseY<300 :   #alex
      flaga_wlosy =  not flaga_wlosy
      
    if mouseX > 400 and mouseX < 500  and mouseY > 680 and mouseY < 1100:
        b_dress = b_dress +1
        if b_dress == 3:
            b_dress = 0
        
    if mouseX > 635 and mouseX < 730  and mouseY > 680 and mouseY < 1100:
        b_wlosy = b_wlosy +1
        if b_wlosy == 5:
            b_wlosy = 0
        
    if mouseX > 525 and mouseX < 620  and mouseY > 680 and mouseY < 1100:
        b_heels = b_heels + 1
        if b_heels == 3:
            b_heels = 0
        
    if mouseX > 755 and mouseX < 875  and mouseY > 680 and mouseY < 1100:
        #b_skirt = not b_skirt
        b_skirt = b_skirt + 1
        if b_skirt == 5:
            b_skirt = 0

def mousePressed():
    for rzecz in [dress, hair, hair2, shoes, wlosyczarne, koszulkaczarna, sukienkaczarna, sukienkamagenta]:
        rzecz.mouse_pressed()
        if rzecz.is_dragging:
            break


def mouseReleased():
    for rzecz in [dress, hair, hair2, shoes, wlosyczarne, koszulkaczarna, sukienkaczarna, sukienkamagenta]:
        rzecz.mouse_released()


def mouseDragged():
    for rzecz in [dress, hair, hair2, shoes, wlosyczarne, koszulkaczarna, sukienkaczarna, sukienkamagenta]:
        rzecz.mouse_dragged()
        
        
def keyPressed():
    if key == 'r':
        dress.x = width / 2 - dress.image.width * dress.scale_factor / 2
        dress.y = height / 2 - dress.image.height * dress.scale_factor / 2
        hair.x = width / 2 - hair.image.width * hair.scale_factor / 2
        hair.y = height / 2 - hair.image.height * hair.scale_factor / 2
        hair2.x = width / 2 - hair2.image.width * hair2.scale_factor / 2
        hair2.y = height / 2 - hair2.image.height * hair2.scale_factor / 2
        shoes.x = width / 2 - shoes.image.width * shoes.scale_factor / 2
        shoes.y = height / 2 - shoes.image.height * shoes.scale_factor / 2
        wlosyczarne.x = width / 2 - dress.image.width * dress.scale_factor / 2
        wlosyczarne.y = height / 2 - dress.image.height * dress.scale_factor / 2
        koszulkaczarna.x = width / 2 - dress.image.width * dress.scale_factor / 2
        koszulkaczarna.y = height / 2 - dress.image.height * dress.scale_factor / 2
        sukienkaczarna.x = width / 2 - dress.image.width * dress.scale_factor / 2
        sukienkaczarna.y = height / 2 - dress.image.height * dress.scale_factor / 2
        sukienkamagenta.x = width / 2 - dress.image.width * dress.scale_factor / 2
        sukienkamagenta.y = height / 2 - dress.image.height * dress.scale_factor / 2
      
