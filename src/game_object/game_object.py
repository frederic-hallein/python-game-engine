import pygame as pg

from res.colors import GREEN

class GameObject:
    def __init__(self, x_pos: float, y_pos: float):
        self.pos = pg.Vector2(x_pos, y_pos)

    # TODO : import screen_surface from somewhere else
    def update(self, dt: float, screen_surface: pg.surface) -> None:
        self.draw(screen_surface)
        self.move(dt)

    def draw(self, screen_surface: pg.Surface) -> None:
        pg.draw.circle(screen_surface, GREEN, self.pos, 40)

    def move(self, dt: float) -> None:
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.pos.y -= 300 * dt
        if keys[pg.K_s]:
            self.pos.y += 300 * dt
        if keys[pg.K_q]:
            self.pos.x -= 300 * dt
        if keys[pg.K_d]:
            self.pos.x += 300 * dt