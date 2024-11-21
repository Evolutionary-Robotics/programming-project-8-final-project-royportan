import numpy as np
import RandomWalker as RW 
import NeuralNet as NN

    #          -----s2-----
    #        lm1[       ] rm1
    #         s1[       ]s3
    #        lm2[       ] rm2 
    #           ----s4----


def load(self, filename):
        params = np.load(filename)
        self.Size = params['size']
        self.Weights = params['weights']
        self.Biases = params['biases']
        self.TimeConstants = params['timeconstants']
        self.invTimeConstants = 1.0/self.TimeConstants

class Predator(RW.Walker):
    def distance(self, prey):
        return np.sqrt((self.x - prey.x)**2+(self.y - prey.y)**2)
    def senDistance(self,prey,index):
        # print("index")
        # print(index)
        # print("x")
        # print(self.sensorPos[index][0])
        # print("y")
        # print(self.sensorPos[index][1])
        return np.sqrt((self.sensorPos[index][0]-prey.x)**2+(self.sensorPos[index][1]-prey.y)**2)    
    def __init__(self,x,y):
        super().__init__()
        self.setX(x)
        self.setY(y)
        self.orientation = np.pi/2

        self.width = 4
        self.length = 5     
        self.direction = 1                
        self.leftmotor1 = 0
        self.leftmotor2 = 0
        self.rightmotor1 = 0
        self.rightmotor2 = 0
        # self.signal = [0.5,1/3,0.5]
        self.sensors = [0, 0, 0, 0]
        self.sensorPos = [[self.x - self.width/2,self.y],[self.x, self.y +self.length/2],[self.x + self.width/2,self.y],[self.x, self.y - self.length/2]]
    def sense(self, prey):
        for senIndex in range(4):
            self.sensors[senIndex] =np.sqrt((self.senDistance(prey,senIndex)))
        # self.signal = self.controller.forward(self.sensors)
    def rotate(self):
        self.orientation += (self.rightmotor1 + self.rightmotor2 - self.leftmotor1 - self.leftmotor2)*np.pi/16
        self.orientation = self.orientation % (2*np.pi)
        #self.orientation += np.random.rand()*np.pi/60
    def think(self):
        rand = 0
        if self.sensors[1] < self.sensors[3]:
            direction = -1
        else: 
            if self.sensors[1] == self.sensors[3]:
                rand = np.random.rand() 
                if rand >= 0.5:
                    direction = 1
                else : 
                    direction = -1
            else:
                self.direction = 1
                
            direction = -1
        self.leftmotor1 =  direction*2*(3*self.sensors[0] - 0.05*self.sensors[2])
        self.leftmotor2 =  direction*2*(3*self.sensors[0] - 0.05*self.sensors[2])
        self.rightmotor1 = direction*2*(-0.05*self.sensors[0] + 3*self.sensors[2])
        self.rightmotor2 = direction*2*(-0.05*self.sensors[0] + 3*self.sensors[2])
        # signal = self.controller.forward(self.sensors)
        # # self.leftmotor1 = signal[0]
        # # self.leftmotor2 = signal[1]
        # # self.rightmotor1 = signal[2]
        # # self.rightmotor2 = signal[3]
    def move(self):
        self.rotate()
        self.velocity = (self.leftmotor1 + self.leftmotor2 + self.rightmotor1 + self.rightmotor2)
        self.velocity = np.clip(self.velocity,-3.51,3.51)
        self.x += self.velocity * np.cos(self.orientation) 
        self.y += self.velocity * np.sin(self.orientation)  
        # print("moved")
        self.sensorPos = [[self.x + (self.width/2)*np.cos(self.orientation+np.pi/2),self.y+(self.width/2)*np.sin(self.orientation+np.pi/2)],
                          [self.x + (self.length/2)*np.cos(self.orientation),self.y+(self.length/2)*np.sin(self.orientation)],
                          [self.x + (self.width/2)*np.cos(self.orientation-np.pi/2),self.y+(self.width/2)*np.sin(self.orientation-np.pi/2)],
                          [self.x + (self.length/2)*np.cos(self.orientation+np.pi),self.y+(self.length/2)*np.sin(self.orientation+np.pi)]]
    
