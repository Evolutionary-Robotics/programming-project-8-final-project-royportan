import Predator 
import Prey
import matplotlib.pyplot as plt
import numpy as np
import CTRNN
import DumbPrey
Predator1 = Predator.Predator(0,50)

count = 10
genesize = count*count+2*count + 6
#gene = np.random.uniform(-7,7,size = genesize)
gene = np.load("bestGene.npy")
gene2 = np.load("bestGene2.npy")
stepSize = 0.02

controller1 = CTRNN.CTRNN(count,stepSize)
controller1.setParams(gene2)
duration = 102
time = np.arange(0.0,duration,stepSize)
Prey1 = Prey.newPrey(0,0)
Prey2 = DumbPrey.newPrey(10,10,controller1)
Time = 500

pdtx = np.zeros(Time+1)
pdty = np.zeros(Time+1)

endTime = 200

pryx = np.zeros(Time+1)
pryy = np.zeros(Time+1)

def runSimulation(Time):
    global endTime
    for t in range(Time):
        pdtx[t] = Predator1.x
        pdty[t] = Predator1.y
        pryx[t] = Prey2.x
        pryy[t] = Prey2.y
        if Predator1.distance(Prey2) <= 2:
            print(str(t) + "caught" )
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
        print(Predator1.y)
        Predator1.move()
        print(Predator1.velocity)
        Prey2.sense(Predator1)
        Prey2.compute()
        Prey2.escape()
        Prey2.move()
    print(pdty)
    
        
# pdtx[endTime] = Predator1.x
# pdty[endTime] = Predator1.y
# pryx[endTime] = Prey2.x
# pryy[endTime] = Prey2.y
runSimulation(Time)
plt.plot(pdtx,pdty)
plt.plot(pryx,pryy)
plt.plot(pdtx[-1],pdty[-1],'ro')
plt.plot(pryx[-1],pryy[-1],'bo')
plt.show()

plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
ax.set_xlim(-200, 200)  # Set x-axis limits from 0 to 10000
ax.set_ylim(-200, 200)  # Set y-axis limits from 0 to 10000

x1_data = pdtx[0:endTime+1]
y1_data = pdty[0:endTime+1]
x2_data = pryx[0:endTime+1]
y2_data = pryy[0:endTime+1]   
print("x1")
print(x1_data)
print("x2")
print(x2_data)

line1, = ax.plot([], [], 'r-', label='Prey')  
line2, = ax.plot([], [], 'b-', label='Predator') 
ax.legend() 



x1_points, y1_points = [x1_data[0]], [y1_data[0]]
x2_points, y2_points = [x2_data[0]], [y2_data[0]]


ax.scatter(x1_points[0], y1_points[0], color='red', s=10, label='Prey Start')
ax.scatter(x2_points[0], y2_points[0], color='blue', s=10, label='Predator Start')
# ax.scatter(shelter2.x, shelter2.y, color='cyan', s=30, label='Shelter')

def is_fig_open(figure):
    return plt.fignum_exists(figure.number)
print(endTime)



for i in range((endTime+1)):
    if not is_fig_open(fig):  
        break


    x1_points.append(x1_data[i])
    y1_points.append(y1_data[i])
    line1.set_data(x1_points, y1_points)

    x2_points.append(x2_data[i])
    y2_points.append(y2_data[i])
    line2.set_data(x2_points, y2_points)
    # print("left: " +str(Predator2.leftmotor1))
    # print("right: " +str(Predator2.rightmotor1))
    
    plt.draw()
    plt.pause(0.2) 

plt.ioff() 
plt.show() 