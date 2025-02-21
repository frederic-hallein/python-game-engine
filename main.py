import pygame as pg
from pygame.locals import *

from src.scene.scene import Scene
from src.game_object.player.player import Player

from res.colors import *

background_colors = {K_r: RED, K_b: BLUE}

if __name__ == "__main__":
    pg.init()
    screen_width, screen_height = 900, 600
    screen = Scene(screen_width, screen_height)
    pg.display.set_caption("Game Engine")
    clock = pg.time.Clock()
    running = True
    dt = 0

    player_start_x_pos = screen_height  / 2
    player_start_y_pos = screen_height / 2
    player = Player(player_start_x_pos, player_start_y_pos)

    background = WHITE
    while running:
        for event in pg.event.get():
            if event.type == QUIT: running = False
            if event.type == KEYDOWN:
                if event.key in background_colors:
                    background = background_colors[event.key]

        screen.update(background)
        player.update(dt, screen.surface)

        pg.display.update()
        dt = clock.tick(60) / 1000

    pg.quit()