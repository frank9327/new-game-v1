import math
from pygame import mixer
import pygame, random
from sys import exit
import random
import sys
pygame.init()
font = pygame.font.Font("proffesional Edition.ttf", 30)
screen_width = 500
screen_height = 750
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
        if self.rect.right>500:
            deltax *= -3
            self.rect.centerx=445
        self.rect.centerx += deltax
        self.rect.centery += deltay


class Food(pygame.sprite.Sprite):
    def __init__(self,color):
        super(Food,self).__init__()
        self.radius=5
        self.speed=random.randint(5,20)
        self.x = random.randint(0,500)
        self.y = random.randint(0,700)
        self.x_heading = (1/self.radius) * self.speed
        self.y_heading = (1/self.radius) * self.speed
        self.image=pygame.Surface((self.radius*2,self.radius*2),pygame.SRCALPHA, 32)
        self.image=self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (self.radius,self.radius),self.radius)
        self.rect=self.image.get_rect(center=(random.randint(10,450),random.randint(5,80)))


    def move(self):
        if self.rect.centery <= 0 or self.rect.centery >= 750:
            self.y_heading *= -1
        self.rect.y += self.y_heading

sq1 = Square(400,600,"pink")
squares = pygame.sprite.Group()
squares.add(sq1)
food=pygame.sprite.Group()
edible=pygame.sprite.Group()
edible.add(food)
edible.add(squares)

spawn=random.randint(3,6)
alive=spawn
for num in range(spawn):
    # mealColor=(random.randint(0,0),random.randint(0,0),random.randint(50,255))
    mealColor="White"
    food.add(Food(mealColor))
points=0
misses=0
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

    for fruit in food:
        fruit.move()
        if sq1.rect.colliderect(fruit.rect):
            fruit.kill()
            alive-=1
            points+=1
        if fruit.rect.centery>sq1.rect.centery+30:
            fruit.kill()
            misses+=1
            alive-=1
        if alive<1:
            alive=spawn
            for num in range(spawn):
                # mealColor=(random.randint(0,0),random.randint(0,0),random.randint(50,255))
                food.add(Food(mealColor))
        if misses>=10:
            text=str("You lose")
            text = font.render(text, True, (200,0,0))
            screen.blit(text, (200, 350))
            alive=9
        if points>=1:
            text=str("You Win")
            text = font.render(text, True, (250,250,0))
            screen.blit(text, (200, 350))
            alive=9
    squares.draw(screen)
    food.draw(screen)
    text=str(f"{str(points)} points")
    text = font.render(text, True, (255,255,255))
    screen.blit(text, (10, 10))
    text=str(f"{str(misses)} misses")
    text = font.render(text, True, (255,255,255))
    screen.blit(text, (350, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()



