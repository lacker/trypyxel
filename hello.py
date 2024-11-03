import pyxel
import random

SCREEN_SIZE = 200
CELLS = 5
CELL_SIZE = SCREEN_SIZE // CELLS


class App:
    def __init__(self):
        pyxel.init(SCREEN_SIZE, SCREEN_SIZE)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        for i in range(5):
            for j in range(5):
                color = random.randint(0, 15)
                pyxel.rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE, color)


App()
