import pygame
import random
import sys

from game_parameters import *
from healthy_food import Shake, shakes, Yogurt, yogurts
from background import draw_background, add_shake, add_enemies, add_yogurt, add_enemies2, add_enemies3
from player import Player
from enemy import Enemy, enemies, enemies2, enemies3

#initialize pygame
pygame.init()

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('adding a player fish on the screen')
clock= pygame.time.Clock()

running=True
background= screen.copy()
draw_background(background)
# draw fish
add_shake(1)
add_yogurt(1)
#draw enemies
add_enemies(1)
add_enemies2(1)
add_enemies3(1)

#create a player
player = Player(screen_width/2, screen_height/2)

#initialize score
score= 10
score_font= pygame.font.Font('../assets/fonts/DERSIRA.ttf', 50)
text= score_font.render(f'{score}',True, (255,0,0))
if score <10:
    score_font = pygame.font.Font('../assets/fonts/DERSIRA.ttf', 50)
    text = score_font.render(f'{score}', True, (255, 0, 0))

#load sound effects
eat_sound= pygame.mixer.Sound('../assets/sounds/chomp.wav')
ew_sound=pygame.mixer.Sound('../assets/sounds/MITCH.wav')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        #control player with keyboard
        player.stop()

        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_UP:
                player.jump()
            if event.key == pygame.K_DOWN:
                player.down()


#DRAW BACKGROUND
    screen.blit(background, (0, 0))
    #DRAW items
    shakes.update()
    player.update()
    enemies.update()
    yogurts.update()
    enemies2.update()
    enemies3.update()

    #check for player collisions with items

    result=pygame.sprite.spritecollide(player, shakes, True)
    #print(result)
    if result:
        #play sound
        pygame.mixer.Sound.play(eat_sound)
        score += 1
        print(score)
    # draw more  core_powers
        add_shake(len(result))
        player.image=player.celebratory_image

    result = pygame.sprite.spritecollide(player, yogurts, True)

    if result:  # if it is not empty
        # play sound
        pygame.mixer.Sound.play(eat_sound)
        score += 1
        print(score)
        # draw more  core_powers
        add_yogurt(len(result))
        player.image=player.celebratory_image


    result = pygame.sprite.spritecollide(player, enemies, True)
    if result: #if it is not empty
        #play sound
        pygame.mixer.Sound.play(ew_sound)
        score -= 1
        print(score)
    # draw more  fish
        add_enemies(len(result))
        player.image=player.hurt

    result = pygame.sprite.spritecollide(player, enemies2, True)
    if result:
        #play sound
        pygame.mixer.Sound.play(ew_sound)
        score -= 1
        print(score)
    # draw more items
        add_enemies2(len(result))
        player.image = player.hurt
    result = pygame.sprite.spritecollide(player, enemies3, True)
    if result:
        #play sound
        pygame.mixer.Sound.play(ew_sound)
        score -= 1
        print(score)
    # draw more items
        add_enemies3(len(result))
        player.image = player.hurt

    #check if any fish is off the screen
    for shake in shakes:
        if shake.rect.y > 600:
            shakes.remove(shake)
            add_shake(1)
            #fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            #random.randint(0, screen_height - tile_size * 2)))
    for yogurt in yogurts:
        if yogurt.rect.y > 600:
            yogurts.remove(yogurt)
            add_yogurt(1)

    for enemy in enemies:
        if enemy.rect.y > 600:
            enemies.remove(enemy)
            add_enemies(1)

    for enemy2 in enemies2:
        if enemy2.rect.y > 600:
            enemies2.remove(enemy2)
            add_enemies2(1)
    for enemy3 in enemies3:
        if enemy3.rect.x < 0:
            enemies3.remove(enemy3)
            add_enemies3(1)

#draw green fish
    shakes.draw(screen)
    enemies.draw(screen)
    yogurts.draw(screen)
    enemies2.draw(screen)
    enemies3.draw(screen)
#draw player fish
    player.draw(screen)
    # draw score on screen

    text = score_font.render(f'{score}', True, (255, 255, 255))
    screen.blit(text, (screen_width/2, tile_size))

    pygame.display.flip()
    clock.tick(80)

pygame.quit()
sys.exit