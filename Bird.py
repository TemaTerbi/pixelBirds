from pygame import *

# Const variables
FLY_SPEED = 10
JUMP_POWER = 10
GRAVITY = 0.35
WIDTH = 50
HEIGHT = 50
COLOR = (0, 0, 0)


class Bird(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.on_ground = False
        self.startX = x
        self.startY = y
        self.imgage = Surface((WIDTH, HEIGHT))
        self.imgage.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right, up):
        if left:
            self.xvel = -FLY_SPEED
        elif right:
            self.xvel = FLY_SPEED
        elif up:
           if self.on_ground:
               self.yvel = -JUMP_POWER
        elif not (left, right, up):
            self.xvel = 0
        if not self.on_ground:
            self.yvel += GRAVITY

        self.on_ground = False
        self.rect.y += self.yvel
        self.rect.x += self.xvel

    def draw(self, screen):
        screen.blit(self.imgage, (self.rect.x, self.rect.y))
