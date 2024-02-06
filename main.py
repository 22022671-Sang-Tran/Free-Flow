import pygame
import sys
from Dot.Dot import Dot
from Line.Line import Line
from Constant.Constant import *
pygame.init()

# Khởi tạo màn hình
clock = pygame.time.Clock()

class Game:
    def __init__(self, level_file):
        self.dots = []
        self.lines = []
        self.load_level(level_file)
        self.selected_dot = None

    def load_level(self, level_file):
        with open(level_file, 'r') as file:
            lines = file.readlines()

        # Parse the number of rows and columns
        self.num_cols, self.num_rows = map(int, lines[0].split())

        for row in range(self.num_rows):
            for col, char in enumerate(lines[row + 1].strip()):
                if char != ' ':
                    color = self.get_color(char)
                    if color:
                        self.dots.append(Dot(row, col, color))

    def get_color(self, char):
        color_mapping = {
            'R': RED,
            'G': GREEN,
            'B': BLUE,
            'Y': YELLOW
        }
        return color_mapping.get(char)

    def draw_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    def draw_dots(self):
        for dot in self.dots:
            dot.draw(screen)
# Specify the path to your level file
level_file_path = "test.txt"

# Create the game
game = Game(level_file_path)

# Parse the number of rows and columns from the first line of the file
with open(level_file_path, 'r') as file:
    num_cols, num_rows = map(int, file.readline().split())

# Create the Pygame display window
screen = pygame.display.set_mode((num_cols * CELL_SIZE, num_rows * CELL_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            col = mouse_pos[0] // CELL_SIZE
            row = mouse_pos[1] // CELL_SIZE

            #for dot in game.dots:
            #    if dot.row == row and dot.col == col:
            #        game.connect_dots(dot)

    screen.fill(BLACK)
    game.draw_grid()
    #game.draw_lines()
    game.draw_dots()

    pygame.display.flip()
    clock.tick(60)
