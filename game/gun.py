from ball import *

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
        pygame.draw.polygon(self.screen, self.color,
                            [[x - self.h / 2 * np.sin(self.an), y + self.h / 2 * np.cos(self.an)],

                             [x - self.h / 2 * np.sin(self.an) + self.l * np.cos(self.an),
                              y + self.h / 2 * np.cos(self.an) + self.l * np.sin(self.an)],

                             [x + self.h / 2 * np.sin(self.an) + self.l * np.cos(self.an),
                              y - self.h / 2 * np.cos(self.an) + self.l * np.sin(self.an)],

                             [x + self.h / 2 * np.sin(self.an), y - self.h / 2 * np.cos(self.an)]])
