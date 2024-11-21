import Predator
import numpy as np
class newPrey():
    def __init__(self,x,y):
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
        self.sensors = [0, 0, 0, 0]
        self.sensors2 = [0, 0, 0, 0]
        self.sensorPos = [[self.x - self.width/2,self.y],[self.x, self.y +self.length/2],[self.x + self.width/2,self.y],[self.x, self.y - self.length/2]]
    def senDistance(self,obj,index):
        # print("index")
        # print(index)
        # print("x")
        # print(self.sensorPos[index][0])
        # print("y")
        # print(self.sensorPos[index][1])
        return np.sqrt((self.sensorPos[index][0]-obj.x)**2+(self.sensorPos[index][1]-obj.y)**2)
    def distance(self, agent):
        return np.sqrt((self.x-agent.x)**2+(self.y-agent.y)**2)
    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y = y
    def setVelocity(self,velocity):
        self.velocity = velocity
    def sense(self,Predator):
        for senIndex in range(4):
            self.sensors[senIndex] =np.sqrt((self.senDistance(Predator,senIndex)))
            # self.sensors2[senIndex] = np.sqrt(self.senDistance(Shelter, senIndex))
    def senseShelter(self,Shelter):
         shelterDis = np.sqrt((self.x - Shelter.x)**2+(Shelter.y - self.y)**2)
         return shelterDis
    def findShelter(self):
        direction = 1
        rand = 0
        if self.sensors2[1] < self.sensors2[3]:
            direction = 1
        else: 
            direction = -1
        self.leftmotor1 =  2*direction*(2*self.sensors2[0] - 0.02*self.sensors2[2])
        self.leftmotor2 =  2*direction*(2*self.sensors2[0] - 0.02*self.sensors2[2])
        self.rightmotor1 = 2*direction*(-0.02*self.sensors2[0] + 2*self.sensors2[2])
        self.rightmotor2 = 2*direction*(-0.02*self.sensors2[0] + 2*self.sensors2[2])
    def rotate(self):
        self.orientation += (self.rightmotor1 + self.rightmotor2 - self.leftmotor1 - self.leftmotor2)*np.pi/8
        self.orientation = self.orientation % (2*np.pi)
        self.orientation += (np.random.rand()*2-1)*np.pi/60
    def think(self, Predator):
        if self.distance(Predator) >= 8:
            self.findShelter()
        else:
            self.escape()
    def escape(self):
        rand = 0
        if self.sensors[1] < self.sensors[3]:
            direction =  -1
        else: 
            if self.sensors[1] == self.sensors[3]:
                rand = np.random.rand() 
                if rand >= 0.5:
                    direction = 1
                else : 
                    direction = -1
            else:
                direction = 1
        self.rightmotor1 =  direction*(2*self.sensors[0] - 0.005*self.sensors[2])
        self.rightmotor2 =  direction*(2*self.sensors[0] - 0.005*self.sensors[2])
        self.leftmotor1 = direction*(-0.005*self.sensors[0] + 2*self.sensors[2])
        self.leftmotor2 = direction*(-0.005*self.sensors[0] + 2*self.sensors[2])
    def move(self):
        self.rotate()
        self.velocity = (self.leftmotor1 + self.leftmotor2 + self.rightmotor1 + self.rightmotor2)/4
        self.velocity = np.clip(self.velocity,-4,4)
        self.x += self.velocity * np.cos(self.orientation) 
        self.y += self.velocity * np.sin(self.orientation)  
        # print("moved")
        self.sensorPos = [[self.x + (self.width/2)*np.cos(self.orientation+np.pi/2),self.y+(self.width/2)*np.sin(self.orientation+np.pi/2)],
                          [self.x + (self.length/2)*np.cos(self.orientation),self.y+(self.length/2)*np.sin(self.orientation)],
                          [self.x + (self.width/2)*np.cos(self.orientation-np.pi/2),self.y+(self.width/2)*np.sin(self.orientation-np.pi/2)],
                          [self.x + (self.length/2)*np.cos(self.orientation+np.pi),self.y+(self.length/2)*np.sin(self.orientation+np.pi)]]
    