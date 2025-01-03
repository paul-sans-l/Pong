import random
import pygame

class Ball:
    def __init__(self, x, y, radius,height):
        self.x = x
        self.y = y
        self.radius = radius
        self.image_rect = None
        self.color = (255, 255, 255)  # White
        self.dx = 5 *(random.choice([1, -1]))  # Randomly choose initial direction
        self.dy = 5  *(random.choice([1, -1]))  # Randomly choose initial direction
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.height = height

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def drawDirection(self, screen):
        arrow_image = pygame.image.load("Object/Arrow.png")
        arrow_image = pygame.transform.scale(arrow_image, (50, 50))
        
        # Determine the angle based on the direction of the ball
        if self.dx > 0 and self.dy > 0:
            angle = -45  # (1, 1)
        elif self.dx < 0 and self.dy > 0:
            angle = -135  # (-1, 1)
        elif self.dx > 0 and self.dy < 0:
            angle = 45  # (1, -1)
        elif self.dx < 0 and self.dy < 0:
            angle = 135  # (-1, -1)
        
        rotated_image = pygame.transform.rotate(arrow_image, angle)
        self.image_rect = rotated_image.get_rect(center=(self.x + 10*self.dx, self.y + 10*self.dy))
        screen.blit(rotated_image, self.image_rect.topleft)

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Update rect for collision detection
        self.rect.topleft = (self.x - self.radius, self.y - self.radius)

        # Bounce off top and bottom walls
        if self.y - self.radius <= 0 or self.y + self.radius >= self.height:
            self.dy = -self.dy

    def reverse_direction(self):
        self.dx = -self.dx
    def get_direction_rect(self):
        return self.image_rect


class Stick:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)  # White
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dy, screen_height):
        # Update position
        self.y += dy

        # Keep the stick within screen bounds
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > screen_height:
            self.y = screen_height - self.height

        # Update rect for collision detection
        self.rect.topleft = (self.x, self.y)


class Limit:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)  # Red
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Score:
    def __init__(self, x, y, font_size):
        self.x = x
        self.y = y
        self.value = 0 # Initial score
        self.font = pygame.font.Font("Font/Pixeltype.ttf", font_size)
        self.color = (255, 255, 255)

    def draw(self, screen):
        text = self.font.render(str(self.value), True, self.color)
        screen.blit(text, (self.x, self.y))
    def increment(self):
        self.value += 1
    def getvalue(self):
        return self.value
class Button:
    def __init__(self, x, y, width, height, text, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.Font("Font/Pixel Game.otf", font_size)
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load("Object/download (1).png")
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, screen):
        # Create a temporary surface to combine the image and text
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        temp_surface.blit(self.image, (0, 0))
        
        # Render the text
        text = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width//2 + 20, self.height//2 + 55))
        temp_surface.blit(text, text_rect)
        
        # Blit the combined surface onto the screen
        screen.blit(temp_surface, self.rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)