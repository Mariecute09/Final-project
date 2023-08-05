from pygame import *
mixer.init()
mixer.music.load("Music.mp3")
mixer.music.play()
clock = time.Clock()

WIDTH = 700
HEIGHT = 500
FPS = 40


score_1 = 0
score_2 = 0

speed_x = 5
speed_y = 5

screen = display.set_mode((WIDTH, HEIGHT))
background = transform.scale(image.load('background.png'),(WIDTH,HEIGHT))

font.init()
font1 = font.Font(None, 35)
win_1 = font1.render("YOU WIN, PLAYER 1", True, (250, 250, 250))
win_2 = font1.render("YOU WIN, PLAYER 2", True, (250, 250, 250))

score_one = font1.render("Player 1: "+str(score_1),True,(250,250,250))
score_two = font1.render("Player 2: "+str(score_2),True,(250,250,250))

class Main(sprite.Sprite):
    def __init__(self,img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(Main):
    def controls_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 2:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - 50:
           self.rect.y += self.speed
    def controls_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 2:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - 50:
           self.rect.y += self.speed

paddle_1 = Player("paddle.png", 30, 200, 30, 50, 10)
paddle_2 = Player("paddle.png", 630, 200, 30, 50, 10)
ball = Main("Ball.png", 200, 200, 20, 20, 8)

run = True
finish = False

while run:


    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        screen.blit(background,(0,0))
        screen.blit(score_one,(10,10))
        screen.blit(score_two,(10,50))

        paddle_1.reset()
        paddle_2.reset()
        ball.reset()
        paddle_1.controls_1()
        paddle_2.controls_2()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(paddle_1, ball) or sprite.collide_rect(paddle_2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y < 0 or ball.rect.y > HEIGHT - 20:
            speed_y *= -1

        if ball.rect.x < 0:
            score_2 += 1
            score_two = font1.render("Pplayer 2: "+str(score_2),True,(250,250,250))
            finish = True
        
        if ball.rect.x > WIDTH - 20:
            score_1 += 1
            score_one = font1.render("Player 1: "+str(score_1),True,(250,250,250))
            finish = True

        if score_1 >= 1:
            finish = True
            screen.blit(score_one,(WIDTH//2 - 30, HEIGHT//2))
            screen.blit(win_1,(WIDTH//2 - 80, HEIGHT//2 + 50))
        if score_2 >= 1:
            finish = True
            screen.blit(score_two,(WIDTH//2, HEIGHT//2))  
            screen.blit(win_2,(WIDTH//2, HEIGHT//2 + 10))


        display.update()

    else:
        finish = False
        paddle_1 = Player("paddle.png", 30, 200, 30, 50, 10)
        paddle_2 = Player("paddle.png", 650, 200, 30, 50, 10)
        ball = Main("Ball.png", 200, 200, 20, 20, 8)
        time.delay(100)

    clock.tick(50)


        

