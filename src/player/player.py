import pygame as pg

class Player:
    def __init__(self, x_pos: float, y_pos: float):
        self.pos = pg.Vector2(x_pos, y_pos)

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.circle(screen, "red", self.pos, 40)

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