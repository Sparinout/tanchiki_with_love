from variables import *

<<<<<<< HEAD
'''
Данная часть кода отвечает за действия с танками.
'''
class Tank:
    def __init__(self, screen):
        '''
        Инициализация танка.
        screen: экран, на котором существует танк
        '''
        self.screen = screen # экран, на котором существует танк
        # 4 атрибута, отвечающие за движение танка в четырёх направлениях
=======
class Tank:
    def __init__(self, screen):
        self.screen = screen
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
        self.right_on = 0
        self.left_on = 0
        self.up_on = 0
        self.down_on = 0
<<<<<<< HEAD
        self.speed = 5 # скорость танка
        self.width = 50 # ширина танка
        self.height = 50 # высота танка
        self.x = 5 # начальная обсцисса танка
        self.y = HEIGHT - self.height - 5 # начальная ордината танка
        # примечание: координатами х и у танка являются координаты его левого верхнего угла
        self.color = RED # цвет танка (точнее, его башни)

    def move(self):
        '''
        Функция движения танка.
        '''
        # если движение происходит только в одном направлении, то оно происходит со скоростью self.speed
=======
        self.speed = 6
        self.width = 50
        self.height = 50
        self.x = 5
        self.y = HEIGHT - self.height - 5
        self.color = RED

    def move(self):
        # Если движение происходит только в одном направлении, то оно происходит со скоростью self.speed
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
        if self.right_on + self.left_on + self.up_on + self.down_on == 1:
            if self.right_on:
                self.x += self.speed
            if self.left_on:
                self.x -= self.speed
            if self.up_on:
                self.y -= self.speed
            if self.down_on:
                self.y += self.speed
<<<<<<< HEAD
        # если танк одновременно двигается в двух направлениях, то модуль его скорости должен остаться
=======
        # Если танк одновременно двигается в двух направлениях, то его модуль скорости должен остаться
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
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

<<<<<<< HEAD
        # столкновение танка со стенами
=======
        # Столкновение танка со стенами
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
        if self.x + self.width >= WIDTH:
            self.right_on = 0
            self.x = WIDTH - self.width - 1
        if self.x <= 0:
            self.left_on = 0
            self.x = 1
        if self.y + self.height >= HEIGHT:
            self.down_on = 0
            self.y = HEIGHT - self.height - 1
        if self.y <= 0:
            self.up_on = 0
            self.y = 1

    def draw(self):
<<<<<<< HEAD
        '''
        Функция отрисовки корпуса танка (всегда чёрный).
        '''
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
    def draw_turret(self):
        '''
        Функция отрисовки башни танка.
        '''
        pygame.draw.circle(screen, self.color, (self.x + self.width / 2, self.y + self.height / 2), min(self.width, self.height) / 3)
=======
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
    def draw_turret(self):
        pygame.draw.circle(screen, self.color, (self.x + self.width / 2, self.y + self.height / 2), min(self.width, self.height) / 3)
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
