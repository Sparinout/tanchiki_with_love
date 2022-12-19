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
        self.speed = 12
        self.width = 30
        self.height = 30
        self.color = RED

    def move(self):
        # Если движение происходит только в одном направлении, то оно происходит со скоростью self.speed
        if self.right_on + self.left_on + self.up_on + self.down_on == 1:
            if self.right_on:
                self.x += self.speed
            if self.left_on:
                self.x -= self.speed
            if self.up_on:
                self.y -= self.speed
            if self.down_on:
                self.y += self.speed
        # Если танк одновременно двигается в двух направлениях, то его модуль скорости должен остаться
        # равным self.speed, поэтому скорость движения в каждом направлении делится на sqrt(2)
        elif self.right_on + self.left_on + self.up_on + self.down_on > 1:
            if self.right_on:
                self.x += self.speed * 0.7071
            if self.left_on:
                self.x -= self.speed * 0.7071
            if self.up_on:
                self.y -= self.speed * 0.7071
            if self.down_on:
                self.y += self.speed * 0.7071

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
        pygame.draw.circle(screen, self.color, (self.x + self.width / 2, self.y + self.height / 2), min(self.width, self.height) / 3)