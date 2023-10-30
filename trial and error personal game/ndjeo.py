import pygame
import os

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Image")

# Load image
image = pygame.image.load(os.path.join('../assets/sprites/person_walking.jpg'))
image_width, image_height = image.get_rect().width, image.get_rect().height

# Create a class for the moving image
class MovingImage:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

# Initial position of the image
moving_image = MovingImage(100, 100, image)

# Set up variables for movement
vel = 5
is_running = True

clock = pygame.time.Clock()

# Main game loop
while is_running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()

    # Move the image based on key presses
    if keys[pygame.K_LEFT]:
        moving_image.move(-vel, 0)
    if keys[pygame.K_RIGHT]:
        moving_image.move(vel, 0)
    if keys[pygame.K_UP]:
        moving_image.move(0, -vel)
    if keys[pygame.K_DOWN]:
        moving_image.move(0, vel)

    # Refresh the screen
    win.fill((0, 0, 0))  # Fill the screen with black color
    moving_image.draw(win)  # Draw the image

    pygame.display.update()

pygame.quit()