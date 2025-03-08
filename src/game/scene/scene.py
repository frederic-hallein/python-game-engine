import pygame as pg

class Scene:
    def __init__(self):
        self._width  = 900
        self._height = 600
        self._surface = pg.display.set_mode((self._width, self._height))

    def fill(self, background_color: str) -> None:
        self._surface.fill(background_color)

    @property
    def surface(self) -> pg.Surface:
        return self._surface
    
    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height

    
