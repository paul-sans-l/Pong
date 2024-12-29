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
ball = Entities.Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, SCREEN_HEIGHT)  
stick1 = Entities.Stick(10, SCREEN_HEIGHT // 2, 10, 100)
stick2 = Entities.Stick(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2, 10, 100)
limit1 = Entities.Limit(-3, 50 // 2, 5, SCREEN_HEIGHT - 60)  
limit2 = Entities.Limit(SCREEN_WIDTH - 3, 50 // 2, 5, SCREEN_HEIGHT - 60)
score1 = Entities.Score(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 4 - 100, 100)
score2 = Entities.Score(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 4 - 100, 100)
start = Entities.Button(SCREEN_WIDTH // 2 - 500, SCREEN_HEIGHT // 2 - 500, 1000, 1000, "start", 100)

game_started = False  # Flag to track if the game has started
game_paused = False   # Flag to track if the game is paused
AfterPaused = False
just_started = True

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start.is_clicked(mouse_pos):
                game_started = True
        # Check if the pause button is clicked
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_started:
            game_paused = not game_paused

    BACKGROUND_COLOR = (a, b, c)
    screen.fill(BACKGROUND_COLOR)
    
    if not game_started:
        start.draw(screen)
    else:

        
        font = pygame.font.Font("Font/Pixeltype.ttf", 30)
        text = font.render("Press Space to pause and Resume the game", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH//2 - 190, 100))


        if not game_paused:
            if AfterPaused:
                AfterPaused = False
                font = pygame.font.Font("Font/Pixeltype.ttf", 72)
                for i in range(3, 0, -1):
                    screen.fill(BACKGROUND_COLOR)
                    ball.draw(screen)
                    stick1.draw(screen)
                    stick2.draw(screen)
                    limit1.draw(screen)
                    limit2.draw(screen)
                    score1.draw(screen)
                    score2.draw(screen)
                    ball.drawDirection(screen)
                    text = font.render(str(i), True, (255, 255, 255))
                    screen.blit(text, (SCREEN_WIDTH//2 - 20, SCREEN_HEIGHT//2 - 36))
                    pygame.display.flip()
                    pygame.time.wait(1000)

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
            stick1_collision_area = stick1.rect.inflate(10,50)
            stick2_collision_area = stick2.rect.inflate(10,50)

            if ball.rect.colliderect(stick1_collision_area):
                a = min(max(a + 15, 10), 200)
                b = min(max(b + 32, 10), 200)
                c = min(max(c + 40, 10), 200)
                pygame.mixer.music.load('Sound/bounce2.mp3')
                pygame.mixer.music.play()
                ball.reverse_direction()  # Example: Reverse ball's direction on collision

            if ball.rect.colliderect(stick2_collision_area):
                a = min(max(a - 10, 10), 200)
                b = min(max(b - 17, 10), 200)
                c = min(max(c - 20, 10), 220)
                ball.reverse_direction()
                pygame.mixer.music.load('Sound/bounce2.mp3')
                pygame.mixer.music.play()

            # Check collisions with limits
            if ball.rect.colliderect(limit1.rect):
                a = min(max(a + 15, 10), 200)
                b = min(max(b + 5, 10), 200)
                c = min(max(c - 20, 10), 220)
                score2.increment()
                pygame.mixer.music.load('Sound/bounce.wav')
                pygame.mixer.music.play()

            if ball.rect.colliderect(limit2.rect):
                a = min(max(a + 5, 10), 230)
                b = min(max(b + 5, 10), 220)
                c = min(max(c + 10, 10), 200)
                score1.increment()
                pygame.mixer.music.load('Sound/bounce.wav')
                pygame.mixer.music.play()

            if ball.x > SCREEN_WIDTH - 24 or ball.x< 24:
                ball.reverse_direction()
            # Draw everything
            
            
            
            
            ball.draw(screen)
            stick1.draw(screen)
            stick2.draw(screen)
            limit1.draw(screen)
            limit2.draw(screen)
            score1.draw(screen)
            score2.draw(screen)
            
            if just_started:
                for _ in range(6):  # Blink 3 times
                    ball.draw(screen)
                    stick1.draw(screen)
                    stick2.draw(screen)
                    limit1.draw(screen)
                    limit2.draw(screen)
                    score1.draw(screen)
                    score2.draw(screen)
                    screen.fill(BACKGROUND_COLOR, ball.get_direction_rect())  # Clear only the arrow area
                    pygame.display.flip()
                    pygame.time.wait(500)
                    ball.drawDirection(screen)
                    pygame.display.flip()
                    pygame.time.wait(500)
                just_started = False
        else:
            font = pygame.font.Font("Font/Pixeltype.ttf", 72)
            text = font.render("Game Paused", True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH//2 - 110, SCREEN_HEIGHT//2 ))
            AfterPaused = True

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)
