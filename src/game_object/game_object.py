import pygame as pg
from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, x: float, y: float, vx: float=0, vy: float=0, ax: float=0, ay: float=0, width: int=50, height: int=50):
        self._r = pg.Vector2(x, y)
        self._v = pg.Vector2(vx, vy)
        self._a = pg.Vector2(ax, ay)
        self._width = width
        self._height = height
        self._rect = pg.Rect(x, y, width, height)

    def apply_force(self, fx, fy) -> None:
        self._a += pg.Vector2(fx, fy)
        
    @abstractmethod
    def update(self):
        """Update object state"""
        pass
        
    @abstractmethod
    def draw(self, scene_surface: pg.Surface):
        """Draw object onto scene surface"""
        pass

    @property
    def rect(self) -> pg.Rect:
        return self._rect
