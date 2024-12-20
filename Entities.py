
import pygame

class Ball:
    def __init__(self, x, y, radius,height):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 255, 255)  # White
        self.dx = 5  # Horizontal velocity
        self.dy = 5  # Vertical velocity
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.height = height

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

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
