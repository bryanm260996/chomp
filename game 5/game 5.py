import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import draw_background
from player import Player

#initialize pygame
pygame.init()

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('adding a player fish on the screen')
clock= pygame.time.Clock()

running=True
background= screen.copy()
draw_background(background)

for _ in range(3):
    fishes.add(Fish(random.randint(screen_width, screen_width*1.5), random.randint(0, screen_height - tile_size * 2)))

#create a player fish
player = Player(screen_width/2, screen_height/2)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        #control fish with keyboard
        player.stop()

        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_UP:
                print('you pressed up key')
                player.move_up()
            if event.key == pygame.K_DOWN:
                print('you pressed down key')
                player.move_down()
            if event.key == pygame.K_LEFT:
                print('you pressed left key')
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print('you pressed right key')
                player.move_right()
#DRAW BACKGROUND
    screen.blit(background, (0, 0))
    #DRAW GREEN FISH
    fishes.update()
    player.update()
#check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            random.randint(0, screen_height - tile_size * 2)))
#draw green fish
    fishes.draw(screen)
#draw player fish
    player.draw(screen)

    pygame.display.flip()
    clock.tick(150)

pygame.quit()
sys.exit