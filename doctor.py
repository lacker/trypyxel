import random
import pyxel

BOARD_HEIGHT = 14
BOARD_WIDTH = 8
CELL_SIZE = 10
DROP_TICKS = 30
COLORS = [12, 10, 8]


class App:
    def __init__(self):
        pyxel.init(CELL_SIZE * BOARD_WIDTH, CELL_SIZE * BOARD_HEIGHT, title="Doctor M")
        self.ticks = 0
        self.active_x = BOARD_WIDTH // 2
        self.active_y = 0
        self.active_color = random.choice(COLORS)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.ticks += 1
        if self.ticks % DROP_TICKS == 0:
            self.active_y += 1
            if self.active_y == BOARD_HEIGHT:
                self.active_y = 0
                self.active_color = random.choice(COLORS)

    def draw(self):
        pyxel.cls(0)
        left = self.active_x * CELL_SIZE
        top = self.active_y * CELL_SIZE
        pyxel.rect(left, top, CELL_SIZE, CELL_SIZE, self.active_color)


App()
