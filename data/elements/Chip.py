import pygame as pg


class Chip:
    def __init__(self, color, x, y):
        self.width = 200
        self.height = 150
        self.color = color
        self.isBlock = False
        self.x = x
        self.y = y

    def draw_chip(self, surf):
        pg.draw.rect(surf, self.color, (self.x, self.y, self.width, self.height))

