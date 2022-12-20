from variables import *

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

        # уменьшение запаса жизни снаряда
        if (self.live < 0):
            balls.pop(balls.index(self))
        else:
            self.live -= 1

    def draw(self):
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
            return True
        else:
            return False

def circle_draw(screen, color, x, y, r):
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
