import pygame
import random
from game_parameters import *

class Shake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load('../assets/sprites/corepower.png').convert()
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.speed= random.uniform(2.0, 3.0)
        self.rect.center= (x,y)
    def update(self):
        self.y += self.speed
        self.rect.y= self.y

    def draw(self,surf):
        surf.blit(self.image, self.rect)


class Yogurt(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../assets/sprites/oiko.jpg').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(2.0, 3.0)
        self.rect.center = (x, y)
    def update(self):
        self.y += self.speed
        self.rect.y= self.y

    def draw(self,surf):
        surf.blit(self.image, self.rect)


shakes = pygame.sprite.Group()
yogurts = pygame.sprite.Group()
