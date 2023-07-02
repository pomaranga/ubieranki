class Clothes: #class for elements of clothes; that class was originally created by Anhelina Hlushanok
    def __init__(self, name, file_path, x, y):
        self.name = name
        self.file_path = file_path
        self.x = x
        self.y = y
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)


class Hair(Clothes): #subclass for elements of hairstyles
    def __init__(self, name, file_path, x, y):
        Clothes.__init__(self, name, file_path, x, y) #command 'super().' doesn't work
        
    def load_image(self, file_path):
        Clothes.load_image(self, file_path)
         
                                   
class Torso(Clothes): #subclass for elements of upper body clothes
    def __init__(self, name, file_path, x, y):
        Clothes.__init__(self, name, file_path, x, y)
        
    def load_image(self, file_path):
        Clothes.load_image(self, file_path)
    
    
class Legs(Clothes): #subclass for elements of lower body clothes
    def __init__(self, name, file_path, x, y):
        Clothes.__init__(self, name, file_path, x, y)
        
    def load_image(self, file_path):
        Clothes.load_image(self, file_path)
    
    
class Footwear(Clothes): #subclass for elements of footwear
    def __init__(self, name, file_path, x, y):
        Clothes.__init__(self, name, file_path, x, y)
    
    def load_image(self, file_path):
        Clothes.load_image(self, file_path)


class Dress(Clothes): #subclass for elements of full body clothes
    def __init__(self, name, file_path, x, y):
        Clothes.__init__(self, name, file_path, x, y)
        
        
        
class Interface: #class for interface elements
    def __init__(self, name,  file_path, x, y):
        self.name = name
        self.file_path = file_path
        self.x = x
        self.y = y
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
    
    
class Button(Interface): #subclass for buttoms
    def __init__(self, name, file_path, x, y, size_x, size_y):
        Interface.__init__(self, name, file_path, x, y)
        self.size_x = size_x
        self.size_y = size_y
        
    def load_image(self, file_path):
        Interface.load_image(self, file_path)


hair_1 = Hair("hair_1", "data/Hair/hair_1.png", 1500, 200)
hair_2 = Hair("hair_2", "data/Hair/hair_2.png", 1500, 200)
wlosy_blond = Hair("wlosy_blond", "data/Hair/wlosy_blond.png", 1500, 200)
wlosy_brazowe = Hair("wlosy_brazowe", "data/Hair/wlosy_brazowe.png", 1500, 200)
wlosy_czarne_1 = Hair("wlosy_czarne_1", "data/Hair/wlosy_czarne_1.png", 1500, 200)
wlosy_czarne_2 = Hair("wlosy_czarne_2", "data/Hair/wlosy_czarne_2.png", 1500, 200)


bluzka_niebieska = Torso("bluzka_niebieska", "data/Torso/bluzka_niebieska.png", 1500, 200)
bluzka_rozowa = Torso("bluzka_rozowa", "data/Torso/bluzka_rozowa.png", 1500, 200)
bluzka_zielona = Torso("bluzka_zielona", "data/Torso/bluzka_zielona.png", 1500, 200)
koszulka_czarna = Torso("koszulka_czarna", "data/Torso/koszulka_czarna.png", 1500, 200)


spodnica_brazowa = Legs("spodnica_brazowa", "data/Legs/spodnica_brazowa.png", 1500, 200)
spodnica_czerwona = Legs("spodnica_czerwona", "data/Legs/spodnica_czerwona.png", 1500, 200)
spodnica_fioletowa = Legs("spodnica_fioletowa", "data/Legs/spodnica_fioletowa.png", 1500, 200)
spodnica_niebieska = Legs("spodnica_niebieska", "data/Legs/spodnica_niebieska.png", 1500, 200)
spodnica_zielona = Legs("spodnica_zielona", "data/Legs/spodnica_zielona.png", 1500, 200)


black_shoes = Footwear("black_shoes", "data/Footwear/black_shoes.png", 1500, 200)
klapki_fioletowe = Footwear("klapki_fioletowe", "data/Footwear/klapki_fioletowe.png", 1500, 200)
klapki_rozowe = Footwear("klapki_rozowe", "data/Footwear/klapki_rozowe.png", 1500, 200)
klapki_zielone = Footwear("klapki_fioletowe", "data/Footwear/klapki_fioletowe.png", 1500, 200)


sukienka_czarna_1 = Dress("sukienka_czarna_1", "data/Dresses/sukienka_czarna_1.png", 1500, 200)
sukienka_czarna_2 = Dress("sukienka_czarna_2", "data/Dresses/sukienka_czarna_2.png", 1500, 200)
sukienka_magenta = Dress("sukienka_magenta", "data/Dresses/sukienka_magenta.png", 1500, 200)


background_image = Interface("background_image", "data/background_image.png", 0, 0)
character_image = Interface("character_image", "data/character.png", 600, 200)


exit_button = Button("exit_button", "data/Buttons/exit_button.png", 1155, 5, 80, 40)
reset_button = Button("reset_button", "data/Buttons/reset_button.png", 700, 625, 80, 40)

#quit_button = Button("quit_button", "data/Buttons/quit_button.png", x, y)
#quit_hover_button = Button("quit_hover_button", "data/Buttons/quit_hover_button.png", x, y)
#start_button = Button("start_button", "data/Buttons/start_button.png", x, y)
#start_hover_button = Button("start_hover_button", "data/Buttons/start_hover_button.png", x, y)
                     
                     
# class Wardrobe: #klasa dla szafy 
#     def __init__(self):
#         self.items = []
        
#     def add_items(self, item): #funkcja zeby dodac rzeczy do szafy
#         self.items.append(item) 

# class Character(): #klasa postaci
#     def __init__(self,name):
#         self.name = name

# class Character():
#     def __init__(self,x,y):
#         self.rect.x = x
#         self.rect.y = y

# def menu_start():
#     global start, quit, starthover, quithover
#     image(start,100,300) #B.Rząd
#     image(quit,650,300) #B.Rząd
#     if(mouseX > 100 and mouseX < 535 and mouseY > 310 and mouseY < 492):
#         image(starthover,100,300)
#     if(mouseX > 665 and mouseX < 1100 and mouseY > 310 and mouseY < 492):
#         image(quithover,650,300)
#     if(mousePressed and mouseX > 665 and mouseX < 1100 and mouseY > 310 and mouseY < 492):
#         clear()
#         exit()










hair_selected = False
torso_selected = False
legs_selected = False
footwear_selected = False
dress_selected = False


# Możliwość nazwania postaci (Joanna Baran)
# def nazwij_postac():
#     name_character = input(u"Wpisz nazwę postaci: ")
#     if name_character:
#         print(u"Miło mi Cię poznać, jestem:", name_character)
#     else:
#         print(u"Nie wpisano nazwy postaci.")



# Przesunięcie wybranych elementów ubioru za pomocą myszy
# if hair_selected:
#         hair.x = mouseX - hair_img.get_width() // 2
#         hair.y = mouseY - hair_img.get_height() // 2
# if dress_selected:
#         dress.x = mouseX - dress_img.get_width() // 2
#         dress.y = mouseY - dress_img.get_height() // 2
# if footwear_selected:
#         footwear.x = mouseX - shoes_img.get_width() // 2
#         footwear.y = mouseY - shoes_img.get_height() // 2



def setup():
    # global is_dragging, mouse_offsetdress, mouse_offsethair, flaga_wlosy
    size(1280, 720)
    textSize(40) 
    
    # start = loadImage("star_img.png") #B.Rząd
    # quit = loadImage("quit_img.png") #B.Rząd
    # starthover = loadImage("star_hover_img.png") #B.Rząd
    # quithover = loadImage("quit_hover_img.png") #B.Rząd
    
    background_image.load_image(background_image.file_path)
    character_image.load_image(character_image.file_path)  #Władysław Bacewicz
    
    exit_button.load_image(exit_button.file_path)  #Władysław Bacewicz
    reset_button.load_image(reset_button.file_path)  #Władysław Bacewicz
    
    hair_1.load_image(hair_1.file_path)
    hair_2.load_image(hair_2.file_path)  #Władysław Bacewicz
    wlosy_blond.load_image(wlosy_blond.file_path)  #Patrycja Leśniak
    wlosy_brazowe.load_image(wlosy_brazowe.file_path)
    wlosy_czarne_1.load_image(wlosy_czarne_1.file_path)
    wlosy_czarne_2.load_image(wlosy_czarne_2.file_path) #Julia Kornecka
    
    bluzka_niebieska.load_image(bluzka_niebieska.file_path)
    bluzka_rozowa.load_image(bluzka_rozowa.file_path) #Patrycja Leśniak
    bluzka_zielona.load_image(bluzka_zielona.file_path)
    koszulka_czarna.load_image(koszulka_czarna.file_path) #Julia Kornecka
    
    spodnica_brazowa.load_image(spodnica_brazowa.file_path)
    spodnica_czerwona.load_image(spodnica_czerwona.file_path)
    spodnica_fioletowa.load_image(spodnica_fioletowa.file_path)
    spodnica_niebieska.load_image(spodnica_niebieska.file_path) #Patrycja Leśniak
    spodnica_zielona.load_image(spodnica_zielona.file_path)
    
    black_shoes.load_image(black_shoes.file_path)  #Władysław Bacewicz
    klapki_fioletowe.load_image(klapki_fioletowe.file_path)
    klapki_rozowe.load_image(klapki_rozowe.file_path) #Patrycja Leśniak
    klapki_zielone.load_image(klapki_zielone.file_path)
    
    sukienka_czarna_1.load_image(sukienka_czarna_1.file_path)
    sukienka_czarna_2.load_image(sukienka_czarna_2.file_path) #Julia Kornecka
    sukienka_magenta.load_image(sukienka_magenta.file_path) #Julia Kornecka
    
    # dress_x = width / 2 - dress.width / 2 #it must be x coordinate of "sukienka_czarna_1"
    # dress_y = height / 2 - dress.height / 2 #it must be y coordinate of "sukienka_czarna_1"
    
    
    # is_dragging = False
    
    
    # mouse_offsetdress = PVector(0, 0)  #Wladiskowacz
    
    
     
     
    # hair_x = width / 2 - hair.width / 2 #it must be x coordinate of "hair_1"
    # hair_y = height / 2 - hair.height / 2 #it must be y coordinate of "hair_1"
    
    
    # is_dragging2 = False 
    
    
    # mouse_offsethair = PVector(0, 0) #Pshenychniak
    
    # flaga_wlosy = True #???
    
    
    
def draw():
    # if mousePressed: #ta konstrukcja odpowiada za kursor (Patrycja Leśniak)
    #     cursor(HAND)
    # else: 
    #     cursor(ARROW)
        # background(0)
        # image(background_image.img, 0, 0)
#     menu_start()
    background(0)
    image(background_image.img, backgroung_img.x, backgroung_img.y)
    #image(wlosyczarne, -150, -400) #Kornecka
    # image(koszulkaczarna, -140, -250) #Kornecka
    # image(sukienkaczarna, 600, -400) #Kornecka
    # image(sukienkamagenta, 460, -100) #Kornecka
   
    fill(30, 30, 30, 200)
    rect(20, 100, 300, 600, 10)    
    fill(400, 400, 400, 400)
    rect(600, 200, 150, 450, 10)

    fill(255,255,255)
    text("Hair", width//2-500, height//2-200, 40)   
    text("Torso", width//2-500, height//2-150, 80)
    text("Legs", width//2-500, height//2-100, 80)  #Vitalii Pshenychniak
    text("Footwear", width//2-500, height//2-50, 80)  #Wladiskowacz
    text("Dresses", width//2-500, height//2-0, 80)  #Wladiskowacz
    
    image(exit_button.img, exit_button.x, exit_button.y, exit_button.size_x, exit_button.size_y)  #Wladiskowacz
    image(reset_button.img, reset_button.x, reset_button.y, reset_button.size_x, reset_button.size_y)  #Wladiskowacz
    image(character_image.img, 600, 200)  #Wladiskowacz
    # image(dress, dress_x, dress_y)
    # image(hair, hair_x, hair_y) #Pshenychniak
    # image(hair2Img, 600, 200, 150, 450)  #Wladiskowacz
    # image(shoesImg, 600, 180, 150, 450)  #Wladiskowacz
    # image(spodnicaniebieskaImg, 250, 180, 150, 450) #Patrycja Leśniak
    # image(bluzkarozowaImg, 250, 160, 150, 450) #Patrycja Leśniak
    # image(klapkirozoweImg, 250, 140, 150, 450) #Patrycja Leśniak
    # image(wlosyblondImg, 250, 100, 150, 450) #Patrycja Leśniak
    
    # if flaga_wlosy:
    #     image(wlosyblondImg, 250, 100, 150, 450)
    # else:
    #     image(wlosybrazImg,250, 100, 150, 450)
        
        
   

# def mouseClicked():  #Wladiskowacz (prawdopodobnie po kliknięciu przycisku „sukienka” pojawia się na ekranie(dodac))
#     global reset, flaga_wlosy
#     if mouseX > 137 and mouseX < 260 and mouseY > 5 and mouseY < 75:
#         reset()
#     if mouseX > 5 and mouseX < 130 and mouseY > 5 and mouseY < 75:
#         exit()
#     if mouseX < 300 and mouseY<300 :   #alex
#       flaga_wlosy =  not flaga_wlosy

# def mousePressed():
#     global is_dragging, is_dragging2, mouse_offsetdress, mouse_offsethair
#     if dress_x <= mouseX <= dress_x + dress.width and dress_y <= mouseY <= dress_y + dress.height:
#         is_dragging = True
#         mouse_offsetdress.x = dress_x - mouseX
#         mouse_offsetdress.y = dress_y - mouseY
#     if hair_x <= mouseX <= hair_x + hair.width and hair_y <= mouseY <= hair_y + hair.height:
#         is_dragging2 = True
#         mouse_offsethair.x = hair_x - mouseX
#         mouse_offsethair.y = hair_y - mouseY

        
        
# def mouseReleased():
#     global is_dragging, is_dragging2
#     is_dragging = False
#     is_dragging2 = False

# def mouseDragged():
#     global dress_x, dress_y, hair_x, hair_y
#     if is_dragging:
#         dress_x = mouseX + mouse_offsetdress.x
#         dress_y = mouseY + mouse_offsetdress.y
#     if is_dragging2:
#         hair_x = mouseX + mouse_offsethair.x
#         hair_y = mouseY + mouse_offsethair.y
      


# def reset():  #Wladiskowacz (prawdopodobnie po kliknięciu znika z ekranu)
#     global x, y
#     imageMode(CENTER)
#     image(dressImg, -200, -200) #Nie dziala :(
    

    
 #   Hair.x = -100
 #   Hair.y = -100
    
 #   Hair2.x = -100
 #   Hair2.y = -100

#    Shoes.x = -100
#    Shoes.y = -100
