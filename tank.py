from variables import *

class Tank:
    def __init__(self, screen):
        self.screen = screen
        self.x = WIDTH // 2 - 30 // 2
        self.y = HEIGHT // 2 - 30 // 2
        self.right_on = 0
        self.left_on = 0
        self.up_on = 0
        self.down_on = 0
        self.speed = 6
        self.width = 30
        self.height = 30

    def move(self):
        if self.right_on:
            self.x += self.speed
        if self.left_on:
            self.x -= self.speed
        if self.up_on:
            self.y -= self.speed
        if self.down_on:
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 30, 30))
