import pygame
import sys
from Dot.Dot import Dot
from Constant.Constant import *
from Game.Game import *
pygame.init()

# Khởi tạo màn hình
clock = pygame.time.Clock()

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

    screen.fill(BLACK)
    game.draw_grid(screen)
    #game.draw_lines()
    game.draw_dots(screen)

    pygame.display.flip()
    clock.tick(60)
