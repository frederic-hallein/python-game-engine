import pygame as pg
from src.player.player import Player

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((900, 600))
    clock = pg.time.Clock()
    running = True
    dt = 0

    player_start_x_pos = screen.get_width() / 2
    player_start_y_pos = screen.get_height() / 2
    player = Player(player_start_x_pos, player_start_y_pos)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill("white")

        player.draw(screen)
        player.move(dt)

        pg.display.flip()
        dt = clock.tick(60) / 1000

    pg.quit()