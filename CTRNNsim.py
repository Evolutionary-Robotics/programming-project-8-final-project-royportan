import numpy as np
import matplotlib.pyplot as plt
import CTRNN 


count = 4
genesize = count*count+2*count + 6
gene = np.random.uniform(-5,5,size = genesize)
stepSize = 0.01

controller1 = CTRNN.CTRNN(count,stepSize)
controller1.setParams(gene)
duration = 1000
time = np.arange(0.0,duration,stepSize)
outputs = np.zeros((len(time),count))
states = np.zeros((len(time),count))
step = 0

# for i in range(20):
#     print("NNNNNNNNNNNNNNNNNNNNNNNN")
#     # print(controller1.State)
#     controller1.Step()
#     # print(controller1.State)

for t in range(len(time)):
    controller1.Step()
    states[t] = controller1.State
    outputs[t] = controller1.Output
    # print(controller1.State[0])

plt.plot(time,outputs)
plt.xlabel("Time")
plt.ylabel("Outputs")
plt.title(" Output plot over time ")
plt.show()

# Plot activity
plt.plot(time,states)
plt.xlabel("Time")
plt.ylabel("States")
plt.title(" State plot over time ")
plt.show()

