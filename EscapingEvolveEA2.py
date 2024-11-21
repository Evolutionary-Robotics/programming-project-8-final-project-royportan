import numpy as np
import DumbPrey 
import matplotlib.pyplot as plt
import GeneA as EA
import CTRNN
import Predator


popSize = 25
replaceProb = 0.5
mutateprob = 0.3
generationNum = 20
mutateRate = 0.3
count = 10
genesize = count*count+count 
probInit = 0.5
# Predator1 = Predator.Predator(-0,200)
def mutateFunction(currGene, mutateRate):
    if np.random.randn() <= 0.5:
        if np.random.rand() <= 0.5:
            return currGene + mutateRate
        else:
            return currGene - mutateRate
    else :
        return currGene*2*np.tanh(np.random.rand())
Count = []
BestList = []
MeanList = []
WorstList = []
def Calchar(pop):
    CalArray = []
    location = [[50,0],[-50,0],[0,50],[0,-50],[50*np.cos(np.pi/4),50*np.cos(np.pi/4)],[-50*np.cos(np.pi/4),50*np.cos(np.pi/4)],[50*np.cos(np.pi/4),-50*np.cos(np.pi/4)],[-50*np.cos(np.pi/4),-50*np.cos(np.pi/4)]]
    for popIndex in range(len(pop)):
        genChar = np.zeros(8)
        stepSize = 0.01
        controller1 = CTRNN.CTRNN(count,stepSize)
        controller1.setParams(pop[popIndex])
        testPrey = DumbPrey.newPrey(0,0,controller1)
        for i in range(len(location)):
            testPredator = Predator.Predator(location[i][0],location[i][1])
            testPrey.sense(testPredator)
            testPrey.compute()
            testPrey.escape()
            genChar[i] = testPrey.rotateAngle()
        CalArray.append(genChar)
    return CalArray

def CalcharInd(gene): 
    stepSize = 0.01
    genChar = np.zeros(8)
    location = [[50,0],[-50,0],[0,50],[0,-50],[50*np.cos(np.pi/4),50*np.cos(np.pi/4)],[-50*np.cos(np.pi/4),50*np.cos(np.pi/4)],[50*np.cos(np.pi/4),-50*np.cos(np.pi/4)],[-50*np.cos(np.pi/4),-50*np.cos(np.pi/4)]]
    controller1 = CTRNN.CTRNN(count,stepSize)
    controller1.setParams(gene)
    testPrey = DumbPrey.newPrey(0,0,controller1)
    for i in range(len(location)):
        testPredator = Predator.Predator(location[i][0],location[i][1])
        testPrey.sense(testPredator)
        testPrey.compute()
        testPrey.escape()
        genChar[i] = testPrey.rotateAngle()
    return genChar
def CalDiver(genChar,popChar):
    DiverScore = 0
    for popIndex in range(len(popChar)):
        for i in range(8):
            if genChar[i] != 0:
                if abs((genChar[i]-popChar[popIndex][i])/genChar[i]) >= 0.05:
                    DiverScore +=1
            else:
                if abs((genChar[i]-popChar[popIndex][i])) >= 0.05:
                    DiverScore +=1
    return DiverScore
def visualize(fitscore):
    global Count, BestList, MeanList, WorstList
    # fitscore = fitnessFunction(pop)
    # bestGenotype = pop[0]
    # worstGenotype = pop[-1] 
    Best = fitscore[0]
    Worst = fitscore[-1]
    Mean = np.mean(fitscore) 
    
    if len(Count) == 0:
        Count.append(0)  
    else:
        Count.append(Count[-1] + 1) 
    BestList.append(Best)  
    MeanList.append(Mean)
    WorstList.append(Worst)
def fitnessfunction(gene):
    fitscore = 0
    stepSize = 0.01
    # genChar = CalcharInd(gene)
    # DiverScore = CalDiver(genChar,popChar)
    duration = 100
    testCoord =[[50,0],[-50,0],[0,50],[0,-50],[50*np.cos(np.pi/4),50*np.cos(np.pi/4)],[-50*np.cos(np.pi/4),50*np.cos(np.pi/4)],[50*np.cos(np.pi/4),-50*np.cos(np.pi/4)],[-50*np.cos(np.pi/4),-50*np.cos(np.pi/4)]]
    # testCoord2 = -1*[[50,0],[-50,0],[0,50],[0,-50],[50*np.cos(np.pi/4),50*np.cos(np.pi/4)],[-50*np.cos(np.pi/4),50*np.cos(np.pi/4)],[50*np.cos(np.pi/4),-50*np.cos(np.pi/4)],[-50*np.cos(np.pi/4),-50*np.cos(np.pi/4)]]
    controller1 = CTRNN.CTRNN(count,stepSize)
    controller1.setParams(gene)
    disAvgSum = 0
    for i in range(8):
        stepSize = 0.01
        Predator1 = Predator.Predator(testCoord[i][0],testCoord[i][1])
        # Predator2 = Predator.Predator(testCoord2[i][0],testCoord2[i][1])
        endTime = 0
        Prey2 = DumbPrey.newPrey(0,0,controller1)
        # pdtx = np.zeros(duration+1)
        # pdty = np.zeros(duration+1)
        # pryx = np.zeros(duration+1)
        # pryy = np.zeros(duration+1)
        disSUM = 0
        disAvg = 0
        for t in range(duration):
            # pdtx[t] = Predator1.x
            # pdty[t] = Predator1.y
            # pryx[t] = Prey2.x
            # pryy[t] = Prey2.y
            disSUM += Predator1.distance(Prey2)
            if Predator1.distance(Prey2) <= 2:
                endTime = t
                # print(Predator1.x)
                # print(Prey2.x)
                # pdtx[t+1] = Predator1.x
                # pdty[t+1] = Predator1.y
                # pryx[t+1] = Prey2.x
                # pryy[t+1] = Prey2.y
                break
            Predator1.sense(Prey2)
            Predator1.think()
            Predator1.move()
            Prey2.sense(Predator1)
            Prey2.compute()
            Prey2.escape()
            Prey2.move()
        disAvg = disSUM/duration
        disAvgSum += disAvg
        fitscore += endTime
    return ((fitscore)/duration)/8 
print("hello")
evolution1 = EA.GeneA(visualize,mutateFunction,fitnessfunction,popSize,genesize,replaceProb,mutateRate,probInit,mutateprob,generationNum)
print("done1")
evolution1.runGen()
bestTime = 102
visualize(evolution1.fitScore)
pdtx = np.zeros(bestTime+1)
pdty = np.zeros(bestTime+1)

plt.plot(Count,BestList)
plt.plot(Count,WorstList)
plt.plot(Count,MeanList)
plt.xlabel("Generations")
plt.ylabel("Fitness")
plt.title("Evolution")
plt.show()
pryx = np.zeros(bestTime+1)
pryy = np.zeros(bestTime+1)

bestGene = evolution1.pop[0]
np.save("bestGene2.npy",bestGene)
stepSize = 0.02
# Predator1 = Predator.Predator(-0,-30)
# controller2 = CTRNN.CTRNN(count,stepSize)
# Prey2 = DumbPrey.newPrey(10,10,controller2)
# for t in range(bestTime):
#         pdtx[t] = Predator1.x
#         pdty[t] = Predator1.y
#         pryx[t] = Prey2.x
#         pryy[t] = Prey2.y
#         if Predator1.distance(Prey2) <= 2:
#             endTime = t
#             # print(Predator1.x)
#             # print(Prey2.x)
#             # pdtx[t+1] = Predator1.x
#             # pdty[t+1] = Predator1.y
#             # pryx[t+1] = Prey2.x
#             # pryy[t+1] = Prey2.y
#             break
#         Predator1.sense(Prey2)
#         Predator1.think()
#         Predator1.move()
#         Prey2.sense(Predator1)
#         Prey2.compute()
#         Prey2.escape()
#         Prey2.move()

# plt.plot(pdtx,pdty)
# plt.plot(pryx,pryy)
# plt.plot(pdtx[-1],pdty[-1],'ro')
# plt.plot(pryx[-1],pryy[-1],'bo')
# plt.show()
# index = int(evolution1.bestind[-1])
# print(index)
# bestGene = evolution1.pop[index]
# np.save("bestGene.npy",bestGene)

# print("done3")
# print(evolution1.fit)
