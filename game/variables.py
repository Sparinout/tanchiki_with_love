import pygame
import numpy as np
import math
import time

'''
В этом файле собраны переменные, которые используются в различных частях кода.
'''
WIDTH = 1400  # ширина экрана
HEIGHT = 700  # высота экрана
FPS = 60 # FPS игры

# кодировка цветов
GREY = 0x7D7D7D
RED = 0xFF0000
BLUE = 0x0000FF

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
