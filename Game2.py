import pygame
import sys
import random

#Initialize Pygame:
pygame.init()

#screen dimensions:

screen_width=800
screen_height=600
tile_size=64

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Beach')

custom_font=pygame.font.Font('assets/fonts/DERSIRA.ttf', 80)

#define function to draw background

def draw_background(surf):
    water= pygame.image.load('assets/sprites/water.png').convert() #CONVERT ALLOWS TO MAKE BACKGROUND TRANSPARENT
    sand=pygame.image.load('assets/sprites/sand_top (1).png').convert()
    seagrass=pygame.image.load('assets/sprites/seagrass.png').convert()

    #use png transparency
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0, 0, 0))

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

def draw_fishes(): 








    #MAIN LOOP
running=True
background= screen.copy()
draw_background(background)  #THIS 2 LINES OF CODE ARE TO CREATE A COPY OF THE ORIGINAL BACKGROUND

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
        #DRAW BACKGROUND
    screen.blit(background, (0,0)) #THIS PASTES THE ENTIRE FUNCTION INTO THE ORIGINAL SCREEN, STARTING AT 0,0
    pygame.display.flip()

pygame.quit()
