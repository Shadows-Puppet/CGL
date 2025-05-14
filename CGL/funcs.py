import pygame
from collections import Counter
import presets as pr

def draw_map(cells, screen, cell_size):
    for i, j in cells:
        pygame.draw.rect(screen, "white", (cell_size * j, cell_size * i, cell_size, cell_size))

def draw_outline(screen, cell_size, outline):
    mouse_pos = pygame.mouse.get_pos()
    points = None
    if outline == 'glider':
        points = pr.glider
    elif outline == 'gun':
        points = pr.gun
    for i, j in points:
        pygame.draw.rect(screen, "yellow",
                         (cell_size * (mouse_pos[0] // cell_size + j), cell_size * (mouse_pos[1] // cell_size + i),
                          cell_size, cell_size))

def add_preset(cells, cell_size, outline):
    mouse_pos = pygame.mouse.get_pos()
    points = None
    if outline == 'glider':
        points = pr.glider
    elif outline == 'gun':
        points = pr.gun
    for i, j in points:
        cells.add((mouse_pos[1] // cell_size + i,mouse_pos[0] // cell_size + j))
    return cells

def count_neighbors(cells, i, j):
    return sum(
        (i + dx, j + dy) in cells
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if not (dx == 0 and dy == 0)
    )

def update_cells(cells):
    neighbor_counts = Counter()

    for i,j in cells:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighbor = (i + dx, j + dy)
                neighbor_counts[neighbor] += 1

    new_cells = set()

    for cell, count in neighbor_counts.items():
        if count == 3 or (count == 2 and cell in cells):
            new_cells.add(cell)

    return new_cells