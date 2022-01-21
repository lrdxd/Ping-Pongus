from pygame import *

 
font.init()
font1 = font. SysFont('Arial', 30)
img_zadnik = "wht.jpg"
img_rack1 = "ham1.png" 
img_rack2 = "ham2.png" 
img_ballz = "frd.png" 

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pongus")


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
           self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
           self.rect.y += self.speed
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

'''class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 500:
            self.direction = "left"
        if self.rect.x >= win_width -85:
            self.direction = "right"
        
        
        if self.direction == "left":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed'''
        
background = transform.scale(image.load(img_zadnik), (win_width, win_height))
player1 = Player( img_rack1, 30, 200, 4, 50, 150 )
player2 = Player( img_rack2, 620, 200, 4, 50, 150)   

speed_x = 3
speed_y = 3

game = True
finish = False
clock = time.Clock()
FPS = 60


while game:
    for e in event.get():
       if e.type == QUIT:
           game = False

    if finish != True:
            player1.update_1()
            player2.update_2()
    window.blit(background,(0,0))

    player1.reset()
    player2.reset()

    display.update()
    clock.tick(FPS)