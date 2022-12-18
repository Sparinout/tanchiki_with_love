from variables import *

class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = RED
        self.live = 240

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.y + self.r >= HEIGHT and self.vy > 0:
            self.vy = -self.vy
            self.y = HEIGHT - self.r
        if self.x + self.r >= WIDTH and self.vx >= 0:
            self.vx = -self.vx
            self.x = WIDTH - self.r
        if self.x - self.r <= 0 and self.vx <= 0:
            self.vx = -self.vx
            self.x = self.r
        if self.y - self.r <= 0 and self.vy <= 0:
            self.vy = -self.vy
            self.y = self.r

        if (self.live < 0):
            balls.pop(balls.index(self))
        else:
            self.live -= 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (self.x, self.y),
            self.r, 1)

    def hittest(self, obj):
        if ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2) ** 0.5 <= (self.r + obj.r):
            return True
        else:
            return False

