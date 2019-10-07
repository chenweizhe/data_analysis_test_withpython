# coding = utf-8

import numpy as np

# shuju pingjie

t1 = np.arange(12).reshape((2,6))
# print(t1)
print('*'*50)
t2 = np.arange(12,24).reshape((3,4))
print(t2)
print('*'*50)
# shuzu de pingjie
# print(np.vstack((t1,t2)))  #shuzhi pingjie
# print(np.hstack((t1,t2))) #shiping pingjie

# t3 = np.vstack((t1,t2))
# print(t3)
# print(np.vsplit(t1,))
# hangjiaohuan
t2[[1,2],:] = t2[[2,1],:]
print(t2)
print('*'*50)
# liejiaohuan
t2[:,[0,2]] = t2[:,[2,0]]
print(t2)