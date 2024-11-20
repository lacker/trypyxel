import random
import pyxel

SCREEN_SIZE = 300
THING_SIZE = 10
MAX_POS = SCREEN_SIZE - THING_SIZE
H_SPEED = 3
V_SPEED = 3


class Thing:
    def __init__(self):
        self.x = random.randint(0, MAX_POS)
        self.y = 0
        self.dx = 0


class App:
    def __init__(self):
        pyxel.init(SCREEN_SIZE, SCREEN_SIZE, title="Thing Dropper")
        self.static = []
        self.active = Thing()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.active.dx = H_SPEED
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.active.dx = -H_SPEED
        if pyxel.btnr(pyxel.KEY_RIGHT) and self.active.dx > 0:
            self.active.dx = 0
        if pyxel.btnr(pyxel.KEY_LEFT) and self.active.dx < 0:
            self.active.dx = 0

        self.active.x += self.active.dx
        if self.active.x < 0:
            self.active.x = 0
        elif self.active.x > MAX_POS:
            self.active.x = MAX_POS

        self.active.y += V_SPEED
        if self.active.y >= MAX_POS:
            self.active.y = MAX_POS
            self.things.append(self.active)
            self.active = Thing()

    def draw(self):
        pyxel.cls(0)
        for thing in self.static:
            pyxel.rect(thing.x, thing.y, THING_SIZE, THING_SIZE, 8)
        pyxel.rect(self.active.x, self.active.y, THING_SIZE, THING_SIZE, 7)


App()
