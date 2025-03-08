import pygame as pg

from res.colors import BLUE

from src.game_object.game_object import GameObject

class Wall(GameObject):
    def __init__(self, x: float, y: float, vx: float=0, vy: float=0, ax: float=0, ay: float=0, width: int=50, height: int=50):
        super().__init__(x, y, vx, vy, ax, ay, width, height)
        self._color = BLUE

    def update(self, dt: float) -> None:
        pass

    def draw(self, scene_surface: pg.Surface) -> None:
        pg.draw.rect(scene_surface, self._color, self._rect)
