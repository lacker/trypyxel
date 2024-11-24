import math
import random
import pyxel

SCREEN_SIZE = 200
THING_SIZE = 10
MAX_POS = SCREEN_SIZE - THING_SIZE
SPEED = 6


class App:
    def __init__(self):
        pyxel.init(SCREEN_SIZE, SCREEN_SIZE, title="Thing Bouncer")
        self.x = random.randrange(0, MAX_POS)
        self.y = random.randrange(0, MAX_POS)
        self.randomize_direction()
        pyxel.run(self.update, self.draw)

    def randomize_direction(self):
        angle = random.random() * 100
        self.dx = math.cos(angle) * SPEED
        self.dy = math.sin(angle) * SPEED

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.randomize_direction()

        self.x += self.dx
        if self.x <= 0 and self.dx < 0:
            self.x = 0
            self.dx = -self.dx
        if self.x >= MAX_POS and self.dx > 0:
            self.x = MAX_POS
            self.dx = -self.dx

        self.y += self.dy
        if self.y <= 0 and self.dy < 0:
            self.y = 0
            self.dy = -self.dy
        if self.y >= MAX_POS and self.dy > 0:
            self.y = MAX_POS
            self.dy = -self.dy

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, THING_SIZE, THING_SIZE, 8)


App()
