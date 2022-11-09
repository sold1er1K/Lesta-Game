import pygame as pg
from data.utils.utils import print_text


class Button:
    def __init__(self, message, width, height, fsize):
        self.width = width
        self.height = height
        self.inactive_clr = (0, 0, 200)
        self.active_clr = (0, 0, 175)
        self.message = message
        self.fsize = fsize
        self.x = 0
        self.y = 0

    def is_active(self):
        mouse = pg.mouse.get_pos()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            return True
        else:
            return False

    def draw(self, surface, x, y, indentX, indentY):
        self.x = x
        self.y = y

        if self.is_active():
            pg.draw.rect(surface, self.active_clr, (x, y, self.width, self.height))
        else:
            pg.draw.rect(surface, self.inactive_clr, (x, y, self.width, self.height))

        print_text(surface, self.message, x + indentX, y + indentY, font_size=self.fsize)

