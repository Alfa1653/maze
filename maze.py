#создай игру "Лабиринт"!

from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (700, 500))

window.blit(background,(0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed

    def auto_move(self):
        if self.rect.x <= 470:
           self.direction = "right"
        if self.rect.x >= 615:
           self.direction = "left"

    
        if self.direction == "left":
           self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

hero = GameSprite('hero.png', 100, 100, 10)

game = True
while game:
    window.blit(background,(0, 0))
    hero.move()
    hero.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    time.delay(50)