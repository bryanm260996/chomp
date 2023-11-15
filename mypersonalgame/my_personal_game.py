import pygame
import random
import sys

from game_parameters import *
from healthy_food import Shake, shakes, Yogurt, yogurts
from background import draw_background, add_shake, add_enemies, add_yogurt, add_enemies2, add_enemies3,  draw_background2
from player import Player
from enemy import Enemy, enemies, enemies2, enemies3

#initialize pygame
pygame.init()

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('adding a player on the screen')
clock= pygame.time.Clock()

running=True
background= screen.copy()
draw_background(background)
# draw items
add_shake(1)
add_yogurt(1)
#draw enemies
add_enemies(1)
add_enemies2(1)
add_enemies3(1)



#create a player
player = Player(screen_width/2, screen_height/2)

#initialize score
score= 0

score_font= pygame.font.Font('../assets/fonts/DERSIRA.ttf', 50)
text= score_font.render(f'{score}',True, (255,0,0))
fast_font=pygame.font.Font('../assets/fonts/DERSIRA.ttf', 40)


#load sound effects
eat_sound= pygame.mixer.Sound('../assets/sounds/chomp.wav')
ew_sound=pygame.mixer.Sound('../assets/sounds/MITCH.wav')
lives= 1
while lives > 0 and running:
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
        lives -=1
        print(score)
    # draw more  enemies
        add_enemies(len(result))
        player.image=player.hurt

    result = pygame.sprite.spritecollide(player, enemies2, True)
    if result:
        #play sound
        pygame.mixer.Sound.play(ew_sound)
        score -= 1
        lives -= 1
        print(score)
    # draw more items
        add_enemies2(len(result))
        player.image = player.hurt
    result = pygame.sprite.spritecollide(player, enemies3, True)
    if result:
        #play sound
        pygame.mixer.Sound.play(ew_sound)
        score -= 1
        lives -= 1
        print(score)
    # draw more items
        add_enemies3(len(result))
        player.image = player.hurt

    #check if any items is off the screen
    for shake in shakes:
        if shake.rect.y > 600:
            shakes.remove(shake)
            add_shake(1)

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
        if enemy3.rect.x < -600:
            enemies3.remove(enemy3)
            add_enemies3(1)


#draw items
    shakes.draw(screen)
    enemies.draw(screen)
    yogurts.draw(screen)
    enemies2.draw(screen)
    enemies3.draw(screen)


#draw player
    player.draw(screen)
#create a font to give messages while player is playing
    custom_font = pygame.font.Font('../assets/fonts/DERSIRA.ttf', 30)
    # draw score on screen and make it change color depending on score
    if score <0:
        score=0
        clock.tick(60)


    elif score < 2:

        clock.tick(60)
        intro = custom_font.render('EAT HEALTHY FOODS AND AVOID JUNK FOOD', True, (255, 255, 255))
        screen.blit(intro, (70, 550))


    elif score <5:

        text = score_font.render(f'{score}', True, (255, 255, 0))
        clock.tick(65)
    elif score <8:
        text = score_font.render(f'{score}', True, (255, 255, 0))
        clock.tick(70)
    elif score <10:
        text = score_font.render(f'{score}', True, (0, 255, 0))
        clock.tick(75)
    elif score <12:
        text = score_font.render(f'{score}', True, (0, 255, 0))
        clock.tick(80)
    else:
        text = score_font.render(f'{score}', True, (0, 255, 0))
        clock.tick(100)


# draws the score on the screen
    screen.blit(text, (screen_width/2, tile_size))
# draw the number of lives on top of the screen
    for i in range(lives):
        screen.blit(player.small_celebratory_image, (i*20, 10))

    pygame.display.flip()
    #clock.tick(60)

#CREATE NEW BACKGROUND WHEN GAME OVER
screen.blit(background, (0, 0))


#SHOW GAME OVER MESSAGE and FINAL SCORE
draw_background2(background)
screen.blit(background, (0, 0))
#message = score_font.render('GAME OVER', True, (255,0,0))
#screen.blit(message,(screen_width/2- message.get_width()/2, screen_height/2 - message.get_height()/2))
score_text= score_font.render(f' Final Score: {score}', True, (255,0,0))
screen.blit(score_text, (250,340))

#update display

pygame.display.flip()

#WAIT FOR USER TO EXIT GAME
run_background=True
while run_background:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_RIGHT:
                    break


