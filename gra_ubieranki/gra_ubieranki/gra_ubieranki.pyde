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











hat_selected = False
dress_selected = False
shoes_selected = False

#Patrycja Leśniak (linijki odpowiadające za kursor)    
def draw(): #ta funkcja odpowiada za kursor
    if mousePressed:
        cursor(HAND)
    else: 
        cursor(ARROW)

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
