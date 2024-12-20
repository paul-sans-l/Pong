import pygame
import sys
import Entities

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Remastered")

# Colors

a = 12
b = 150 
c = 128
# Entities
ball = Entities.Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20,SCREEN_HEIGHT)  
stick1 = Entities.Stick(10, SCREEN_HEIGHT // 2, 50, 150)
stick2 = Entities.Stick(SCREEN_WIDTH - 60, SCREEN_HEIGHT // 2, 50, 150)
limit1 = Entities.Limit(-3, 50 // 2, 5, SCREEN_HEIGHT - 50)  
limit2 = Entities.Limit(SCREEN_WIDTH - 3, 50 // 2, 5, SCREEN_HEIGHT - 50)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    BACKGROUND_COLOR = (a, b, c)

    keys = pygame.key.get_pressed()

    # Paddle control for stick2
    if keys[pygame.K_o]:
        stick2.move(-5, SCREEN_HEIGHT)  # Move up
    if keys[pygame.K_l]:
        stick2.move(5, SCREEN_HEIGHT)   # Move down

    # Paddle control for stick1
    if keys[pygame.K_w]:
        stick1.move(-5, SCREEN_HEIGHT)  # Move up
    if keys[pygame.K_s]:
        stick1.move(5, SCREEN_HEIGHT)   # Move down

    # Ball movement
    ball.update()  

    # Check collisions with sticks
    if ball.rect.colliderect(stick1.rect):
      a = min(max(a + 15, 10), 230)
      b = min(max(b + 32, 10), 230)
      c = min(max(c + 40, 10), 230)
      ball.reverse_direction()  # Example: Reverse ball's direction on collision

    if ball.rect.colliderect(stick2.rect):
     a = min(max(a - 10, 10), 230)
     b = min(max(b - 17, 10), 230)
     c = min(max(c - 20, 10), 230)
     print("Special event: Ball touched Stick 2!")
     ball.reverse_direction()

# Check collisions with limits
    if ball.rect.colliderect(limit1.rect):
     a = min(max(a + 15, 10), 230)
     b = min(max(b + 5, 10), 230)
     c = min(max(c - 20, 10), 230)
     print("Special event: Ball touched Left Limit!")
     ball.reverse_direction()

    if ball.rect.colliderect(limit2.rect):
      a = min(max(a + 5, 10), 230)
      b = min(max(b + 5, 10), 230)
      c = min(max(c + 10, 10), 230)
      print("Special event: Ball touched Right Limit!")
      ball.reverse_direction()


    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    ball.draw(screen)
    stick1.draw(screen)
    stick2.draw(screen)
    limit1.draw(screen)
    limit2.draw(screen)

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)
