import pyxel
import random

SCREEN_SIZE = 200
CELLS = 5
CELL_SIZE = SCREEN_SIZE // CELLS
PLAYER_COLOR = 8  # Define a constant color for the player
BORDER_COLOR = 5  # Assuming 5 corresponds to a dark grey color

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class App:
    def __init__(self):
        pyxel.init(SCREEN_SIZE, SCREEN_SIZE)
        self.player = Player(0, 0, PLAYER_COLOR)  # Initialize player at top-left corner
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # Handle player movement
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.player.x = min(self.player.x + 1, CELLS - 1)
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.player.x = max(self.player.x - 1, 0)
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.player.y = min(self.player.y + 1, CELLS - 1)
        if pyxel.btnp(pyxel.KEY_UP):
            self.player.y = max(self.player.y - 1, 0)

    def draw(self):
        pyxel.cls(0)
        # Draw grid cells
        for i in range(CELLS):
            for j in range(CELLS):
                if i == self.player.x and j == self.player.y:
                    pyxel.rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE, self.player.color)
                else:
                    pyxel.rectb(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE, BORDER_COLOR)  # Draw border
                    pyxel.rect(i * CELL_SIZE + 1, j * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2, 0)  # Fill cell with black

App()
