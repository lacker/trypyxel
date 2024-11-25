import math
import random
import pyxel

SCREEN_SIZE = 200
THING_SIZE = 10
MAX_POS = SCREEN_SIZE - THING_SIZE
SPEED = 6


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


def random_vector(size):
    angle = random.random() * 100
    x = math.cos(angle) * size
    y = math.sin(angle) * size
    return Vector(x, y)


class App:
    def __init__(self):
        pyxel.init(SCREEN_SIZE, SCREEN_SIZE, title="Thing Bouncer")
        x = random.randrange(0, MAX_POS)
        y = random.randrange(0, MAX_POS)
        self.position = Vector(x, y)
        self.velocity = random_vector(SPEED)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.velocity = random_vector(SPEED)

        self.position += self.velocity

        # Handle bouncing

        if self.position.x <= 0 and self.velocity.x < 0:
            self.position.x = 0
            self.velocity.x = -self.velocity.x
        if self.position.x >= MAX_POS and self.velocity.x > 0:
            self.position.x = MAX_POS
            self.velocity.x = -self.velocity.x

        if self.position.y <= 0 and self.velocity.y < 0:
            self.position.y = 0
            self.velocity.y = -self.velocity.y
        if self.position.y >= MAX_POS and self.velocity.y > 0:
            self.position.y = MAX_POS
            self.velocity.y = -self.velocity.y

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.position.x, self.position.y, THING_SIZE, THING_SIZE, 8)


App()
