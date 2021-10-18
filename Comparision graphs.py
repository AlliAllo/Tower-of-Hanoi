from algorithm1 import TowerOfHanoi
#from algorithm2 import TowerOfHanoi
import os
import time
import resource

import matplotlib.pyplot as plt
startTime = time.time()


#os.system(["exe files dictionary"])



#https://github.com/mame/quine-relay
#https://stackoverflow.com/questions/10464344/reading-from-stdin-in-c
#https://stackoverflow.com/questions/6798817/how-to-pass-variable-argument-to-exe
#Link til de orginale programmer som jeg brugte til at sammenligne sprog - https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

CProgram = []
PythonProgramTimeConsumed = []
PythonProgramMemoryConsumed = []

n = 22

for x in range(n+1):
    x += 1

    # RUN EXE USING X PARAMETER.

    if TowerOfHanoi(x, 'A', 'B', 'C', originalN=x):
        PythonProgramTimeConsumed.append(time.time() - startTime)
        PythonProgramMemoryConsumed.append(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        PythonMemoryConsumed = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# RESET TIME AFTER THE FIRST ALGORITHM
startTime = time.time()


PythonProgramMemoryConsumed = [element / 1000 for element in PythonProgramMemoryConsumed]



xAxis = []
for x in range(n):
    x += 1
    xAxis.append(x)

moveperSecond = (2**n-1) / PythonProgramTimeConsumed[-1]

print(moveperSecond)

print(PythonProgramMemoryConsumed)

print(xAxis,PythonProgramTimeConsumed)

#y = [2 ** element - 1 for element in xAxis]



for something in range(n):
    if not something == 0:
        x = [xAxis[something],PythonProgramTimeConsumed[something]]
    else:
        x = [0,PythonProgramTimeConsumed[something]]

    y = [xAxis[something+1],PythonProgramTimeConsumed[something+1]]

    plt.plot(x,y)


plt.plot(xAxis,PythonProgramTimeConsumed,"ro")

#y = [2 ** element - 1 for element in xAxis]
#plt.plot(xAxis,y)

plt.xlabel("Antal Skiver")
plt.ylabel("Tidsforbrug")


plt.legend(["Python Algoritme","Algorithm 2"])

plt.show()