import random
import sys
import pygame

from background import draw_background
from game_parameters import *

pygame.init()

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('collecting events')

#main loop
running=True
background= screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_UP:
                print('you pressed up key')
            if event.type == pygame.K_DOWN:
                print('you pressed down key')
    screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit