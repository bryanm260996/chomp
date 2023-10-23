import pygame
import sys
import random
from fish import Fish, fishes

#Initialize Pygame:
pygame.init()

#screen dimensions:

screen_width=800
screen_height=600
tile_size=64

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Beach')

clock= pygame.time.Clock()
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

    custom_font = pygame.font.Font('assets/fonts/DERSIRA.ttf', 60)
    text= custom_font.render('CHOMP',True, (255,0,0))
    surf.blit(text, (((screen_width/2)-tile_size*2) , (screen_height/2)-tile_size*3.5))

running=True
background= screen.copy()
draw_background(background)

for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*1.5), random.randint(0, screen_height - tile_size * 2)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.blit(background, (0,0))

    fishes.update()
    #check if any fish is off screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            random.randint(0, screen_height - tile_size * 2)))

    fishes.draw(screen)
    pygame.display.flip()
    clock.tick(150)

pygame.quit()




