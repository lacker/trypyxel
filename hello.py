import pyxel
import random

pyxel.init(160, 120)


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw():
    pyxel.cls(0)
    x = random.randint(0, 160)
    y = random.randint(0, 120)
    color = random.randint(0, 15)
    pyxel.rect(x, y, 25, 20, color)


pyxel.run(update, draw)
