from ball import *

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 50
        self.f2_on = 0
        self.an = 1
        self.h = 10
        self.l = 60
        self.color = GREY

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event, x, y):
        if len(balls) < 10:
            new_ball = Ball(self.screen, x, y)
            new_ball.vx = 10 * math.cos(self.an)
            new_ball.vy = 10 * math.sin(self.an)
            balls.append(new_ball)

    def targetting(self, m_x, m_y, x, y):
        self.an = math.atan2((m_y - y), (m_x - x))

    def draw(self, x, y):
        pygame.draw.polygon(self.screen, self.color,
                            [[x - self.h / 2 * np.sin(self.an), y + self.h / 2 * np.cos(self.an)],

                             [x - self.h / 2 * np.sin(self.an) + self.l * np.cos(self.an),
                              y + self.h / 2 * np.cos(self.an) + self.l * np.sin(self.an)],

                             [x + self.h / 2 * np.sin(self.an) + self.l * np.cos(self.an),
                              y - self.h / 2 * np.cos(self.an) + self.l * np.sin(self.an)],

                             [x + self.h / 2 * np.sin(self.an), y - self.h / 2 * np.cos(self.an)]])

