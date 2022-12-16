import random
import math
import pygame
from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import sys


pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'sub-c-b641520a-0eb7-4a51-8513-1e483f229b87'
pnconfig.publish_key = 'pub-c-a7f07719-20f5-4334-8d5b-c340b995d609'
pnconfig.user_id = "Bogdan"
pubnub = PubNub(pnconfig)

class MySubscribeCallback(SubscribeCallback):
    def message(self, pubnub, message):
        print(message.publisher, ':', message.message)

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('my_channel').execute()
pubnub.publish().channel('my_channel').message(input()).sync


WIDTH = 2000
HEIGHT = 1800
FPS = 60
GREY = 0x7D7D7D
RED = 0xFF0000

class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса Ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = RED
        self.live = 15

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy
        и стен по краям окна (размер окна 800х600).
        """

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
            self.r
        )
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (self.x, self.y),
            self.r, 1
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        # return False
        if ((obj.x - self.x)**2 + (obj.y - self.y)**2)**0.5 <= (self.r + obj.r):
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event, tank0):
        new_ball = Ball(self.screen, tank0.x, tank0.y)
        new_ball.r = 10
        new_ball.vx = (self.f2_power) * math.cos(self.an)
        new_ball.vy = (self.f2_power) * math.sin(self.an)
        balls.append(new_ball)

        self.f2_power = 10
        self.f2_on = 0

    def targetting(self, m_x, m_y, x, y):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((m_y - y), (m_x - x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self, x, y):
        pygame.draw.line(self.screen, self.color, (x, y), (x + (80 + self.f2_power) * math.cos(self.an), y + (80 + self.f2_power) * math.sin(self.an)), 15)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


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

    def right_1(self):
        self.right_on = 1

    def right_0(self):
        self.right_on = 0

    def left_1(self):
        self.left_on = 1

    def left_0(self):
        self.left_on = 0

    def up_1(self):
        self.up_on = 1

    def up_0(self):
        self.up_on = 0

    def down_1(self):
        self.down_on = 1

    def down_0(self):
        self.down_on = 0

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


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = False

number_of_tanks = 2
player = 0

tanks = []
guns = []

for i in range(number_of_tanks):
    t = Tank(screen)
    tanks.append(t)
    t.draw()
    g = Gun(screen)
    guns.append(g)

#tank = Tank(screen)
#tank.draw()


balls = []
#gun = Gun(screen)
mouse_x = 0
mouse_y = 0

while not finished:
    clock.tick(FPS)
    screen.fill((255, 255, 255))

    for i in range (number_of_tanks):
        tanks[i].draw()
        guns[i].draw(tanks[i].x + 15, tanks[i].y + 15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                tanks[player].right_1()
            if event.key == pygame.K_a:
                tanks[player].left_1()
            if event.key == pygame.K_w:
                tanks[player].up_1()
            if event.key == pygame.K_s:
                tanks[player].down_1()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                tanks[player].right_0()
            if event.key == pygame.K_a:
                tanks[player].left_0()
            if event.key == pygame.K_w:
                tanks[player].up_0()
            if event.key == pygame.K_s:
                tanks[player].down_0()
        if event.type == pygame.MOUSEBUTTONDOWN:
            guns[player].fire2_start()
        if event.type == pygame.MOUSEBUTTONUP:
            guns[player].fire2_end(event, tanks[player])
        if event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

    guns[player].power_up()

    if (tanks[player].x + 30 >= WIDTH):
        tanks[player].right_0()
        tanks[player].x -= 1
    if (tanks[player].x <= 0):
        tanks[player].left_0()
        tanks[player].x += 1
    if (tanks[player].y + 30 >= HEIGHT):
        tanks[player].down_0()
        tanks[player].y -= 1
    if (tanks[player].y <= 0):
        tanks[player].up_0()
        tanks[player].y += 1

    tanks[player].move()
    tanks[player].draw()
    guns[player].targetting(mouse_x, mouse_y, tanks[player].x, tanks[player].y)

    print(tanks[player].x, tanks[player].y)

    for b in balls:
        b.move()
        b.draw()
    pygame.display.update()

pygame.quit()