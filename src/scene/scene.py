import pygame as pg

class Scene:
    def __init__(self, screen_width: int, screen_height: int):
        self._width  = screen_width
        self._height = screen_height
        self._screen = pg.display.set_mode((self._width, self._height))

    def update(self, color: str) -> None:
        self._screen.fill(color)

    @property
    def surface(self) -> pg.Surface:
        return self._screen
    
    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
