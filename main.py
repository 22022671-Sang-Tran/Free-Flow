import sys
from Line.Line import *
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

is_dragging = False
start_dot = None
end_dot = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            col = mouse_pos[0] // CELL_SIZE
            row = mouse_pos[1] // CELL_SIZE
            clicked_dot = None
            for dot in game.dots:
                if dot.col == col and dot.row == row:
                    clicked_dot = dot
                    start_dot = dot
                    is_dragging = True
                    break
            if clicked_dot:
                print(f"{col} and {row} and {clicked_dot.color}\n")
        elif event.type == pygame.MOUSEMOTION:
            # Check if dragging a line
            if is_dragging:
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0] // CELL_SIZE
                row = mouse_pos[1] // CELL_SIZE

                # Create a temporary end dot at the current mouse position
                end_dot = Dot(row, col, WHITE)
        elif event.type == pygame.MOUSEBUTTONUP:
            # End dragging
            if is_dragging:
                is_dragging = False

                # Check if the end dot is on a valid position
                if end_dot and (end_dot.row != start_dot.row or end_dot.col != start_dot.col):
                    # Create a line between start and end dot
                    line_color = start_dot.color
                    line = Line(start_dot, end_dot)
                    game.lines.append(line)

                    # Reset start and end dots
                    start_dot = None
                    end_dot = None

    screen.fill(BLACK)
    game.draw_grid(screen)
    # game.draw_lines()
    game.draw_dots(screen)

    pygame.display.flip()
    clock.tick(60)
