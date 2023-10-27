import pygame

IMAGE_PATH = "../assets/sprites/person_walking.jpg"

class MovingJumpingImage:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_jumping = False

    def move(self, dx):
        self.x += dx

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = -10  # Adjust this value for jump height
            self.is_jumping = True

    def update(self):
        if self.is_jumping:
            self.y += self.velocity_y
            self.velocity_y += -9.8  # Adjust for gravity

            if self.y >= HEIGHT - self.image.get_height():
                self.y = HEIGHT - self.image.get_height()
                self.is_jumping = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving and Jumping Image")

# Create a MovingJumpingImage object
image = MovingJumpingImage(100, 300, IMAGE_PATH)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                image.jump()

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image.move(-5)
    if keys[pygame.K_RIGHT]:
        image.move(5)

    # Update the image's position
    image.update()

    # Update the screen
    screen.fill(BG_COLOR)
    image.draw(screen)
    pygame.display.update()

    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()