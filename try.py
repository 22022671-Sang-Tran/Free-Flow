import pygame
import sys

# Define colors
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "orange": (255, 165, 0),
    "light_blue": (173, 216, 230),
    "pink": (255, 182, 193),
    "maroon": (128, 0, 0),
    "purple": (128, 0, 128),
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "light_green": (144, 238, 144),
    "beige": (245, 245, 220),
    "dark_blue": (0, 0, 139),
    "teal": (0, 128, 128),
    "dark_pink": (139, 0, 139),
}

# Initialize Pygame
pygame.init()

# Set up display
width, height = 100, 100
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Grid")

# Cell class
class Cell(pygame.sprite.Sprite):
    def __init__(self, color, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * size, y * size)

# Create grid
grid_size = 5
cell_size = width // grid_size

grid = []
for row in range(grid_size):
    for col in range(grid_size):
        color_name = "white"  # Set default color
        cell = Cell(colors.get(color_name, (255, 255, 255)), col, row, cell_size)
        grid.append(cell)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the grid
    screen.fill((255, 255, 255))  # Background color
    for cell in grid:
        screen.blit(cell.image, cell.rect.topleft)

    pygame.display.flip()
