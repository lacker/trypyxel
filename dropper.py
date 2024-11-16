import random
import pyxel

SCREEN_SIZE = 300
THING_SIZE = 10
MAX_POS = SCREEN_SIZE - THING_SIZE


class Thing:
    def __init__(self):
        self.x = random.randint(0, MAX_POS)
        self.y = 0


class App:
    def __init__(self):
        pyxel.init(SCREEN_SIZE, SCREEN_SIZE, title="Thing Dropper")
        self.static = []
        self.active = Thing()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.active.y >= MAX_POS:
            self.things.append(self.active)
            self.active = Thing()
        else:
            self.active.y += 1

    def draw(self):
        pyxel.cls(0)
        for thing in self.static:
            pyxel.rect(thing.x, thing.y, THING_SIZE, THING_SIZE, 8)
        pyxel.rect(self.active.x, self.active.y, THING_SIZE, THING_SIZE, 7)


App()
