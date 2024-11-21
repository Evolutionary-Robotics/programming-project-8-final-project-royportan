import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))
class NeuralNet:
    def __init__(self, shape, Lrate):
        self.Lrate = Lrate
        self.W = []
        self.bias = []
        self.nodePerLayer = shape
        self.layerNum = len(self.nodePerLayer)
        self.k = 4
        self.Nodes = []
    def updateLearningRat(self, Lrate):
        self.Lrate = Lrate
    def setParams(self,params):
        start = 0 
        for layerIndex in range(1,self.layerNum):
            wNum = self.nodePerLayer[layerIndex - 1]*self.nodePerLayer[layerIndex]
            end = start + wNum
            self.W.append((params[start:end]*self.k).reshape(self.nodePerLayer[layerIndex -1 ],self.nodePerLayer[layerIndex]))
            start = end 
        for layerIndex in range(1,self.layerNum):
            end = start + self.nodePerLayer[layerIndex]
            self.bias.append((params[start:end]*self.k).reshape(1,self.nodePerLayer[layerIndex]))
            start = end
    def buildNet(self):
        firstLayer = [None]
        self.Nodes.append(firstLayer)
        for layerIndex in range(1,self.layerNum):
            currLayer = []
            for nodeIndex in range(self.nodePerLayer[layerIndex]):
                currNode = Ptron.Node(self.nodePerLayer[layerIndex - 1],self.Lrate)
                currLayer.append(currNode)
            self.Nodes.append(currLayer)
    def forward(self, input):
        currInput = input
        for layerIndex in range(1,self.layerNum):
            currOuput = []
            for nodeIndex in range(self.nodePerLayer[layerIndex]):
                currOuput.append(self.Nodes[layerIndex][nodeIndex].forward(currInput))
            currInput = currOuput
        return currOuput[0]
        