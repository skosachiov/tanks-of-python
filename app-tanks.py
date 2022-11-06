from tkinter import *
from random import randint
from PIL import Image, ImageTk

import constants
import tank
import ball
import stone
import box

class AppTanks(Canvas):

    def __init__(self):
        self.sprite_type = "AppTanks"
        self.a = []

        super().__init__(width = constants.WINDOW_WIDTH, height = constants.WINDOW_HEIGHT, background = constants.WINDOW_BG)
        
        for side in ["a", "b"]: tank.Tank(self, side)
        for _ in range(constants.STONES_NUMBER): stone.Stone(self)
        for _ in range(constants.BOXES_NUMBER): box.Box(self)
       
        self.bind_all('<Key>', self.on_key)
        self.pack()
        self.after(constants.DELAY_MS, self.perform_actions)

    def perform_actions(self):
        for e in self.a:
            e.render()
        self.check_collisions()
        self.garbage_collector()
        self.after(constants.DELAY_MS, self.perform_actions)
    
    def check_collisions(self):
        for i in range(len(self.a)):
            if (self.a[i].x < 0 or constants.WINDOW_WIDTH < self.a[i].x or self.a[i].y < 0 or constants.WINDOW_HEIGHT < self.a[i].y):
                self.a[i].collision(self)
            for j in range(len(self.a)):
                if (i == j): continue
                if (self.a[i].x - self.a[j].x)**2 + (self.a[i].y - self.a[j].y)**2 < constants.SPRITE_SIZE**2:
                    self.a[i].collision(self.a[j])

    def garbage_collector(self):
        for e in self.a:
            if e.garbage: self.a.remove(e)
    
    def on_key(self, k):
        for e in self.a:
            e.get_key(k.keysym)

root = Tk()
root.title('Tanks of python')
root.resizable(False, False)

app = AppTanks()
root.mainloop()