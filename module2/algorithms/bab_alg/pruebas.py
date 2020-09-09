# import matplotlib.pyplot as plt
# from drawnow import drawnow
# import numpy as np
#
# def makeFig():
#     plt.scatter(xList,yList) # I think you meant this
#
# plt.ion() # enable interactivity
# fig = plt.figure() # make a figure
# plt.grid()
#
#
# xList=list()
# yList=list()
#
# for i in np.arange(1, 10 + 1):
#     y=np.random.random()
#     xList.append(i)
#     yList.append(y)
#     drawnow(makeFig)
#     #makeFig()      The drawnow(makeFig) command can be replaced
#     #plt.draw()     with makeFig(); plt.draw()
#     plt.pause(0.001)
#
# plt.show(block=True)
#
# print(str([1, 2]))

clmap = ['b'] * (len(range(5)) - 1)
clmap.append('r')

print(clmap)

