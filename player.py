import pygame, math

from pygame.locals import *

up_kb = [K_w, K_UP]
down_kb = [K_s, K_DOWN]
left_kb = [K_a, K_LEFT]
right_kb = [K_d, K_RIGHT]

key_sets = {"kb1": {'up': K_w, 'down': K_s, 'left': K_a, 'right': K_a, 'shoot': K_LSHIFT, 'ability': K_LCTRL},
            "kb2": {'up': K_UP, 'down': K_DOWN, 'left': K_LEFT, 'right': K_RIGHT, 'shoot': K_RCTRL, 'ability': K_MENU}}


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()

        self.angle = 0
        self.color = color
        self.speed = 1

        self.image = pygame.image.load("sprites/Tank 2.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.x = (pos[0])
        self.y = (pos[1])

        self.picture = pygame.image.load("sprites/Tank 2.png")

    def getAngle(self):
        return self.angle

    def movePlayer(self):
        movement_x = math.cos(self.angle) * self.speed
        movement_y = math.sin(self.angle) * self.speed
        self.rect.x += movement_x
        self.rect.y += movement_y

    def rotatePlayer(self):
        pass
        # add rotate function

    def setVelocity(self, x, y):
        self.velocity = [x, y]

    def setSpeedX(self, x):
        self.velocity[0] = x

    def setSpeedY(self, y):
        self.velocity[1] = y

    def getVelocity(self):
        return [self.velocity[0], self.velocity[1]]

    def setAccY(self, y):
        self.velocity[1] = y

    def get_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[key_sets["kb1"]["left"]]:
            self.angle += 1
            picture_copy = pygame.transform.rotate(self.picture, self.angle).copy()
            self.image = pygame.transform.rotate(self.picture, self.angle)
            # self.rect.x = self.x - int(picture_copy.get_width() / 2)
            # self.rect.y = self.y - int(picture_copy.get_height() / 2)
            self.rect.x = 0
            self.rect.y = 0
        if keys[K_d]:
            self.angle -= 1
            self.image = pygame.transform.rotate(self.picture, self.angle)

    def update(self):
        self.get_inputs()
