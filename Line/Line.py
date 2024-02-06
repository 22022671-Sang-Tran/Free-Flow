import pygame
from Constant.Constant import *
class Line:
    def __init__(self, start_dot, end_dot, line_color):
        self.start_dot = start_dot
        self.end_dot = end_dot
        self.line_color = line_color

    def draw(self,screen):
        pygame.draw.line(screen, self.line_color, (self.start_dot.col * CELL_SIZE + CELL_SIZE // 2, self.start_dot.row * CELL_SIZE + CELL_SIZE // 2),
                         (self.end_dot.col * CELL_SIZE + CELL_SIZE // 2, self.end_dot.row * CELL_SIZE + CELL_SIZE // 2), 5)
