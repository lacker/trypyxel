import random
import pyxel

BOARD_HEIGHT = 14
BOARD_WIDTH = 8
CELL_SIZE = 10
COLORS = [12, 10, 8]


class App:
    def __init__(self):
        pyxel.init(CELL_SIZE * BOARD_WIDTH, CELL_SIZE * BOARD_HEIGHT, title="Doctor M")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, CELL_SIZE, CELL_SIZE, random.choice(COLORS))


App()
