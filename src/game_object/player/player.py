import pygame as pg

from src.game_object.game_object import GameObject

class Player(GameObject):
    def __init__(self, x_pos: float, y_pos: float, screen_surface: pg.surface):
        super().__init__(x_pos, y_pos, screen_surface)

    def move(self, dt: float) -> None:
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self._pos.y -= 500 * dt
        if keys[pg.K_s]:
            self._pos.y += 500 * dt
        if keys[pg.K_q]:
            self._pos.x -= 500 * dt
        if keys[pg.K_d]:
            self._pos.x += 500 * dt

