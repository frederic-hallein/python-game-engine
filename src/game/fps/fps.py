import pygame as pg

class FPS:
    def __init__(self, fps_limit: int):
        self._fps_limit = fps_limit
        self._clock = pg.time.Clock()

    @property
    def dt(self) -> float:
        return self._clock.tick(self._fps_limit) / 1000

