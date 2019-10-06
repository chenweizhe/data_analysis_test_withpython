# coding = utf-8
# 数组的形状 数组的行数，列数
import numpy as np

t1 = np.arange(12)
print(t1)
print(t1.shape)

t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)

t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3)
print(t3.shape)

t4 = np.arange(12)
a = t4.reshape(3,4)
print(t4)
print(a)

t5 = np.arange(24).reshape(2,3,4)
print(t5)

t5 = t5.reshape((4,6))
print(t5)

a = t5.reshape((24,))
print(a)
#
# a = t5.reshape((24,1))
# print(a) 24行

t6 = t5.reshape((t5.shape[0]*t5.shape[1],))
print(t6)
# 展开数据
print(t5.flatten())
# 广播机制 全加
print(t5+2)

t6 = np.arange(100,124).reshape((4,6))
print(t6)
# 对应位置相加减
print(t6+t5)

t7 = np.arange(0,6)
print(t5-t7)

t8 = np.arange(4).reshape((4,1))
print(t5-t8)
# 广播原则
# 


