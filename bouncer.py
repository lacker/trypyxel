import math
import random
import pyxel

SCREEN_SIZE = 200
THING_SIZE = 10
MAX_POS = SCREEN_SIZE - THING_SIZE
SPEED = 2
TURN = 2 * math.pi / 16
INITIAL_COLOR = 8
LAST_COLOR = 15


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


def random_vector(size):
    angle = random.random() * 100
    return polar(angle, size)


def polar(angle, size):
    x = math.cos(angle) * size
    y = math.sin(angle) * size
    return Vector(x, y)


class App:
    def __init__(self):
        pyxel.init(SCREEN_SIZE, SCREEN_SIZE, title="Thing Bouncer")
        x = random.randrange(0, MAX_POS)
        y = random.randrange(0, MAX_POS)
        self.direction = 0
        self.position = Vector(x, y)
        self.velocity = polar(self.direction, SPEED)
        self.color = INITIAL_COLOR
        self.score = 0
        pyxel.run(self.update, self.draw)

    def change_color(self):
        self.color += 1
        if self.color > LAST_COLOR:
            self.color = INITIAL_COLOR
        self.score = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.score += 1
            self.direction += TURN
            self.velocity = polar(self.direction, SPEED)

        self.position += self.velocity

        # Handle bouncing

        if self.position.x <= 0 and self.velocity.x < 0:
            self.position.x = 0
            self.velocity.x = -self.velocity.x
            self.change_color()
        if self.position.x >= MAX_POS and self.velocity.x > 0:
            self.position.x = MAX_POS
            self.velocity.x = -self.velocity.x
            self.change_color()

        if self.position.y <= 0 and self.velocity.y < 0:
            self.position.y = 0
            self.velocity.y = -self.velocity.y
            self.change_color()
        if self.position.y >= MAX_POS and self.velocity.y > 0:
            self.position.y = MAX_POS
            self.velocity.y = -self.velocity.y
            self.change_color()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.position.x, self.position.y, THING_SIZE, THING_SIZE, self.color)
        pyxel.text(5, 5, str(self.score), 7)


App()
