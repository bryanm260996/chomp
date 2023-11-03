import pygame
from game_parameters import *

#create pygame sprite class

class Player(pygame.sprite.Sprite):
    def __init__ (self,x,y):
        super().__init__()
        self.image= pygame.image.load('../assets/sprites/player_action1.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.forward_image= pygame.image.load('../assets/sprites/player_slide.png').convert()
        self.forward_image.set_colorkey((0, 0, 0))
        self.reverse_image= pygame.transform.flip(self.forward_image, True, False)

        self.rect=self.image.get_rect()
        self.x=400
        self.y=500
        self.rect.center= (0,0)
        self.x_speed=0
        self.y_speed=0
        self.celebratory_image= self.image = pygame.image.load('../assets/sprites/player_cheer1.png').convert()
        self.celebratory_image.set_colorkey((0, 0, 0))
        self.hurt=self.image = pygame.image.load('../assets/sprites/zombie_hurt.png').convert()
        self.hurt.set_colorkey((0, 0, 0))
        self.climbing_image=self.image = pygame.image.load('../assets/sprites/player_climb1.png').convert()
        self.climbing_image.set_colorkey((0, 0, 0))
    def move_right(self):
        self.x_speed = 1*PLAYER_SPEED
        self.image = self.forward_image

    def move_left(self):
        self.x_speed= -1*PLAYER_SPEED
        self.image = self.reverse_image
    def jump(self):
        self.y_speed= -1*PLAYER_SPEED
        self.image = self.climbing_image

    def down(self):
        self.y_speed= 1*PLAYER_SPEED
        self.image = self.climbing_image

    def stop(self):
        self.x_speed=0
        self.y_speed=0

    def update(self):
         #MAKE SURE PLAYER STAYS WITHIN BOUNDARIES
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > screen_width-tile_size:
            self.x= screen_width-tile_size
        if self.x < 0:
            self.x= 0

        if self.y > 540:
            self.y= 540
        if self.y < 400:
            self.y= 400
        self.rect.x=self.x
        self.rect.y = self.y



    def draw(self, surf):
        surf.blit(self.image , self.rect.topleft)



