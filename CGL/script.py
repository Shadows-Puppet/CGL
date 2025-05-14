# Example file showing a circle moving on screen
import pygame
import funcs


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
pause = False
outline = ''
cells = set()
cell_size = 10
cells.add((0,0))
cells.add((1,1))
cells.add((2,1))
cells.add((1,2))
cells.add((0,2))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                cell_size = min(cell_size + 1, 100)
            elif event.y < 0:
                cell_size = max(cell_size - 1, 1)
        elif event.type == pygame.MOUSEBUTTONDOWN and pause:
            if event.button == 1:
                if outline != '':
                    cells = funcs.add_preset(cells, cell_size, outline)
                    outline = ''
                else:
                    mouse_pos = pygame.mouse.get_pos()
                    cells.add((mouse_pos[1] // cell_size, mouse_pos[0] // cell_size))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            elif event.key == pygame.K_g:
                outline = 'glider'
            elif event.key == pygame.K_s:
                outline = 'gun'
    # fill the screen with a color to wipe away anything from last frame

    if not pause:
        cells = funcs.update_cells(cells)
    funcs.draw_map(cells, screen, cell_size)
    if outline != '':
        funcs.draw_outline(screen, cell_size, outline)
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(10) / 1000

pygame.quit()