import pygame
pygame.init()

info = pygame.display.Info()
MONITOR_WIDTH = info.current_w
MONITOR_HEIGHT = info.current_h

DESIGN_WIDTH = 1200
DESIGN_HEIGHT = 800

scale_x = MONITOR_WIDTH / DESIGN_WIDTH
scale_y = MONITOR_HEIGHT / DESIGN_HEIGHT
SCALE = min(scale_x, scale_y)

WIDTH = int(DESIGN_WIDTH * SCALE)
HEIGHT = int(DESIGN_HEIGHT * SCALE)

ENEMY_FORCE = 4
SHOOT_DELAY = 150
FPS = 60
WHITE = (154, 164, 166)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
