from ball import *

<<<<<<< HEAD
'''
Данная часть кода отвечает за действия с пушкой танка и запуском снарядов.
'''


class Gun:
    def __init__(self, screen):
        '''
        Инициализация пушки
        screen: экран, на котором существует пушка
        '''
        self.screen = screen  # экран, на котором существует пушка
        self.an = 1  # начальный угол наклона пушки
        self.h = 10  # ширина пушки
        self.l = 60  # длина пушки
        self.color = GREY  # цвет пушки

    def fire2_end(self, x, y, speed):
        '''
        Функция выстрела из пушки.
        x: абсцисса точки появления снаряда
        y: ордината точки появления снаряда
        speed: скорость снаряда
        '''
        if len(balls) < 10:  # на экране присутствует не более 10 снарядов одного игрока
            new_ball = Ball(self.screen, x, y)
            new_ball.vx = speed * math.cos(self.an)  # рассчёт горизонтальной скорости снаряда
            new_ball.vy = speed * math.sin(self.an)  # рассчёт вертикальной скорости снаряда
            balls.append(new_ball)

    def targetting(self, m_x, m_y, x, y):
        '''
        Функция наведения пушки на курсор. Высчитывает угол пушки с горизонтом в зависимости от входных параметров.
        m_x: абсцисса курсора
        m_y: ордината курсора
        x: абсцисса основания пушки
        y: ордината основания пушки
        '''
        self.an = math.atan2((m_y - y), (m_x - x))

    def draw(self, x, y):
        '''
        Функция отрисовки пушки
        x: абсцисса основания пушки
        y: ордината основания пушки
        '''
=======
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
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
        pygame.draw.polygon(self.screen, self.color,
                            [[x - self.h / 2 * np.sin(self.an), y + self.h / 2 * np.cos(self.an)],

                             [x - self.h / 2 * np.sin(self.an) + self.l * np.cos(self.an),
                              y + self.h / 2 * np.cos(self.an) + self.l * np.sin(self.an)],

                             [x + self.h / 2 * np.sin(self.an) + self.l * np.cos(self.an),
                              y - self.h / 2 * np.cos(self.an) + self.l * np.sin(self.an)],

                             [x + self.h / 2 * np.sin(self.an), y - self.h / 2 * np.cos(self.an)]])
<<<<<<< HEAD
=======

>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
