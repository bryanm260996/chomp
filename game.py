import pygame
import sys

#Initialize Pygame:
pygame.init()

#screen dimensions:

screen_width=800
screen_height=600

#define colors
BLUE=(0,0,255)
BROWN=(224,161,52)

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Blue background with brown rectangle')

#MAIN LOOP

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    #fill screen with blue
    screen.fill(BLUE)

    #draw the bottom rectangle
    rectangle_height=200
    pygame.draw.rect(screen, BROWN, (0,screen_height-rectangle_height, screen_width, rectangle_height))

    #update display

    pygame.display.flip()

pygame.quit()


