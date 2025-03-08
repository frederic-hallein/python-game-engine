import pygame as pg

from pygame.locals import *

from src.game_object.player.player import Player
from src.game_object.wall.wall import Wall
from src.game.scene.scene import Scene
from src.game.fps.fps import FPS

from res.colors import *

background_colors = {K_r: RED, K_b: BLUE}
class Game:
    global background_colors

    def __init__(self) -> None:
        # init PyGame
        pg.init()
        pg.display.set_caption("Game Engine")

        # init FPS
        self._fps = FPS(60)

        # init scene
        self._scene = Scene()

        # init game objects
        self._player = Player(0, 0)
        self._walls = [
            Wall(100, 100),
            Wall(300, 300)
        ]

    def __del__(self) -> None:
        pg.quit()
    
    def run(self) -> None:
        dt = 0
        background = WHITE

        running = True
        while running:
            for event in pg.event.get():
                if event.type == QUIT: running = False
                # if event.type == KEYDOWN:
                #     if event.key in background_colors:
                #         background = background_colors[event.key]

            # update
            self._player.update(dt)

            # draw
            self._scene.fill(background)
            for wall in self._walls:
                wall.draw(self._scene.surface)
            self._player.draw(self._scene.surface)

            pg.display.update()
            dt = self._fps.dt

