import pygame as pg

from res.colors import GREEN

class GameObject:
    def __init__(self, x_pos: float, y_pos: float, screen_surface: pg.surface) -> None:
        self._pos = pg.Vector2(x_pos, y_pos)
        self._screen_surface = screen_surface

    def update(self, dt: float) -> None:
        self.draw(self._screen_surface)
        self.move(dt)

    def draw(self, screen_surface: pg.Surface) -> None:
        pg.draw.circle(screen_surface, GREEN, self._pos, 40)

    def move(self, dt: float) -> None:
        pass