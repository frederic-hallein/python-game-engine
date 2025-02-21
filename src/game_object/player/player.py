import pygame as pg

from src.game_object.game_object import GameObject

class Player(GameObject):
    def __init__(self, x_pos: float, y_pos: float):
        super().__init__(x_pos, y_pos)

