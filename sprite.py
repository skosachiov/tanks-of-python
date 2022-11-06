from tkinter import *
from PIL import Image, ImageTk

class Sprite():
    def __init__(self, sprite_type, app):
        self.sprite_type = sprite_type
        app.a += [self]
        self.app = app
        self.garbage = False
        self.x = 0; self.y = 0; self.angle = 0; self.v = 0
        self.key = ""

    def load_image(self, png):
        self.file_image = Image.open(png)
        self.photo_image = ImageTk.PhotoImage(self.file_image)
        self.image = self.app.create_image(self.x, self.y, anchor = CENTER, image = self.photo_image)

    def render(self):
        pass

    def collision(self, second):
        pass

    def get_key(self, k):
        pass
