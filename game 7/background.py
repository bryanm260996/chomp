import pygame
from game_parameters import * #to import all
import random
from fish import Fish, fishes
from enemy import Enemy, enemies
def draw_background(surf):
    water= pygame.image.load('../assets/sprites/water.png').convert() #CONVERT ALLOWS TO MAKE BACKGROUND TRANSPARENT
    sand=pygame.image.load('../assets/sprites/sand_top (1).png').convert()
    seagrass=pygame.image.load('../assets/sprites/seagrass.png').convert()

    #use png transparency
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0, 0, 0))
    custom_font = pygame.font.Font('../assets/fonts/DERSIRA.ttf', 60)

    #fill the screen with water
    for x in range(0,screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))  #SCREEN.BLIT IS TO PASTE IT ON THE ORIGINAL
    #draw the sandy bottom
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x,screen_height-tile_size))

    #DRAW THE SEAGRASS
    for x in range(0, screen_width, tile_size):
        surf.blit(seagrass, (x,screen_height-tile_size*2))

    #DRAW TEXT


    text= custom_font.render('CHOMP',True, (255,0,0))
    surf.blit(text, (((screen_width/2)-tile_size*2) , (screen_height/2)-tile_size*3.5))
def add_fish (num_fish):
    for _ in range(num_fish):
        fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                        random.randint(0, screen_height - tile_size * 2)))

def add_enemies (num_enemies):
    for _ in range(num_enemies):
        enemies.add(Enemy(random.randint(screen_width, screen_width + 50),
                        random.randint(0, screen_height - tile_size * 2)))
