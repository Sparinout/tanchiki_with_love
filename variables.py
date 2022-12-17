import pygame
import numpy as np
import math

WIDTH = 1700
HEIGHT = 1000
FPS = 60
GREY = 0x7D7D7D
RED = 0xFF0000

balls = []
tanks = []
guns = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))