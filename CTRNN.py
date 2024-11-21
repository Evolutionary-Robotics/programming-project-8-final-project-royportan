import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def tanh(x):
    return np.tanh(x)
count = 4
genesize = count*count+2*count + 6
gene = np.random.uniform(-20,20,size=genesize)
stepSize = 0.01
# print(gene)
class CTRNN():
    def __init__(self, count,stepSize):
        self.count = count
        self.stepSize = stepSize
        self.State = np.zeros(count)
        self.Input = np.zeros(count)
        self.Output = np.zeros(count)
        self.W = np.random.uniform(-10,10,size=(count,count))
        self.Bias = np.random.uniform(-10,10,size=count)
        self.timeCons = np.ones(count)
        self.A = np.random.uniform(-10,10)
        self.B = np.random.uniform(-10,10)
        self.C = np.random.uniform(-10,10)
        self.D = np.random.uniform(-10,10)
        self.M = np.random.uniform(-10,10)
    def setParams(self,gene):
        position = 0
        for i in range(self.count):
            for j in range(self.count):
                self.W[i][j] = gene[position]
                position +=1
        for i in range(self.count):
            self.Bias[i] = gene[position]
            position +=1
        # for i in range(self.count):
        #     self.timeCons[i] = gene[position]  
        #     position += 1
        # self.A = gene[position]
        # position +=1
        # self.B = gene[position]
        # position += 1
        # self.C = gene[position]
        # position +=1
        # self.D = gene[position]
        # position +=1
        # self.M = gene[position]
    def Plastic(self):
        for i in range(self.count):
            for j in range(self.count):
                if i != j:
                    dW = 0.02*(self.A*self.Output[i]*self.Output[j] -0.05*self.W[i][j])
                    # dW = (self.State[i]*self.State[j])
                    self.W[i][j] += dW
    def Step(self):
        #self.Plastic()
        # print("State")
        # print(self.State)
        cons = 1/self.timeCons
        netInput = self.W.dot(self.Output)
        # print("net Input")
        # print(netInput)
        dState = (-self.State+netInput+self.Input)
        # print("dstate")
        # print(dState)
        self.State += dState*self.stepSize
        self.Output = tanh(self.State+self.Bias)
# controller1 = CTRNN(count,stepSize)
# controller1.setParams(gene)
# print(controller1.Output)
# duration = 1
# time = np.arange(0.0,duration,0.01)
# controller1.Step()
# print(controller1.Output)
# controller1.Step()
# print(controller1.Output)
# #SIM cTRNN