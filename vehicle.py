from collections import namedtuple

class Vehicle(object):
    def __init__(self, x, y):
        self.pos = [x, y]

    def moveOneX(self):
        self.pos[0] = self.pos[0] + 1

    def moveOneY(self):
        self.pos[1] = self.pos[0] + 1