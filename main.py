import sys
import pygame as pg
from data.elements.Button import Button
from data.utils.utils import load_png, sound_play, pause_music, load_music, print_text
from data.elements.Chip import Chip
import json


WIDTH = 1200
HEIGHT = 800
FPS = 60

pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Lesta Test Game')
clock = pg.time.Clock()
button_click_sound = pg.mixer.Sound('data/audio/button.wav')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (238, 192, 252)


def Menu(music):
    surface = pg.Surface((WIDTH, HEIGHT))
    surface.blit(load_png('menu.jpg'), (0, 0))
    if music:
        load_music('menu.mp3', 0.3, -1)
    pg.mouse.set_visible(True)
    display = True
    startGameButton = Button('Start Game', 410, 90)
    controlButton = Button('Control', 290, 90)
    exitButton = Button('Exit', 180, 90)
    while display:
        window.blit(surface, (0, 0))
        startGameButton.draw(surface, 395, 250, 20, 12)
        controlButton.draw(surface, 455, 380, 20, 12)
        exitButton.draw(surface, 510, 510, 20, 12)
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                display = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if startGameButton.is_active():
                    sound_play(button_click_sound)
                    display = False
                    pause_music()
                    Round()
                elif controlButton.is_active():
                    sound_play(button_click_sound)
                    display = False
                    About()

                elif exitButton.is_active():
                    sound_play(button_click_sound)
                    Quit()
        clock.tick(FPS)
    pg.quit()


def About():
    surf = pg.Surface((WIDTH, HEIGHT))
    surf.blit(load_png('menu.jpg'), (0, 0))
    backButton = Button('Back', 180, 80)
    display = True
    while display:
        window.blit(surf, (0, 0))
        pg.draw.rect(surf, BLACK, (20, 100, 1160, 680), 4)
        pg.draw.rect(surf, PURPLE, (24, 104, 1152, 672))
        print_text(surf, 'Key Assignment', 20, 20, WHITE, 'data/fonts/main.ttf', 80)
        pg.draw.line(surf, BLACK, [20, 180], [1176, 180], 4)
        pg.draw.line(surf, BLACK, [20, 300], [1176, 300], 4)
        pg.draw.line(surf, BLACK, [20, 420], [1176, 420], 4)
        pg.draw.line(surf, BLACK, [20, 540], [1176, 540], 4)
        pg.draw.line(surf, BLACK, [20, 660], [1176, 660], 4)
        pg.draw.line(surf, BLACK, [406, 100], [406, 776], 4)
        backButton.draw(surf, 1000, 10, 14, 8)
        print_text(surf, 'KEY', 160, 100, BLACK, 'data/fonts/table.ttf', 90)
        print_text(surf, 'UP ARROW', 120, 210, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'Move a chip up', 640, 210, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'DOWN ARROW', 90, 330, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'Move a chip down', 610, 330, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'LEFT ARROW', 90, 450, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'Move a chip to the left', 540, 450, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'RIGHT ARROW', 80, 570, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'Move a chip to the right', 535, 570, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'MOUSE LEFT KEY', 60, 690, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'Choose a chip', 640, 690, BLACK, 'data/fonts/table.ttf', 70)
        print_text(surf, 'DESCRIPTION', 624, 100, BLACK, 'data/fonts/table.ttf', 90)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if backButton.is_active():
                    sound_play(button_click_sound)
                    display = False
                    Menu(0)


def Round():
    chipList = []
    with open('data/levels/level1.json') as f:
        levelMap = json.load(f)
    load_music('ingame.mp3', 0.5, -1)
    surf = pg.Surface((WIDTH, HEIGHT))
    surf.blit(load_png('menu.jpg'), (0, 0))
    gameZone = pg.Surface((1000, 750))
    gameZone.fill((238, 192, 252))
    pg.draw.rect(surf, BLACK, (10, 15, 1020, 770), 10)
    for element in levelMap:
        index = 0
        for value in levelMap[element]:
            chipList.append(Chip(convertToColor(value), 20 + 200 * index, 25 + 150 * (int(element) - 1)))
            index += 1
    display = True
    while display:
        surf.blit(gameZone, (20, 25))
        for element in chipList:
            element.draw_chip(surf)
        window.blit(surf, (0, 0))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


def convertToColor(char):
    if char == 'o':
        return (255, 127, 0)
    elif char == 'y':
        return (255, 255, 0)
    elif char == 'r':
        return (255, 0, 0)
    elif char == 'b':
        return (100, 100, 100)
    elif char == 'n':
        return (238, 192, 252)


def Quit():
    sys.exit()


if __name__ == '__main__':
    Menu(1)
