import pyxel

SCREEN_SIZE = 200
PLAYER_SIZE = 10
RUN_SPEED = 3
JUMP_ACCEL = 10
MAX_POS = SCREEN_SIZE - PLAYER_SIZE
PLAYER_COLOR = 8  # Define a constant color for the player


class App:
    def __init__(self):
        pyxel.init(SCREEN_SIZE, SCREEN_SIZE, title="Gravity Test")
        self.x = 0
        self.y = MAX_POS
        self.dx = 0
        self.dy = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # Handle player movement
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.dx = RUN_SPEED
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.dx = -RUN_SPEED
        if pyxel.btnr(pyxel.KEY_RIGHT) and self.dx > 0:
            self.dx = 0
        if pyxel.btnr(pyxel.KEY_LEFT) and self.dx < 0:
            self.dx = 0
        if pyxel.btnp(pyxel.KEY_UP) and self.y == MAX_POS:
            self.dy = -JUMP_ACCEL

        # Inertia
        self.x += self.dx
        self.y += self.dy

        # Gravity
        self.dy += 1

        # Limits
        if self.x < 0:
            self.x = 0
        elif self.x > MAX_POS:
            self.x = MAX_POS
        if self.y < 0:
            self.y = 0
        elif self.y > MAX_POS:
            self.dy = 0
            self.y = MAX_POS

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, PLAYER_SIZE, PLAYER_SIZE, PLAYER_COLOR)


App()
