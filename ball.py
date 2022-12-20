from variables import *

<<<<<<< HEAD
'''
Данная часть кода отвечает за действия со снарядами.
'''
class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        '''
        Инициализация снаряда.
        screen: экран программы
        x: абцисса центра снаряда
        y: ордината центра снаряда
        '''
        self.screen = screen # экран, на котором существует снаряд
        self.x = x # абцисса центра снаряда
        self.y = y # ордината центра снаряда
        self.r = 5 # радиус снаряда
        self.vx = 0 # начальная горизонтальная скорость снаряда (до запуска из пушки)
        self.vy = 0 # начальная вертикальная скорость снаряда (до запуска из пушки)
        self.color = RED # цвет снаряда
        self.live = 300 # время жизни снаряда (в сек*FPS)

    def move(self):
        '''
        Функция перемещения снаряда.
        '''
        # изменение координат снаряда
        self.x += self.vx
        self.y += self.vy

        # обработка столкновений снаряда со стенами
=======
class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = RED
        self.live = 150

    def move(self):
        self.x += self.vx
        self.y += self.vy

>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
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

<<<<<<< HEAD
        # уменьшение запаса жизни снаряда
=======
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
        if (self.live < 0):
            balls.pop(balls.index(self))
        else:
            self.live -= 1

    def draw(self):
<<<<<<< HEAD
        '''
        Функция отрисовки снаряда.
        '''
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), self.r, 1)

    def hittest(self, tank):
        '''
        Функция проверки столкновения снаряда с танком. Возвращает True при столкновении, False иначе.
        tank: танк, с которым проверяется столкновение
        '''
        if (self.x > tank.x and self.x < tank.x + tank.width and
            self.y > tank.y and self.y < tank.y + tank.height):
=======
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
        if (self.x > obj.x and self.x < obj.x + obj.width and
            self.y > obj.y and self.y < obj.y + obj.height):
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
            return True
        else:
            return False

def circle_draw(screen, color, x, y, r):
<<<<<<< HEAD
    '''
    Функция отрисовки круга с заданными параметрами (используется для отрисовки вражеских снарядов).
    screen: экран, на котором рисуется снаряд
    color: цвет снаряда
    x: абцисса центра снаряда
    y: ордината центра снаряда
    r: радиус снаряда
    '''
    pygame.draw.circle(screen, color, (x, y), r)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), r, 1)
=======
    pygame.draw.circle(screen, color, (x, y), r)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), r, 1)
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
