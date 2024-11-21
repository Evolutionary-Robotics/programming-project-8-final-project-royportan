import numpy as np
import DumbPrey 
import matplotlib.pyplot as plt
import MGA as EA
import CTRNN
import Predator
popSize = 50
recomprob = 0.25
mutateprob = 0.2
tournaments = 2000
mutateRate = 0.5
count = 10
genesize = count*count+2*count + 6
Predator1 = Predator.Predator(-200,200)
def mutateFunction(mutateRate):
    pass
def fitnessfunction(gene):
    stepSize = 0.02
    Predator1 = Predator.Predator(0,200)
    controller1 = CTRNN.CTRNN(count,stepSize)
    controller1.setParams(gene)
    duration = 100
    endTime = 0
    Prey2 = DumbPrey.newPrey(10,10,controller1)
    # pdtx = np.zeros(duration+1)
    # pdty = np.zeros(duration+1)
    # pryx = np.zeros(duration+1)
    # pryy = np.zeros(duration+1)
    for t in range(duration):
        # pdtx[t] = Predator1.x
        # pdty[t] = Predator1.y
        # pryx[t] = Prey2.x
        # pryy[t] = Prey2.y
        if Predator1.distance(Prey2) <= 3:
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
    return endTime/duration
def fitnessfunction2(gene):
    disAvgSum = 0
    fitscore = 0
    stepSize = 0.02
    duration = 200
    testCoord =[[0,30],[30,0],[0,-30],[-30,0]]
    controller1 = CTRNN.CTRNN(count,stepSize)
    controller1.setParams(gene)
    for i in range(4):
        stepSize = 0.02
        Predator1 = Predator.Predator(testCoord[i][0],testCoord[i][1])
        disSUM = 0
        disAvg = 0
        endTime = 0
        Prey2 = DumbPrey.newPrey(0,0,controller1)
        # pdtx = np.zeros(duration+1)
        # pdty = np.zeros(duration+1)
        # pryx = np.zeros(duration+1)
        # pryy = np.zeros(duration+1)
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
    return (fitscore/4)/duration + (disAvgSum/50)/4
print("hello")
evolution1 = EA.MGA(fitnessfunction2,genesize,popSize,recomprob,mutateprob,tournaments)
print("done1")
evolution1.calculateFitness()
print("done2")
print(evolution1.fit)
evolution1.run()
print(evolution1.bestfit)
evolution1.showFitness()

index = int(evolution1.bestind[-1])
print(index)
bestGene = evolution1.pop[index]
np.save("bestGene.npy",bestGene)

# print("done3")
# print(evolution1.fit)
