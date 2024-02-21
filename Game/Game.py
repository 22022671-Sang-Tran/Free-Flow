from Dot.Dot import *


def get_color(char):
    color_mapping = {
        'R': RED,
        'G': GREEN,
        'B': BLUE,
        'Y': YELLOW,
        'C': CYAN,
        'O': ORANGE,
        'V': VIOLET,
        'P': PINK
    }
    return color_mapping.get(char)


class Game:
    def __init__(self, level_file):
        self.num_rows = None
        self.num_cols = None
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
                if char != '.':
                    color = get_color(char)
                    if color:
                        self.dots.append(Dot(row, col, color))

    def draw_grid(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    def draw_dots(self, screen):
        for dot in self.dots:
            dot.draw(screen)
