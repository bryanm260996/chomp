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