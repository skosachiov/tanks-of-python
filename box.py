from tkinter import *
from random import randint
from PIL import Image, ImageTk

import constants
import sprite

class Box(sprite.Sprite):
    
    def __init__(self, app):
        super().__init__(self, app)
        self.sprite_type = "Box"
        self.x = randint(0, constants.WINDOW_WIDTH)
        self.y = randint(0, constants.WINDOW_HEIGHT)
        self.load_image('./assets/box.png')

