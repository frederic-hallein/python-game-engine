import pygame as pg

from pygame.locals import *

from src.game_object.player.player import Player
from src.game.scene.scene import Scene
from src.game.fps.fps import FPS

from res.colors import *

background_colors = {K_r: RED, K_b: BLUE}
class Game:
    global background_colors

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Game Engine")
        self._scene = Scene()
        self._fps = FPS(60)

        player_start_x_pos = self._scene.width  / 2
        player_start_y_pos = self._scene.height / 2
        self.player = Player(player_start_x_pos, player_start_y_pos, self._scene.surface)

    def __del__(self) -> None:
        pg.quit()

    def run(self) -> None:
        dt = 0
        background = WHITE
        running = True
        while running:
            for event in pg.event.get():
                if event.type == QUIT: running = False
                if event.type == KEYDOWN:
                    if event.key in background_colors:
                        background = background_colors[event.key]

            self._scene.update(background)
            self.player.update(dt)

            pg.display.update()
            dt = self._fps.dt

