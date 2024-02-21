# Dot.py
from Constant.Constant import *
import pygame


class Dot:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def isDot(self):
        return isinstance(self, Dot)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.col * CELL_SIZE + CELL_SIZE // 2, self.row * CELL_SIZE + CELL_SIZE // 2),
                           CELL_SIZE // 2.5)
