import pygame
import sys
from mygame_parameters import *

def draw_background(surf):
    window = pygame.display.set_mode((window_width, window_height))

    # Load your background image
    background_image = pygame.image.load(
        "../assets/sprites/NavalAcademy.jpg")  # Replace "your_image.png" with the path to your image

    # Blit the background image onto the window
    window.blit(background_image, (0, 0))










