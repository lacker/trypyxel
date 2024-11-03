import pyxel

SCREEN_SIZE = 200
CELLS = 5
CELL_SIZE = SCREEN_SIZE // CELLS
PLAYER_COLOR = 8  # Define a constant color for the player
BACKGROUND_COLOR = 0  # Assuming color index 0 is black
BORDER_COLOR = 1      # Assuming color index 1 is dark grey

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
        pyxel.cls(BACKGROUND_COLOR)
        # Draw grid cells
        for i in range(CELLS):
            for j in range(CELLS):
                # Draw cell in black
                pyxel.rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE, BACKGROUND_COLOR)
                # Draw dark grey border
                pyxel.line(i * CELL_SIZE, j * CELL_SIZE, (i + 1) * CELL_SIZE - 1, j * CELL_SIZE, BORDER_COLOR)
                pyxel.line(i * CELL_SIZE, j * CELL_SIZE, i * CELL_SIZE, (j + 1) * CELL_SIZE - 1, BORDER_COLOR)
                pyxel.line(i * CELL_SIZE, (j + 1) * CELL_SIZE - 1, (i + 1) * CELL_SIZE - 1, (j + 1) * CELL_SIZE - 1, BORDER_COLOR)
                pyxel.line((i + 1) * CELL_SIZE - 1, j * CELL_SIZE, (i + 1) * CELL_SIZE - 1, (j + 1) * CELL_SIZE - 1, BORDER_COLOR)
        # Draw player
        pyxel.rect(self.player.x * CELL_SIZE, self.player.y * CELL_SIZE, CELL_SIZE, CELL_SIZE, self.player.color)


App()
