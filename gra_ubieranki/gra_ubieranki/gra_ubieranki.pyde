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


def setup():
    global webImg, characterImg, dress, hair, hair2, shoes
    size(1200, 800)
    textSize(50)
    url = "https://kartinki.pibig.info/uploads/posts/2023-04/1682411811_kartinki-pibig-info-p-garderobnaya-kartinki-arti-instagram-2.jpg"
    webImg = loadImage(url, "jpg")
    characterImg = loadImage("character.PNG")
    dress = RzeciRuszanie("dress.PNG", 600, 200)
    hair = RzeciRuszanie("hair.PNG", -200, 200)
    hair2 = RzeciRuszanie("hair2.PNG", 600, 200)
    shoes = RzeciRuszanie("shoes.PNG", 600, 180)


def draw():
    image(webImg, 0, 0)
    background(0)
    image(webImg, 0, 0)
    fill(30, 30, 30, 200)
    rect(20, 100, 300, 600, 10)
    fill(400, 400, 400, 400)
    rect(600, 200, 150, 450, 10)
    fill(255, 255, 255)

    text("hat", width // 2 - 500, height // 2 - 200, 40)
    text("dress", width // 2 - 500, height // 2 - 150, 80)
    text("Hair", width // 2 - 500, height // 2 - 100, 80)
    text("Hair_2", width // 2 - 500, height // 2 - 50, 80)
    text("Shoes", width // 2 - 500, height // 2 - 0, 80)
    image(characterImg, 600, 200, 150, 430)

    dress.display()
    hair.display()
    hair2.display()
    shoes.display()


def mousePressed():
    for rzecz in [dress, hair, hair2, shoes]:
        rzecz.mouse_pressed()
        if rzecz.is_dragging:
            break


def mouseReleased():
    for rzecz in [dress, hair, hair2, shoes]:
        rzecz.mouse_released()


def mouseDragged():
    for rzecz in [dress, hair, hair2, shoes]:
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
