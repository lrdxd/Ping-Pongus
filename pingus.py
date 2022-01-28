from pygame import *

 
font.init()
font = font.Font(None, 60)
lose1 = font.render("ИГРОК 1 ЛЕЖАТЬ", True, (255, 0, 0))
lose2 = font.render("ИГРОК 2 ЛЕЖАТЬ", True, (255, 0, 0))

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
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
           self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
           self.rect.y += self.speed
      
background = transform.scale(image.load(img_zadnik), (win_width, win_height))
player1 = Player( img_rack1, 30, 200, 4, 50, 150 )
player2 = Player( img_rack2, 620, 200, 4, 50, 150)
ball = GameSprite( img_ballz, 330, 200, 4, 50, 50 )

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
    window.blit(background,(0,0))
    
    if finish != True:
        player1.update_1()
        player2.update_2()
        ball.rect.x +=  speed_x
        ball.rect.y +=  speed_y
    
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
        speed_y *= 1
      
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (165, 200))
        game_over = True
 
    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2, (165, 200))
        game_over = True
    
    
    player1.reset()
    player2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)

