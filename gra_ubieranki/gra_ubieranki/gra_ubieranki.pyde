# I decided to create an abstract class
# for clothes items in our game,
# because of better orderliness of code.
#
# Moreover, clothes in real world are
# the abstract things themselves, so you need to
# specify what are you talking about exactly.
#
# And so a coder won't create any abstract
# clothes item, he/she needs to categorize
# particular item to it's class before
# use it in our code.


from abc import ABCMeta, abstractmethod
class Clothes(): #abstract class for elements of clothes; that class was originally created by Anhelina Hlushanok
    __metaclass__ = ABCMeta
    @abstractmethod      
    def load_image(self):
        super().__init__()


class Hair(Clothes): #subclass for elements of hairstyles
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
         
                                   
class Torso(Clothes): #subclass for elements of upper body clothes
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
    
    
class Legs(Clothes): #subclass for elements of lower body clothes
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
    
    
class Footwear(Clothes): #subclass for elements of footwear
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)


class Dress(Clothes): #subclass for elements of full body clothes
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
        
        
        
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


# def __init__(self, name, file_path):
#         self.name = name
#         self.file_path = file_path
#        
#     def load_image(self, file_path):
#         self.img = loadImage(file_path)

# In lines below
# I created objects withing
# existing classes/subclasses

hair_1 = Hair("hair_1", "data/Hair/hair_1.png")
hair_2 = Hair("hair_2", "data/Hair/hair_2.png")
wlosy_blond = Hair("wlosy_blond", "data/Hair/wlosy_blond.png")
wlosy_brazowe = Hair("wlosy_brazowe", "data/Hair/wlosy_brazowe.png")
wlosy_czarne_1 = Hair("wlosy_czarne_1", "data/Hair/wlosy_czarne_1.png")
wlosy_czarne_2 = Hair("wlosy_czarne_2", "data/Hair/wlosy_czarne_2.png")


bluzka_niebieska = Torso("bluzka_niebieska", "data/Torso/bluzka_niebieska.png")
bluzka_rozowa = Torso("bluzka_rozowa", "data/Torso/bluzka_rozowa.png")
bluzka_zielona = Torso("bluzka_zielona", "data/Torso/bluzka_zielona.png")
koszulka_czarna = Torso("koszulka_czarna", "data/Torso/koszulka_czarna.png")


spodnica_brazowa = Legs("spodnica_brazowa", "data/Legs/spodnica_brazowa.png")
spodnica_czerwona = Legs("spodnica_czerwona", "data/Legs/spodnica_czerwona.png")
spodnica_fioletowa = Legs("spodnica_fioletowa", "data/Legs/spodnica_fioletowa.png")
spodnica_niebieska = Legs("spodnica_niebieska", "data/Legs/spodnica_niebieska.png")
spodnica_zielona = Legs("spodnica_zielona", "data/Legs/spodnica_zielona.png")


black_shoes = Footwear("black_shoes", "data/Footwear/black_shoes.png")
klapki_fioletowe = Footwear("klapki_fioletowe", "data/Footwear/klapki_fioletowe.png")
klapki_rozowe = Footwear("klapki_rozowe", "data/Footwear/klapki_rozowe.png")
klapki_zielone = Footwear("klapki_fioletowe", "data/Footwear/klapki_fioletowe.png")


sukienka_czarna_1 = Dress("sukienka_czarna_1", "data/Dresses/sukienka_czarna_1.png")
sukienka_czarna_2 = Dress("sukienka_czarna_2", "data/Dresses/sukienka_czarna_2.png")
sukienka_magenta = Dress("sukienka_magenta", "data/Dresses/sukienka_magenta.png")


background_image = Interface("background_image", "data/background_image.png", 0, 0)
character_image = Interface("character_image", "data/character.png", 795, 75)


exit_button = Button("exit_button", "data/Buttons/exit_button.png", 1193, 7, 80, 40)
reset_button = Button("reset_button", "data/Buttons/reset_button.png", 945, 650, 80, 40)



# In following lines I wrote
# coordinates for clothes elements.
# I did not create them as class parameters
# because they'll be changing in future.

hair_1.x = 1500
hair_1.y = 200

hair_2.x = 1500
hair_2.y = 200

wlosy_blond.x = 1500
wlosy_blond.y = 200

wlosy_brazowe.x = 1500
wlosy_brazowe.y = 200

wlosy_czarne_1.x = 1500
wlosy_czarne_1.y = 200

wlosy_czarne_2.x = 1500
wlosy_czarne_2.y = 200

bluzka_niebieska.x = 1500
bluzka_niebieska.y = 200

bluzka_rozowa.x = 1500
bluzka_rozowa.y = 200

bluzka_zielona.x = 1500
bluzka_zielona.y = 200

koszulka_czarna.x = 1500
koszulka_czarna.y = 200

spodnica_brazowa.x = 1500
spodnica_brazowa.y = 200

spodnica_czerwona.x = 1500
spodnica_czerwona.y = 200

spodnica_fioletowa.x = 1500
spodnica_fioletowa.y = 200

spodnica_niebieska.x = 1500
spodnica_niebieska.y = 200

spodnica_zielona.x = 1500
spodnica_zielona.y = 200

black_shoes.x = 1500
black_shoes.y = 200

klapki_fioletowe.x = 1500
klapki_fioletowe.y = 200

klapki_rozowe.x = 1500
klapki_rozowe.y = 200

klapki_zielone.x = 1500
klapki_zielone.y = 200

sukienka_czarna_1.x = 1500
sukienka_czarna_1.y = 200

sukienka_czarna_2.x = 1500
sukienka_czarna_2.y = 200

sukienka_magenta.x = 1500
sukienka_magenta.y = 200


#quit_button = Button("quit_button", "data/Buttons/quit_button.png", x, y)                      #B. Rząd
#quit_hover_button = Button("quit_hover_button", "data/Buttons/quit_hover_button.png", x, y)    #B. Rząd
#start_button = Button("start_button", "data/Buttons/start_button.png", x, y)                   #B. Rząd
#start_hover_button = Button("start_hover_button", "data/Buttons/start_hover_button.png", x, y) #B. Rząd
                     
                     
# class Wardrobe: #klasa dla szafy
#     def __init__(self):
#         self.items = []
        
#     def add_items(self, item): #funkcja zeby dodac rzeczy do szafy
#         self.items.append(item) 

        
            

hair_selected = False
torso_selected = False
legs_selected = False
footwear_selected = False
dresses_selected = False

fill_1 = 255     # fill_1 variable colors the text "Hair"
fill_2 = 255     # fill_2 variable colors the text "Torso"
fill_3 = 255     # fill_3 variable colors the text "Legs"
fill_4 = 255     # fill_4 variable colors the text "Footwear"
fill_5 = 255     # fill_5 variable colors the text "Dresses"
 


        
        
        
        
        
        
        

# unfortunately,
# the 'input' command
# DOESN'T WORK
# in processing :(

# Możliwość nazwania postaci (Joanna Baran)
# def nazwij_postac():
#     character_name = input(u"Wpisz nazwę postaci: ")
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
    # global #is_dragging, mouse_offsetdress, mouse_offsethair
    size(1280, 720)
        
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
    
    
    
    
    # is_dragging = False
    # mouse_offsetdress = PVector(0, 0)  #Wladiskowacz
    # is_dragging2 = False     
    # mouse_offsethair = PVector(0, 0) #Pshenychniak
    
    
    
def draw():
    background(background_image.img)
    image(character_image.img, character_image.x, character_image.y)
    
    
    fill(30, 30, 30, 200)
    rect(20, 65, 300, 600, 10)
    
    text_color()
    textSize(40)
    
    fill(fill_1, 255, fill_1)
    text("Hair", width//2-550, height//2-200)
    
    fill(fill_2, 255, fill_2)
    text("Torso", width//2-550, height//2-130)
    
    fill(fill_3, 255, fill_3)
    text("Legs", width//2-550, height//2-60) #Vitalii Pshenychniak
    
    fill(fill_4, 255, fill_4)
    text("Footwear", width//2-550, height//2+10) #Władysław Bacewicz
    
    fill(fill_5, 255, fill_5)
    text("Dresses", width//2-550, height//2+80) #Władysław Bacewicz
    
    
    
    image(exit_button.img, exit_button.x, exit_button.y, exit_button.size_x, exit_button.size_y)  #Wladiskowacz
    image(reset_button.img, reset_button.x, reset_button.y, reset_button.size_x, reset_button.size_y)  #Wladiskowacz
    
    image(hair_1.img, hair_1.x, hair_1.y) #Vitalii Pshenychniak
    image(hair_2.img, hair_2.x, hair_2.y) #Władysław Bacewicz
    image(wlosy_blond.img, wlosy_blond.x, wlosy_blond.y) #Patrycja Leśniak
    image(wlosy_brazowe.img, wlosy_brazowe.x, wlosy_brazowe.y)
    image(wlosy_czarne_1.img, wlosy_czarne_1.x, wlosy_czarne_1.y)
    image(wlosy_czarne_2.img, wlosy_czarne_2.x, wlosy_czarne_2.y) #Julia Kornecka
    
    image(bluzka_niebieska.img, bluzka_niebieska.x, bluzka_niebieska.y)
    image(bluzka_rozowa.img, bluzka_rozowa.x, bluzka_rozowa.y) #Patrycja Leśniak
    image(bluzka_zielona.img, bluzka_zielona.x, bluzka_zielona.y)
    image(koszulka_czarna.img, koszulka_czarna.x, koszulka_czarna.y) #Julia Kornecka
    
    image(spodnica_brazowa.img, spodnica_brazowa.x, spodnica_brazowa.y)
    image(spodnica_czerwona.img, spodnica_czerwona.x, spodnica_czerwona.y)
    image(spodnica_fioletowa.img, spodnica_fioletowa.x, spodnica_fioletowa.y)
    image(spodnica_niebieska.img, spodnica_niebieska.x, spodnica_niebieska.y) #Patrycja Leśniak
    image(spodnica_zielona.img, spodnica_zielona.x, spodnica_zielona.y)
    
    image(black_shoes.img, black_shoes.x, black_shoes.y) #Władysław Bacewicz
    image(klapki_fioletowe.img, klapki_fioletowe.x, klapki_fioletowe.y)
    image(klapki_rozowe.img, klapki_rozowe.x, klapki_rozowe.y) #Patrycja Leśniak
    image(klapki_zielone.img, klapki_zielone.x, klapki_zielone.y)
    
    image(sukienka_czarna_1.img, sukienka_czarna_1.x, sukienka_czarna_1.y)
    image(sukienka_czarna_2.img, sukienka_czarna_2.x, sukienka_czarna_2.y) #Julia Kornecka
    image(sukienka_magenta.img, sukienka_magenta.x, sukienka_magenta.y) #Julia Kornecka
    
    # show_clothes()
    
#  'mouseClicked()'
#  function is responsible for
#  changing the state of chosen
#  clothes category    

def mouseClicked():
    global hair_selected, torso_selected, legs_selected, footwear_selected, dresses_selected
    if mouseX >= 1193 and mouseX <= 1268 and mouseY >= 7 and mouseY <= 47:
        exit()
    if mouseX >= width//2-550 and mouseX <= width//2-550 + 80 and mouseY >= height//2-200 - 30 and mouseY <= height//2-200 + 3:
        hair_selected = True
        torso_selected = False
        legs_selected = False
        footwear_selected = False
        dresses_selected = False
        print(hair_selected)
        hair_1.x = 395
        hair_1.y = 75
        hair_2.x = 495
        hair_2.y = 75
        wlosy_blond.x = 595
        wlosy_blond.y = 75
        wlosy_brazowe.x = 395
        wlosy_brazowe.y = 175
        wlosy_czarne_1.x = 495
        wlosy_czarne_1.y = 175
        wlosy_czarne_2.x = 595
        wlosy_czarne_2.y = 175
    if mouseX >= width//2-550 and mouseX <= width//2-550 + 110 and mouseY >= height//2-130 - 30 and mouseY <= height//2-130 + 3:
        hair_selected = False
        torso_selected = True
        legs_selected = False
        footwear_selected = False
        dresses_selected = False
        print(hair_selected)
        hair_1.x = 1500
        hair_1.y = 200
        hair_2.x = 1500
        hair_2.y = 200
        wlosy_blond.x = 1500
        wlosy_blond.y = 200
        wlosy_brazowe.x = 1500
        wlosy_brazowe.y = 200
        wlosy_czarne_1.x = 1500
        wlosy_czarne_1.y = 200
        wlosy_czarne_2.x = 1500
        wlosy_czarne_2.y = 200
    if mouseX >= width//2-550 and mouseX <= width//2-550 + 90 and mouseY >= height//2-60 - 30 and mouseY <= height//2-60 + 3:
        hair_selected = False
        torso_selected = False
        legs_selected = True
        footwear_selected = False
        dresses_selected = False
    if mouseX >= width//2-550 and mouseX <= width//2-550 + 175 and mouseY >= height//2+10 - 30 and mouseY <= height//2+10 + 3:
        hair_selected = False
        torso_selected = False
        legs_selected = False
        footwear_selected = True
        dresses_selected = False
    if mouseX >= width//2-550 and mouseX <= width//2-550 + 150 and mouseY >= height//2+80 - 30 and mouseY <= height//2+80 + 3:
        hair_selected = False
        torso_selected = False
        legs_selected = False
        footwear_selected = False
        dresses_selected = True
    if mouseX >= 395 and mouseX <= 395+207 and mouseY >= 75 and mouseY <= 75 + 110 and hair_selected is True:
        hair_1.x = 795
        
        
        
#  'text_color()'
#  function is responsible for
#  changing a variable that colors
#  a text of clothes category  
      
def text_color():
    global fill_1, fill_2, fill_3, fill_4, fill_5, hair_selected, torso_selected, legs_selected, footwear_selected, dresses_selected
    if hair_selected is True:
        fill_1 = 150
        fill_2 = 255
        fill_3 = 255
        fill_4 = 255
        fill_5 = 255
    elif torso_selected is True:
        fill_1 = 255
        fill_2 = 150
        fill_3 = 255
        fill_4 = 255
        fill_5 = 255
    elif legs_selected is True:
        fill_1 = 255
        fill_2 = 255
        fill_3 = 150
        fill_4 = 255
        fill_5 = 255
    elif footwear_selected is True:
        fill_1 = 255
        fill_2 = 255
        fill_3 = 255
        fill_4 = 150
        fill_5 = 255
    elif dresses_selected is True:
        fill_1 = 255
        fill_2 = 255
        fill_3 = 255
        fill_4 = 255
        fill_5 = 150
 
 
 
# 'show_clothes()'
# function moves hair items
# to the center of background
# when variable 'hair_selected' is True
#
# sadly, that function conflicts
# with picking a certain hairstyle,
# because a hairstyle comes back at
# original coordinates due to
# the variable 'hair_selected'

# def show_clothes():
#     if hair_selected is True:
#         hair_1.x = 395
#         hair_1.y = 75
#         hair_2.x = 495
#         hair_2.y = 75
#         wlosy_blond.x = 595
#         wlosy_blond.y = 75
#         wlosy_brazowe.x = 395
#         wlosy_brazowe.y = 175
#         wlosy_czarne_1.x = 495
#         wlosy_czarne_1.y = 175
#         wlosy_czarne_2.x = 595
#         wlosy_czarne_2.y = 175    
#     elif hair_selected is False:
#         hair_1.x = 1500
#         hair_1.y = 200
#         hair_2.x = 1500
#         hair_2.y = 200
#         wlosy_blond.x = 1500
#         wlosy_blond.y = 200
#         wlosy_brazowe.x = 1500
#         wlosy_brazowe.y = 200
#         wlosy_czarne_1.x = 1500
#         wlosy_czarne_1.y = 200
#         wlosy_czarne_2.x = 1500
#         wlosy_czarne_2.y = 200
        
   

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
