import math
from pygame import mixer
import pygame, random
from sys import exit
import random
import sys
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Intro to Pygame: Platform Game")
clock = pygame.time.Clock()


class Square(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super(Square, self).__init__()
        self.image = pygame.Surface((100,100), pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
        self.radius=20
    
    def move(self, deltax, deltay):
        if self.rect.left < 0:
            deltax *= -3
            self.rect.centerx=50
        if self.rect.right>800:
            deltax *= -3
            self.rect.centerx=745
        self.rect.centerx += deltax
        self.rect.centery += deltay

class Food(pygame.sprite.Sprite):
    def __init__(self,color):
        super(Food,self).__init__()
        self.radius=5
        self.speed=10
        self.x = random.randint(0,650)
        self.y = random.randint(0,500)
        self.x_heading = (1/self.radius) * self.speed
        self.y_heading = (1/self.radius) * self.speed
        self.image=pygame.Surface((self.radius*2,self.radius*2),pygame.SRCALPHA, 32)
        self.image=self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (self.radius,self.radius),self.radius)
        self.rect=self.image.get_rect(center=(random.randint(10,790),random.randint(5,15)))

    def move(self):
        if self.rect.centerx <= -0 or self.rect.centerx >= 0:
            self.x_heading *= -1
        if self.rect.centery <= 0 or self.rect.centery >= 600:
            self.y_heading *= -1
        self.rect.x += self.x_heading
        self.rect.y += self.y_heading

sq1 = Square(400,500,"pink")
squares = pygame.sprite.Group()
squares.add(sq1)
food=pygame.sprite.Group()
edible=pygame.sprite.Group()
edible.add(food)
edible.add(squares)

alive=5
for num in range(0,alive):
    mealColor=(random.randint(0,0),random.randint(0,0),random.randint(50,255))
    food.add(Food(mealColor))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        sq1.move(-4,0)
    if keys[pygame.K_RIGHT]:
        sq1.move(4,0)

    points=0
    win=False
    for fruit in food:
        fruit.move()
        if sq1.rect.colliderect(fruit.rect):
            fruit.kill()
            points=1
            alive=alive-1
            if points>=alive:
                win=True
    if win==True:
        points=0
        for num in range(0,alive):
            mealColor=(random.randint(0,0),random.randint(55,255),random.randint(0,0))
            food.add(Food(mealColor))
    squares.draw(screen)
    food.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()