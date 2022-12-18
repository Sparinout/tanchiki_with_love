import pygame
import numpy as np
import math

WIDTH = 1500
HEIGHT = 800
FPS = 120
GREY = 0x7D7D7D
RED = 0xFF0000

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