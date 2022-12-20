import pygame
import numpy as np
import math
<<<<<<< HEAD
import time

'''
В этом файле собраны переменные, которые используются в различных частях кода.
'''
WIDTH = 1400  # ширина экрана
HEIGHT = 700  # высота экрана
FPS = 60 # FPS игры

# кодировка цветов
=======

WIDTH = 1500
HEIGHT = 700
FPS = 60
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
GREY = 0x7D7D7D
RED = 0xFF0000
BLUE = 0x0000FF

<<<<<<< HEAD
# начальное положение мыши по х и у
mouse_x = 0
mouse_y = 0

balls = [] # список снарядов
tanks = [] # список танков
guns = [] # список пушек

ball_speed = 8 # модуль скорости снарядов

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # экран
pygame.init() # иницилизация pygame
clock = pygame.time.Clock()
finished = False # флаг завершения программы
number_of_tanks = 2 # количество танков

# объявление используемых в коде шрифтов
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 60)
f3 = pygame.font.Font(None, 24)

# начальный счёт игроков
score_first_player = 0
score_second_player = 0
=======
mouse_x = 0
mouse_y = 0

balls = []
tanks = []
guns = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
clock = pygame.time.Clock()
finished = False
number_of_tanks = 2

f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 60)
f3 = pygame.font.Font(None, 24)
score_first_player = 0
score_second_player = 0
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
