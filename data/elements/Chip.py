import pygame as pg
from data.utils.utils import load_png


class Chip:
    def __init__(self, filename, x, y):
        self.width = 150
        self.height = 150
        self.filename = filename
        self.isBlock = False
        self.isNone = False
        self.x = x
        self.y = y
        self.border = False

    def is_active(self):
        if self.filename != 'block.jpg' and self.filename != 'nothing.jpg':
            mouse = pg.mouse.get_pos()
            x_coord = mouse[0] - 310
            y_coord = mouse[1] - 160
            if self.x < x_coord < self.x + self.width and self.y < y_coord < self.y + self.height:
                return True
            else:
                return False

    def draw(self, surf):
        texture = load_png(self.filename)
        if self.border:
            pg.draw.rect(texture, (0, 255, 255), (0, 0, self.width, self.height), 2)
        surf.blit(texture, (self.x, self.y))

    def switch_border(self):
        if not self.border:
            self.border = True
        else:
            self.border = False

