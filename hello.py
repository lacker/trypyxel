import pyxel
import random

SCREEN_SIZE = 200
CELLS = 5
CELL_SIZE = SCREEN_SIZE // CELLS
PLAYER_COLOR = 8  # Define a constant color for the player


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
        for i in range(5):
            for j in range(5):
                color = random.randint(0, 15)
                pyxel.rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE, color)
        # Draw player
        pyxel.rect(self.player.x * CELL_SIZE, self.player.y * CELL_SIZE, CELL_SIZE, CELL_SIZE, self.player.color)


App()
