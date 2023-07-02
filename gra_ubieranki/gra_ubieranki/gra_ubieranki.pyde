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
character_image = Interface("character_image", "data/character.png", 795, 75)


exit_button = Button("exit_button", "data/Buttons/exit_button.png", 1193, 7, 80, 40)
reset_button = Button("reset_button", "data/Buttons/reset_button.png", 945, 650, 80, 40)

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

def exit_game(): #that function was originally created by Bartosz Rząd
    if (mousePressed and mouseX >= 1193 and mouseX <= 1268 and mouseY >= 7 and mouseY <= 47):
        exit()
        
def choose_category(): #function that shows if user clicked on "Hair" text (Aleksander Otradnov)
    hair_selected = None #not sure if is that variable is needed
    torso_selected = None
    legs_selected = None
    footwear_selected = None
    dresses_selected = None
    if (mousePressed and mouseX >= width//2-550 and mouseX <= width//2-550 + 80 and mouseY >= height//2-200 - 30 and mouseY <= height//2-200 + 3):
                hair_selected = True #not sure if is that variable is needed
                fill(150, 255, 150)
                text("Hair", width//2-550, height//2-200)
                fill(255, 255, 255)
                text("Torso", width//2-550, height//2-130)
                text("Legs", width//2-550, height//2-60)
                text("Footwear", width//2-550, height//2+10)
                text("Dresses", width//2-550, height//2+80)
                cursor(HAND) # this part of function was originally conceived by Patrycja Leśniak
    elif (mousePressed and mouseX >= width//2-550 and mouseX <= width//2-550 + 80 and mouseY >= height//2-130 - 30 and mouseY <= height//2-130 + 3):
                torso_selected = True 
                fill(150, 255, 150)
                text("Torso", width//2-550, height//2-130)
                fill(255, 255, 255)
                text("Hair", width//2-550, height//2-200)
                text("Legs", width//2-550, height//2-60)
                text("Footwear", width//2-550, height//2+10)
                text("Dresses", width//2-550, height//2+80)
                cursor(HAND)
    elif (mousePressed and mouseX >= width//2-550 and mouseX <= width//2-550 + 80 and mouseY >= height//2-60 - 30 and mouseY <= height//2-60 + 3):
                legs_selected = True
                fill(150, 255, 150)
                text("Legs", width//2-550, height//2-60)
                fill(255, 255, 255)
                text("Hair", width//2-550, height//2-200)
                text("Torso", width//2-550, height//2-130)
                text("Footwear", width//2-550, height//2+10)
                text("Dresses", width//2-550, height//2+80)
                cursor(HAND)
    elif (mousePressed and mouseX >= width//2-550 and mouseX <= width//2-550 + 80 and mouseY >= height//2+10 - 30 and mouseY <= height//2+10 + 3):
                footwear_selected = True
                fill(150, 255, 150)
                text("Footwear", width//2-550, height//2+10)
                fill(255, 255, 255)
                text("Hair", width//2-550, height//2-200)
                text("Torso", width//2-550, height//2-130)
                text("Legs", width//2-550, height//2-60)
                text("Dresses", width//2-550, height//2+80)
                cursor(HAND)           
    elif (mousePressed and mouseX >= width//2-550 and mouseX <= width//2-550 + 80 and mouseY >= height//2+80 - 30 and mouseY <= height//2+80 + 3):
                dresses_selected = True
                fill(150, 255, 150)
                text("Dresses", width//2-550, height//2+80)
                fill(255, 255, 255)
                text("Hair", width//2-550, height//2-200)
                text("Torso", width//2-550, height//2-130)
                text("Legs", width//2-550, height//2-60)
                text("Footwear", width//2-550, height//2+10)
                cursor(HAND)
    else:
                hair_selected = False #not sure if is that variable is needed
                torso_selected = False
                legs_selected = False
                footwear_selected = False
                dresses_selected = False
                fill(255,255,255)
                text("Hair", width//2-550, height//2-200)
                text("Torso", width//2-550, height//2-130)
                text("Legs", width//2-550, height//2-60)  #Vitalii Pshenychniak
                text("Footwear", width//2-550, height//2+10)  #Władysław Bacewicz
                text("Dresses", width//2-550, height//2+80)  #Władysław Bacewicz
                cursor(ARROW)            















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
    global background_image #is_dragging, mouse_offsetdress, mouse_offsethair, flaga_wlosy
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
        # background(background_image.img)
        
#     menu_start() #B.Rząd
    
    
    
    background(background_image.img)
   
    fill(30, 30, 30, 200)
    rect(20, 65, 300, 600, 10)    
    
    choose_category()
    
    image(exit_button.img, exit_button.x, exit_button.y, exit_button.size_x, exit_button.size_y)  #Wladiskowacz
    image(reset_button.img, reset_button.x, reset_button.y, reset_button.size_x, reset_button.size_y)  #Wladiskowacz
    image(character_image.img, character_image.x, character_image.y)  #Wladiskowacz
    
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
    
    exit_game()

    
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
