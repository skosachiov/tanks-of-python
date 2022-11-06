from tkinter import *
from random import randint
from PIL import Image, ImageTk
import math

import constants
import sprite

class Ball(sprite.Sprite):

    def __init__(self, app, tank):
        super().__init__(self, app)
        self.sprite_type = "Ball"                
        self.x = tank.x + constants.SPRITE_SIZE * math.cos(math.radians(tank.angle))
        self.y = tank.y + constants.SPRITE_SIZE * math.sin(-math.radians(tank.angle))
        self.angle = tank.angle
        self.v = abs(tank.v) + constants.BALL_SPEED
        self.load_image('./assets/ball.png')

    def render(self):
        self.x += self.v * math.cos(math.radians(self.angle))
        self.y += self.v * math.sin(-math.radians(self.angle))
        self.app.moveto(self.image, self.x, self.y)

        self.photo_image = ImageTk.PhotoImage(self.file_image.rotate(self.angle))
        self.image = self.app.create_image(self.x, self.y, anchor = CENTER, image = self.photo_image)

    def collision(self, second):
        if (second.sprite_type in ["Stone", "AppTanks", "Tank"]):
            self.load_image('./assets/explosion.png')
            self.garbage = True