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

        # Столкновение танка со стенами
        if self.x + self.width >= WIDTH:
            self.right_on = 0
            self.x -= 1
        if self.x <= 0:
            self.left_on = 0
            self.x += 1
        if self.y + self.height >= HEIGHT:
            self.down_on = 0
            self.y -= 1
        if self.y <= 0:
            self.up_on = 0
            self.y += 1

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
    def draw_turret(self):
        pygame.draw.circle(screen, RED, (self.x + self.width / 2, self.y + self.height / 2), min(self.width, self.height) / 3)
