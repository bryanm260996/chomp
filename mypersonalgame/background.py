import pygame
from game_parameters import * #to import all
import random
from healthy_food import Shake, shakes, Yogurt, yogurts
from enemy import Enemy, enemies, Enemy2, enemies2, Enemy3, enemies3
def draw_background(surf):
    king_hall= pygame.image.load('../assets/sprites/Dining_Hall.jpeg').convert() #CONVERT ALLOWS TO MAKE BACKGROUND TRANSPARENT
    king_hall.set_colorkey((0,0,0))

    custom_font = pygame.font.Font('../assets/fonts/DERSIRA.ttf', 60)

    #fill the screen with water
    surf.blit(king_hall, (0,0))  #SCREEN.BLIT IS TO PASTE IT ON THE ORIGINAL


    #DRAW TEXT


    text= custom_font.render('DINING KING',True, (255,255,255))
    surf.blit(text, (((screen_width/2)-tile_size*2.8) , (screen_height/2)-tile_size*4.5))

    # Draw a white rectangle at the bottom of the screen and a gray rectangle on top
    blue_bottom_rect = pygame.Rect(0, screen_height-100, screen_width, 200)
    pygame.draw.rect(surf, (0, 13, 192), blue_bottom_rect)

    gold_bottom_rect = pygame.Rect(0, screen_height-200, screen_width, 100)
    pygame.draw.rect(surf, (255, 188, 0), gold_bottom_rect)

def draw_background2(surf):
    custom_font = pygame.font.Font('../assets/fonts/DERSIRA.ttf', 100)
    white_bottom_rect = pygame.Rect(0, 0, screen_width, 800)
    pygame.draw.rect(surf, (255, 255, 255), white_bottom_rect)
    custom_font_small= pygame.font.Font('../assets/fonts/DERSIRA.ttf', 50)

    text = custom_font.render('GAME OVER', True, (255, 0, 0))
    surf.blit(text, (80, 200))
    play_again= custom_font_small.render("Press 'Y' to restart ", True, (255, 0, 0))
    surf.blit(play_again, (190, 400))


def add_shake (num_shake):
    for _ in range(num_shake):
        shakes.add(Shake(random.randint(10, 790),
                        random.randint(10, 20)))

def add_yogurt (num_yogurt):
    for _ in range(num_yogurt):
        yogurts.add(Yogurt(random.randint(10,790),
                        random.randint(0,20)))

def add_enemies (num_enemies):
    for _ in range(num_enemies):
        enemies.add(Enemy(random.randint(10,790),
                        random.randint(0, 20)))

def add_enemies2 (num_enemies2):
    for _ in range(num_enemies2):
        enemies2.add(Enemy2(random.randint(10,790),
                        random.randint(0, 400)))

def add_enemies3 (num_enemies3):
    for _ in range(num_enemies3):
        enemies3.add(Enemy3(random.randint(800,1000),
                        random.randint(400, 600)))


