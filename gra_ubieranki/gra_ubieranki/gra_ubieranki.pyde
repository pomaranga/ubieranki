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
class ImageAbstract(): #abstract class for elements of clothes; that class was originally created by Anhelina Hlushanok
    __metaclass__ = ABCMeta
    @abstractmethod      
    def load_image(self):
        super().__init__()


class Hair(ImageAbstract): #subclass for elements of hairstyles
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
         
                                   
class Torso(ImageAbstract): #subclass for elements of upper body clothes
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
    
    
class Legs(ImageAbstract): #subclass for elements of lower body clothes
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
    
    
class Footwear(ImageAbstract): #subclass for elements of footwear
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)


class Dress(ImageAbstract): #subclass for elements of full body clothes
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
        
        
        
# For interface elements will suit a standard class,
# because there won't be a lot of
# interface elements, that we could lost in.
                
class ButtonInterface: #changed from Interface class to ButtonInterface N.Kunach 
    def __init__(self, name,  file_path, x, y):
        self.name = name
        self.file_path = file_path
        self.x = x
        self.y = y
        
    def load_image(self, file_path):
        self.img = loadImage(file_path)
    

# But still I created the button subclass
# for better readability of code and maybe
# to a future use for you.
            
class Button(ButtonInterface): #subclass for buttoms
    def __init__(self, name, file_path, x, y, size_x, size_y):
        ButtonInterface.__init__(self, name, file_path, x, y)
        self.size_x = size_x
        self.size_y = size_y
        
    def load_image(self, file_path):
        ButtonInterface.load_image(self, file_path)

class CategoryInterface: #klasa N.Kunach
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class Category(CategoryInterface): #N.Kunach
    def __init__(self, name, x, y,):
        CategoryInterface.__init__(self, name, x, y)
        self.size_x = x + 90
        self.size_y = y - 30
        
    def print_text(self, r, g, b):
        fill(r, g, b)
        text(self.name, self.x, self.y)


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


background_image = ButtonInterface("background_image", "data/background_image.png", 0, 0) #N.Kunach
character_image = ButtonInterface("character_image", "data/character.png", 795, 75) #N.Kunach


exit_button = Button("exit_button", "data/Buttons/exit_button.png", 1193, 7, 80, 40)
reset_button = Button("reset_button", "data/Buttons/reset_button.png", 945, 650, 80, 40)

start_button = Button("start_button", "data/Buttons/start_button.png", 75, 100, 200, 100) #N.Kunach
how_to_play_button = Button("how_to_play_button", "data/Buttons/htp_img.png", 75, 300, 200, 100) #N.Kunach
quit_button = Button("quit_button", "data/Buttons/quit_button.png", 75, 500, 200, 100) #N.Kunach


hair_category = Category("Hair", 90, 230)            #N.Kunach categories
torso_category = Category("Torso", 90, 300)
legs_category = Category("Legs", 90, 370)
footwear_category = Category("Footwearr", 90, 440)
dresses_category = Category("Dresses", 90, 520)


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
                     
                
                        
                                        
        
# Below I set variable statements for classes            

game_started = False #N.Kunach
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
    
        
    
    background_image.load_image(background_image.file_path)
    character_image.load_image(character_image.file_path)  #Władysław Bacewicz
    
    
    exit_button.load_image(exit_button.file_path)          #Władysław Bacewicz
    reset_button.load_image(reset_button.file_path)        #Władysław Bacewicz
    
    
    start_button.load_image(start_button.file_path)             #N.Kunach
    how_to_play_button.load_image(how_to_play_button.file_path) #N.Kunach
    quit_button.load_image(quit_button.file_path)               #N.Kunach  
    
    hair_1.load_image(hair_1.file_path)
    hair_2.load_image(hair_2.file_path)                    #Władysław Bacewicz
    wlosy_blond.load_image(wlosy_blond.file_path)          #Patrycja Leśniak
    wlosy_brazowe.load_image(wlosy_brazowe.file_path)
    wlosy_czarne_1.load_image(wlosy_czarne_1.file_path)
    wlosy_czarne_2.load_image(wlosy_czarne_2.file_path)    #Julia Kornecka
    
    bluzka_niebieska.load_image(bluzka_niebieska.file_path)
    bluzka_rozowa.load_image(bluzka_rozowa.file_path)      #Patrycja Leśniak
    bluzka_zielona.load_image(bluzka_zielona.file_path)
    koszulka_czarna.load_image(koszulka_czarna.file_path)  #Julia Kornecka
    
    spodnica_brazowa.load_image(spodnica_brazowa.file_path)
    spodnica_czerwona.load_image(spodnica_czerwona.file_path)
    spodnica_fioletowa.load_image(spodnica_fioletowa.file_path)
    spodnica_niebieska.load_image(spodnica_niebieska.file_path) #Patrycja Leśniak
    spodnica_zielona.load_image(spodnica_zielona.file_path)
    
    black_shoes.load_image(black_shoes.file_path)               #Władysław Bacewicz
    klapki_fioletowe.load_image(klapki_fioletowe.file_path)
    klapki_rozowe.load_image(klapki_rozowe.file_path)           #Patrycja Leśniak
    klapki_zielone.load_image(klapki_zielone.file_path)
    
    sukienka_czarna_1.load_image(sukienka_czarna_1.file_path)
    sukienka_czarna_2.load_image(sukienka_czarna_2.file_path)   #Julia Kornecka
    sukienka_magenta.load_image(sukienka_magenta.file_path)     #Julia Kornecka
    
    
    
    
    # is_dragging = False
    # mouse_offsetdress = PVector(0, 0)  #Wladiskowacz
    # is_dragging2 = False     
    # mouse_offsethair = PVector(0, 0)   #Pshenychniak
    
def background_screen(): #N.Kunach zmiana def draw na background_screen
    background(background_image.img)
    fill(30, 30, 30, 200)
    rect(20, 65, 300, 600, 10)
    text_color()
    textSize(40)
    
def menu_screen(): #N.Kunach
    image(start_button.img, start_button.x, start_button.y, start_button.size_x, start_button.size_y)
    image(how_to_play_button.img, how_to_play_button.x, how_to_play_button.y, how_to_play_button.size_x, how_to_play_button.size_y)
    image(quit_button.img, quit_button.x, quit_button.y, quit_button.size_x, quit_button.size_y)
    
    # Set font N.Kunach
    fill(114, 26, 48) 
    font = createFont("Vallena.ttf", 50) 
    textFont(font)
    textSize(74)  
    textAlign(CENTER, CENTER)  
    text("UBIERANKI", width / 2.08, height / 20)
    # Back to default N.Kunach
    fill(0)
    font = createFont("Arial", 36)
    textFont(font)
    textSize(36)
    textAlign(LEFT, BASELINE)    
    
def game_screen(): #N.Kunach
    image(character_image.img, character_image.x, character_image.y) 
    

    hair_category.print_text(fill_1, 255, fill_1) # using the print_text method instead of the fill and text N.Kunach
    torso_category.print_text(fill_2, 255, fill_2)
    legs_category.print_text(fill_3, 255, fill_3)
    footwear_category.print_text(fill_4, 255, fill_4)
    dresses_category.print_text(fill_5, 255, fill_5) #N.Kunach
        
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
    
    image(exit_button.img, exit_button.x, exit_button.y, exit_button.size_x, exit_button.size_y)  #Wladiskowacz
    image(reset_button.img, reset_button.x, reset_button.y, reset_button.size_x, reset_button.size_y)  #Wladiskowacz    
    
def draw():
    background_screen()
    
    if game_started:
        game_screen()
    else:
        menu_screen()
 
def between(x, limit1, limit2): #N.Kunach will always be between two numbers
    return (x >= min(limit1, limit2) and (x <= max(limit1, limit2)))



  
#  'mouseClicked()'
#  function is responsible for
#  changing the state of chosen
#  clothes category    

def mouseClicked():
    global hair_selected, torso_selected, legs_selected, footwear_selected, dresses_selected, game_started #N.Kunach game_started, htp, quit

    #print "mouseClicked: x:{} y:{} ".format(mouseX, mouseY) #position search by N.Kunach
    # print "hair? x:{} size_x:{} y:{} size_y:{}".format(mouseX >= hair_category.x, mouseX <= hair_category.size_x, mouseY >= hair_category.y, mouseY <= hair_category.size_y)
    # print "Hair: x:{} y:{} size_x:{} size_y:{}".format(hair_category.x, hair_category.y, hair_category.size_x, hair_category.size_y) 

    if game_started is False:
        if mouseX >= start_button.x and mouseX <= start_button.x + start_button.size_x and mouseY >= start_button.y and mouseY <= start_button.y + start_button.size_y: #N.Kunach
            game_started = True
        if mouseX >= how_to_play_button.x and mouseX <= how_to_play_button.x + how_to_play_button.size_x and mouseY >= how_to_play_button.y and mouseY <= how_to_play_button.y + how_to_play_button.size_y: #N.Kunach
            print "how to play"
        if mouseX >= quit_button.x and mouseX <= quit_button.x + quit_button.size_x and mouseY >= quit_button.y and mouseY <= quit_button.y + quit_button.size_y: #N.Kunach
            exit()
    if game_started is True:    
        if mouseX >= exit_button.x and mouseX <= exit_button.x + exit_button.size_x and mouseY <= exit_button.y and mouseY >= exit_button.y + exit_button.size_y:
            exit()
            
        if between(mouseX, hair_category.x, hair_category.size_x) and between(mouseY, hair_category.y, hair_category.size_y):
            # if False: # mouseX >= width//2-550 and mouseX <= width//2-550 + 80 and mouseY >= height//2-200 - 30 and mouseY <= height//2-200 + 3:
            print "Hair clicked: x:{} y:{} size_x:{} size_y:{}".format(hair_category.x, hair_category.y, hair_category.size_x, hair_category.size_y)
            
            
            
            hair_selected = True
            torso_selected = False
            legs_selected = False
            footwear_selected = False
            dresses_selected = False
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
        if between(mouseX, torso_category.x, torso_category.size_x) and between(mouseY, torso_category.y, torso_category.size_y): #N.Kunach each of between, corrected, to make the categories torso, legs and etc better written
        # if mouseX >= width//2-550 and mouseX <= width//2-550 + 110 and mouseY >= height//2-130 - 30 and mouseY <= height//2-130 + 3:
            print "Torso clicked"
            hair_selected = False
            torso_selected = True
            legs_selected = False
            footwear_selected = False
            dresses_selected = False
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
        if between(mouseX, legs_category.x, legs_category.size_x) and between(mouseY, legs_category.y, legs_category.size_y):
        # if mouseX >= legs_category.x and mouseX <= legs_category.x + legs_category.size_x  and mouseY >= legs_category.y and mouseY <= legs_category.y + legs_category.size_y:
            print "Legs clicked"
            hair_selected = False
            torso_selected = False
            legs_selected = True
            footwear_selected = False
            dresses_selected = False
        if between(mouseX, footwear_category.x, footwear_category.size_x) and between(mouseY, footwear_category.y, footwear_category.size_y):
        # if mouseX >= footwear_category.x and mouseX <= footwear_category.x + footwear_category.size_x  and mouseY >= footwear_category.y and mouseY <= footwear_category.y + footwear_category.size_y:
            print "Footwear clicked"
            hair_selected = False
            torso_selected = False
            legs_selected = False
            footwear_selected = True
            dresses_selected = False
        if between(mouseX, dresses_category.x, dresses_category.size_x) and between(mouseY, dresses_category.y, dresses_category.size_y):
        # if mouseX >= dresses_category.x and mouseX <= dresses_category.x + dresses_category.size_x and mouseY >= dresses_category.y and mouseY <= dresses_category.y + dresses_category.size_y:
            print "Dresses clicked"
            hair_selected = False
            torso_selected = False
            legs_selected = False
            footwear_selected = False
            dresses_selected = True
        # if mouseX >= 395 and mouseX <= 395+207 and mouseY >= 75 and mouseY <= 75 + 110 and hair_selected is True:
            # hair_1.x = 795
        if between(mouseX, hair_1.x, hair_1.x - 30) and between(mouseY, hair_1.y, hair_1.y + 75): #N.Kunach próby naprawienia wlosów
            hair_1.x = 795
        if between(mouseX, hair_2.x, hair_2.x - 30) and between(mouseY, hair_2.y, hair_2.y + 75):
            hair_2.x = 795
        if between(mouseX, wlosy_blond.x, wlosy_blond.x - 30) and between(mouseY, wlosy_blond.y, wlosy_blond.y + 75):
            wlosy_blond.x = 795
        if between(mouseX, wlosy_brazowe.x, wlosy_brazowe.x - 30) and between(mouseY, wlosy_brazowe.y, wlosy_brazowe.y + 75):
            wlosy_brazowe.x = 795
        if between(mouseX, wlosy_czarne_1.x, wlosy_czarne_1.x - 30) and between(mouseY, wlosy_czarne_1.y, wlosy_czarne_1.y + 75):
            wlosy_czarne_1.x = 795
        if between(mouseX, wlosy_czarne_2.x, wlosy_czarne_2.x - 30) and between(mouseY, wlosy_czarne_2.y, wlosy_czarne_2.y + 75):
            wlosy_czarne_2.x = 795
        
        
        
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
