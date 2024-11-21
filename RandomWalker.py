import numpy as np

class Walker:
    def __init__(self) :
        self.x = 1
        self.y = 1
        self.velocity = 3
        self.orientation = np.random.rand()*2*np.pi
    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y = y
    def setVelocity(self,velocity):
        self.velocity = velocity
    def setOrientation(self,orientation):
        self.orientation = orientation
    def move(self):
        self.x += self.velocity*np.cos(self.orientation)
        self.y += self.velocity*np.sin(self.orientation)
        