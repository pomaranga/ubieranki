
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
