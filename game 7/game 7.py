import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import draw_background, add_fish, add_enemies
from player import Player
from enemy import Enemy, enemies

#initialize pygame
pygame.init()

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('adding a player fish on the screen')
clock= pygame.time.Clock()

running=True
background= screen.copy()
draw_background(background)
# draw fish
add_fish(5)

#for _ in range(400):
    #fishes.add(Fish(random.randint(screen_width, screen_width*1.5), random.randint(0, screen_height - tile_size * 2)))

#draw enemies
add_enemies(5)

#create a player fish
player = Player(screen_width/2, screen_height/2)

#initialize score
score= 0
score_font= pygame.font.Font('../assets/fonts/DERSIRA.ttf', 60)
text= score_font.render(f'{score}',True, (255,0,0))

#load sound effects
scream= pygame.mixer.Sound('../assets/sounds/chomp.wav')
hurt= pygame.mixer.Sound('../assets/sounds/hurt.wav')
bubbles= pygame.mixer.Sound('../assets/sounds/bubbles.wav')

#ADD ALTERNATE FISH IMAGE
life_icon= pygame.image.load('../assets/sprites/orange_fish_alt.png').convert()
life_icon.set_colorkey((0,0,0))
#SET NUMBER OF LIVES
lives=NUM_LIVES


while lives > 0 and running:
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
    enemies.update()

    #check for player and green fish collisions

    result=pygame.sprite.spritecollide(player, fishes, True)
    #print(result)
    if result: #if it is not empty
        #play sound
        pygame.mixer.Sound.play(scream)
        score += len(result)
        print(score)
    # draw more green fish
        add_fish(len(result))
        #for _ in range(len(result)):
            #fishes.add(Fish(random.randint(screen_width, screen_width * 1.5),
                            #random.randint(0, screen_height - tile_size * 2)))
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result: #if it is not empty
        #play sound
        pygame.mixer.Sound.play(hurt)
        lives-=1
        score -= len(result)
        print(score)
    # draw more  fish
        add_enemies(len(result))

    #check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            add_fish(1)
            #fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            #random.randint(0, screen_height - tile_size * 2)))
    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)
            add_enemies(1)
#draw green fish
    fishes.draw(screen)
    enemies.draw(screen)
#draw player fish
    player.draw(screen)
    # draw score on screen

#draw score
    text = score_font.render(f'{score}', True, (255, 0, 0))
    screen.blit(text, (screen_width - tile_size, 0))
#draw lives in lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i*tile_size, screen_height-tile_size))

    pygame.display.flip()
    clock.tick(80)


#CREATE NEW BACKGROUND WHEN GAME OVER
screen.blit(background, (0, 0))


#SHOW GAME OVER MESSAGE and FINAL SCORE
message = score_font.render('GAME OVER', True, (255,0,0))
screen.blit(message,(screen_width/2- message.get_width()/2, screen_height/2 - message.get_height()/2))
score_text= score_font.render(f'score{score}', True, (255,255,0))
screen.blit(score_text, (screen_width/2- message.get_width()/2, screen_height/2 - message.get_height()/2))

#update display

pygame.display.flip()

#WAIT FOR USER TO EXIT GAME

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




