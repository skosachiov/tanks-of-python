from tkinter import *
from random import randint
from PIL import Image, ImageTk
import math

import constants
import sprite
import ball

class Tank(sprite.Sprite):

    keys_map = {"w": "Up",
                "s": "Down",
                "a": "Left",
                "d": "Right",
                "shift_l": "Shift_R" }

    def __init__(self, app, side):
        super().__init__(self, app)
        self.sprite_type = "Tank"
        self.side = side
        self.x = randint(0, constants.WINDOW_WIDTH)
        self.y = randint(0, constants.WINDOW_HEIGHT)
        self.load_image('./assets/tank-' + side + '.png')
        self.hits = 0
        self.balls = 0
        self.text = None

    def get_key(self, k):
        if self.side == "a":
            if k.lower() in Tank.keys_map.keys(): self.key = Tank.keys_map[k.lower()]
        if self.side == "b":
            self.key = k

    def render(self):
        self.x += self.v * math.cos(math.radians(self.angle))
        self.y += self.v * math.sin(-math.radians(self.angle))
        self.app.moveto(self.image, self.x, self.y)

        if   self.key == "Up":       self.v += constants.SPEED_INCREMENT if self.v < constants.MAX_SPEED else 0
        elif self.key == "Down":     self.v -= constants.SPEED_INCREMENT if self.v > -constants.MAX_SPEED else 0
        elif self.key == "Left":     self.angle += constants.ANGLE_INCREMENT
        elif self.key == "Right":    self.angle -= constants.ANGLE_INCREMENT
        elif self.key == "Shift_R":
            if self.balls > 0:
                self.app.a += [ball.Ball(self.app, self)]
                self.balls -= 1

        self.key = ""

        self.photo_image = ImageTk.PhotoImage(self.file_image.rotate(self.angle))
        self.image = self.app.create_image(self.x, self.y, anchor = CENTER, image = self.photo_image)

    def collision(self, second):
        if second.sprite_type in ["Stone", "AppTanks", "Tank"]:
            self.v *= -1
        if second.sprite_type == "Ball":
            if not second.garbage:
                self.hits += 1
                second.garbage = True
            if self.text is not None: self.app.delete(self.text)
            self.text = self.app.create_text(constants.SPRITE_SIZE if self.side == "a" else
                constants.WINDOW_WIDTH - constants.SPRITE_SIZE, constants.SPRITE_SIZE, text = self.hits, fill = "black")
        if second.sprite_type == "Box":
            if not second.garbage:
                self.balls += constants.BOX_CAPACITY
                second.garbage = True
