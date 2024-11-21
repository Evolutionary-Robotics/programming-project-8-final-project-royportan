import numpy as np
class GeneA: 
    def __init__(self,visualize,mutateFunction,fitnessFunction,popSize,geneSize,replaceProb,muteRate,probInit,mutateProb,generationNum):
        self.fitnessFunction = fitnessFunction
        self.geneSize = geneSize
        self.replaceProb = replaceProb
        self.mutateProb = mutateProb
        self.generationNum = generationNum
        self.popSize = popSize
        self.probInit = probInit
        self.muteRate = muteRate
        self.mutateFunction = mutateFunction
        self.visualize = visualize
        self.pop = np.random.rand(popSize,geneSize)*30 - 15 
        self.fitScore = np.zeros(geneSize+1)
        self.bestGene = np.random.rand(geneSize)
    def calcProb(self):
        chooseProb = np.zeros(self.popSize)
        probInit = self.probInit
        for currProb in range(self.popSize):
            chooseProb[currProb] = ((1-probInit)**(currProb))*probInit
        return chooseProb
    def ranking(self,pop, popScore):
        combine = list(zip(pop,popScore))
        sortGeneCombine = sorted(combine,key=lambda x: x[1],reverse=True)
        sortedPop, sortedScore =zip(*sortGeneCombine)
        return sortedPop, sortedScore
    def runGen(self):
        print(self.popSize)
        for currMem in range(self.popSize):
                self.fitScore[currMem] = self.fitnessFunction(self.pop[currMem])
        self.pop,self.fitScore = self.ranking(self.pop,self.fitScore)
        currPop = self.pop
        self.pop = np.array(currPop)
        self.fitScore = np.array(self.fitScore)
        for currGeneration in range(self.generationNum):
            
            print(currGeneration)
            #fitScore = np.zeros(self.popSize)
            #1evaluate all the population
            # print(self.fitScore[1])
            # print(self.pop[1])
            #2Select or ranking
            chooseProb = self.calcProb()
            #3preproduction loop pick 2 parents and recombine
            offSpring = np.zeros( ( round(self.popSize*self.replaceProb), self.geneSize))
            for pair in range(round(self.replaceProb*self.popSize)):
                parent1 = None
                parent2 = None
                while parent1 == None or parent2 == None:
                    if parent1 == None:
                        for currGeno in range(self.popSize):
                            rate1 = np.random.rand()
                            if rate1 < chooseProb[currGeno]:
                                parent1 = currGeno 
                                break
                    if parent2 == None: 
                        for currGeno in range(self.popSize):
                            if currGeno != parent1:
                                rate2 = np.random.rand()
                                if rate2 < chooseProb[currGeno]:
                                    parent2 = currGeno
                                    break
                for genIndex in range(self.geneSize//2):
                
                    offSpring[pair][genIndex] = self.pop[parent1][genIndex]
                for genIndex in range((self.geneSize//2),self.geneSize):
                 
                    offSpring[pair][genIndex] = self.pop[parent2][genIndex]
            #mute the offspring
                rate3 = np.random.rand()
                if rate3 <= 0.3:  
                    for genIndex in range(self.geneSize):
                        rate4 = np.random.rand()
                        if rate4 < self.mutateProb:
                            offSpring[pair][genIndex] = self.mutateFunction(offSpring[pair][genIndex],self.muteRate)  
            #replace bad parental with new gene
                startInd = (self.popSize - round(self.replaceProb*self.popSize))
                endInd = self.popSize
            self.fitScore = np.array(self.fitScore)
            currPop = self.pop
            self.pop = np.array(currPop)
            for popIndex in range(startInd):
                rate = np.random.rand()
                if rate < 0.2:
                    for geneIndex in range(self.geneSize):
                        rate2 = np.random.rand()
                        if rate2 < self.mutateProb:
                            self.pop[popIndex][geneIndex] = self.mutateFunction(self.pop[popIndex][genIndex],self.muteRate) 
            for popIndex in range(startInd,endInd):
                    if 0.9*self.fitnessFunction(self.pop[popIndex]) < self.fitnessFunction(offSpring[popIndex-startInd]):
                        self.pop[popIndex] = offSpring[popIndex-startInd]
            for currMem in range(self.popSize):
                self.fitScore[currMem] = self.fitnessFunction(self.pop[currMem])
            self.pop,self.fitScore = self.ranking(self.pop,self.fitScore)
            self.visualize(self.fitScore)
            print(self.fitnessFunction(self.pop[0]))
            print(self.fitScore)
            #self.visualize(self.pop)
            
        
      