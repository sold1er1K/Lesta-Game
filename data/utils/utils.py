import os
import pygame as pg
import json
pg.mixer.init()


def load_png(filename):
    fullpath = os.path.join(os.path.dirname(__file__), '..', 'graphics', filename)
    if not os.path.exists(fullpath):
        raise FileNotFoundError('File not found: {}'.format(fullpath))

    image = pg.image.load(fullpath)
    if image.get_alpha is None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    return image


def print_text(surface, message, x, y, font_color=(255, 255, 255), font_type='data/fonts/main.ttf', font_size=80):
    font_type = pg.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    surface.blit(text, (x, y))


def sound_play(sound):
    sound.play()
    pg.time.delay(300)


def pause_music():
    pg.mixer.music.pause()


def load_music(name, volume, repeat):
    pg.mixer.music.load(f'data/audio/{name}')
    pg.mixer.music.set_volume(volume)
    pg.mixer.music.play(repeat)
