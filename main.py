import sys
import pygame as pg
from data.elements.Button import Button
from data.utils.utils import load_png, sound_play, pause_music, load_music, print_text
from data.elements.Chip import Chip
import json


WIDTH = 1920
HEIGHT = 1080
FPS = 60

pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Lesta Test Game')
clock = pg.time.Clock()
button_click_sound = pg.mixer.Sound('data/audio/button.wav')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def Menu(music):
    surface = pg.Surface((WIDTH, HEIGHT))
    surface.blit(load_png('menu.jpg'), (0, 0))
    if music:
        load_music('menu.mp3', 0.3, -1)
    pg.mouse.set_visible(True)
    display = True
    startGameButton = Button('Start Game', 700, 140, 140)
    controlButton = Button('Control', 480, 140, 140)
    exitButton = Button('Exit', 280, 140, 140)
    while display:
        window.blit(surface, (0, 0))
        startGameButton.draw(surface, 610, 400, 28, 14)
        controlButton.draw(surface, 720, 600, 22, 14)
        exitButton.draw(surface, 820, 800, 18, 12)
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
    backButton = Button('Back', 180, 80, 80)
    display = True
    while display:
        window.blit(surf, (0, 0))
        pg.draw.rect(surf, BLACK, (250, 200, 1160, 680), 4)
        pg.draw.rect(surf, (0, 0, 190), (254, 204, 1152, 672))
        print_text(surf, 'Key Assignment', 580, 120, WHITE, 'data/fonts/main.ttf', 80)
        pg.draw.line(surf, BLACK, [250, 336], [1406, 336], 4)
        pg.draw.line(surf, BLACK, [250, 472], [1406, 472], 4)
        pg.draw.line(surf, BLACK, [250, 608], [1406, 608], 4)
        pg.draw.line(surf, BLACK, [250, 744], [1406, 744], 4)
        pg.draw.line(surf, BLACK, [840, 204], [840, 876], 4)
        backButton.draw(surf, 1500, 800, 14, 8)
        print_text(surf, 'KEY', 480, 230, WHITE, 'data/fonts/table.ttf', 90)
        print_text(surf, 'UP ARROW', 430, 370, WHITE, 'data/fonts/table.ttf', 70)
        print_text(surf, 'Move a chip up', 970, 370, WHITE, 'data/fonts/table.ttf', 70)
        print_text(surf, 'DOWN ARROW', 410, 650, WHITE, 'data/fonts/table.ttf', 70)
        print_text(surf, 'Move a chip down', 940, 650, WHITE, 'data/fonts/table.ttf', 70)
        print_text(surf, 'LEFT ARROW', 410, 510, WHITE, 'data/fonts/table.ttf', 70)
        print_text(surf, 'Move a chip to the left', 880, 510, WHITE, 'data/fonts/table.ttf', 70)
        print_text(surf, 'RIGHT ARROW', 400, 790, WHITE, 'data/fonts/table.ttf', 70)
        print_text(surf, 'Move a chip to the right', 875, 790, WHITE, 'data/fonts/table.ttf', 70)
        print_text(surf, 'DESCRIPTION', 950, 230, WHITE, 'data/fonts/table.ttf', 90)
        print_text(surf, 'click on the left mouse button to choose a chip', 240, 880, WHITE, 'data/fonts/table.ttf', 80)
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
    load_music('ingame.mp3', 0.5, -1)
    with open('data/levels/level_1.json') as f:
        map = json.load(f)
    level_map = createChipMap(map)
    surface = pg.Surface((WIDTH, HEIGHT))
    surface.blit(load_png('menu.jpg'), (0, 0))
    gameZone = pg.Surface((750, 750))
    gameZone.fill((169, 169, 169))
    backButton = Button('Back', 180, 80, 80)
    display = True
    activeBorder = False
    while display:
        pg.draw.rect(surface, BLACK, (300, 150, 770, 770), 10)
        for element in level_map:
            for chip in level_map[element]:
                chip.draw(gameZone)
        surface.blit(gameZone, (310, 160))
        backButton.draw(surface, 1500, 500, 14, 8)

        window.blit(surface, (0, 0))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backButton.is_active():
                        sound_play(button_click_sound)
                        display = False
                        Menu(1)
                    for element in level_map:
                        for chip in level_map[element]:
                            if chip.is_active() and not activeBorder:
                                chip.switch_border()
                                activeBorder = True
                            elif chip.is_active() and chip.border and activeBorder:
                                chip.switch_border()
                                activeBorder = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    for element in level_map:
                        for chip in level_map[element]:
                            if chip.border:
                                stop = False
                                ind = level_map[element].index(chip) - 1
                                if chip.x != 0 and level_map[element][ind].filename == 'nothing.jpg':
                                    temp = chip.x
                                    chip.x = level_map[element][ind].x
                                    level_map[element][ind].x = temp
                                else:
                                    stop = True
                                if not stop:
                                    temp = level_map[element][ind]
                                    level_map[element][ind] = level_map[element][ind + 1]
                                    level_map[element][ind + 1] = temp
                elif event.key == pg.K_RIGHT:
                    for element in level_map:
                        for chip in level_map[element]:
                            if chip.border:
                                stop = False
                                ind = level_map[element].index(chip) + 1
                                if chip.x != 600 and level_map[element][ind].filename == 'nothing.jpg':
                                    temp = chip.x
                                    chip.x = level_map[element][ind].x
                                    level_map[element][ind].x = temp
                                else:
                                    stop = True
                                if not stop:
                                    list = []
                                    ind = level_map[element].index(chip)
                                    if ind > 0:
                                        for i in range(ind):
                                            list.append(level_map[element][i])
                                        list.append(level_map[element][ind + 1])
                                        list.append(level_map[element][ind])
                                        for i in range(ind + 2, 5):
                                            list.append(level_map[element][i])
                                    else:
                                        list.append(level_map[element][ind + 1])
                                        list.append(level_map[element][ind])
                                        for i in range(ind + 2, 5):
                                            list.append(level_map[element][i])
                                    level_map[element] = list
                elif event.key == pg.K_UP:
                    for element in level_map:
                        for chip in level_map[element]:
                            if chip.border:
                                stop = False
                                ind = level_map[element].index(chip)
                                ind_y = str(int(element) - 1)
                                if chip.y != 0 and level_map[ind_y][ind].filename == 'nothing.jpg':
                                    temp = chip.y
                                    chip.y = level_map[ind_y][ind].y
                                    level_map[ind_y][ind].y = temp
                                else:
                                    stop = True
                                if not stop:
                                    temp = level_map[element][ind]
                                    level_map[element][ind] = level_map[ind_y][ind]
                                    level_map[ind_y][ind] = temp
                elif event.key == pg.K_DOWN:
                    count = 0
                    for element in level_map:
                        if count == 0:
                            for chip in level_map[element]:
                                if chip.border:
                                    stop = False
                                    ind = level_map[element].index(chip)
                                    ind_y = str(int(element) + 1)
                                    if chip.y != 600 and level_map[ind_y][ind].filename == 'nothing.jpg':
                                        temp = chip.y
                                        chip.y = level_map[ind_y][ind].y
                                        level_map[ind_y][ind].y = temp
                                    else:
                                        stop = True
                                    if not stop:
                                        ind = level_map[element].index(chip)
                                        ind_y = str(int(element) + 1)
                                        r = level_map[element][ind]
                                        d = level_map[ind_y][ind]

                                        level_map[ind_y][ind] = r
                                        level_map[element][ind] = d
                                        count += 1


def GetName(char):
    name = ''
    if char == 'o':
        name = 'orange.jpg'
    elif char == 'y':
        name = 'yellow.jpg'
    elif char == 'r':
        name = 'red.jpg'
    elif char == 'b':
        name = 'block.jpg'
    elif char == 'n':
        name = 'nothing.jpg'
    return name


def createChipMap(map):
    new_map = {}
    for element in map:
        index = 0
        list = []
        for value in map[element]:
            list.append(Chip(GetName(value), 150 * index, 150 * (int(element) - 1)))
            index += 1
        new_map[element] = list
    return new_map


def GetChipByCoords(x, y):
    x_index = x / 150
    y_index = y / 150
    if x_index > int(x_index):
        x_index = int(x_index) + 1
    if y_index > int(y_index):
        y_index = int(y_index) + 1
    return int(x_index), str(int(y_index + 1))


def Quit():
    sys.exit()


if __name__ == '__main__':
    Menu(1)