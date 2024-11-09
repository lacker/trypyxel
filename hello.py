import pyxel

SCREEN_SIZE = 200
PLAYER_COLOR = 8  # Define a constant color for the player
BORDER_COLOR = 5  # 5 corresponds to a dark grey color


class Player:
    def __init__(self, x, y, color):
        "x and y are in pixels."
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
            self.player.x += 1
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.player.x -= 1

    def draw(self):
        pyxel.cls(0)
        # TODO: draw player


App()
