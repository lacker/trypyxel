import pyxel

SCREEN_SIZE = 200
PLAYER_SIZE = 10
RUN_SPEED = 3
JUMP_ACCEL = 10
BULLET_SPEED = 6
BULLET_COLOR = 11
MAX_POS = SCREEN_SIZE - PLAYER_SIZE
PLAYER_COLOR = 8  # Define a constant color for the player


class App:
    def __init__(self):
        pyxel.init(SCREEN_SIZE, SCREEN_SIZE, title="Gravity Test")
        self.x = 0
        self.y = MAX_POS
        self.dx = 0
        self.dy = 0
        self.bullets = []
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

        # Spawn bullets
        if pyxel.btnp(pyxel.KEY_SPACE):
            direction = 1
            if self.dx < 0:
                direction = -1

            self.bullets.append((self.x, self.y, direction))

        # Inertia
        self.x += self.dx
        self.y += self.dy
        new_bullets = []
        for x, y, direction in self.bullets:
            if x < 0 or x > MAX_POS:
                continue
            new_bullets.append((x + BULLET_SPEED * direction, y, direction))
        self.bullets = new_bullets

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
        for x, y, _ in self.bullets:
            pyxel.rect(x, y, PLAYER_SIZE, PLAYER_SIZE, BULLET_COLOR)


App()
