import pygame as pg
from enum import Enum

from res.colors import RED

from src.game_object.game_object import GameObject
from src.game_object.wall.wall import Wall

class MovementState(Enum):
    IDLE = 0
    MOVING = 1
    ACCELERATING = 2

class Player(GameObject):
    def __init__(self, x: float, y: float, vx: float=0, vy: float=0, ax: float=0, ay: float=0, width: int=50, height: int=50):
        super().__init__(x, y, vx, vy, ax, ay, width, height)
        self._v_max = 5000
        self._a_p = 5000
        self._friction = 4800
        self._state = MovementState.IDLE
        self._color = RED

    def handle_input(self) -> None:
        self._a = pg.Vector2(0, 0)
        keys = pg.key.get_pressed()

        if keys[pg.K_q]:
            self._a.x = -self._a_p
            self._state = MovementState.ACCELERATING
        elif keys[pg.K_d]:
            self._a.x = self._a_p
            self._state = MovementState.ACCELERATING
        else:
            if self._v.x != 0:
                friction_direction = -1 if self._v.x > 0 else 1
                self._a.x = friction_direction * self._friction
                self._state = MovementState.MOVING

        if keys[pg.K_z]:
            self._a.y = -self._a_p
            self._state = MovementState.ACCELERATING
        elif keys[pg.K_s]:
            self._a.y = self._a_p
            self._state = MovementState.ACCELERATING
        else:
            if self._v.y != 0:
                friction_direction = -1 if self._v.y > 0 else 1
                self._a.y = friction_direction * self._friction
                self._state = MovementState.MOVING

    # TODO : fix movement jittering 
    def update(self, dt: float) -> None:
        self.handle_input()

        # TODO : set maximum velocity
        # speed = (self.vx ** 2 + self.vy ** 2) ** 0.5
        # if speed > self.max_speed:
            # scale = self.max_speed / speed
            # self.vx *= scale
            # self.vy *= scale

        self._v += self._a * dt
        self._r += self._v * dt

        self._rect = pg.Rect(self._r.x, self._r.y, self._width, self._height)

        # TODO : update state
        # if abs(self.vx) < 1 and abs(self.vy) < 1:
        #     self.state = MovementState.IDLE
        # elif self.state == MovementState.ACCELERATING:
        #     self.state = MovementState.MOVING

    def draw(self, scene_surface: pg.Surface) -> None:
        pg.draw.rect(scene_surface, self._color, self._rect)
        


