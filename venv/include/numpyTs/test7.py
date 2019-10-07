#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/7上午9:18
"""
import numpy as np
# nan he inf
a = np.inf
# print(type(a))
# print(np.nan == np.nan)
# print(np.nan != np.nan)

t2 = np.arange(24).astype(float).reshape(4,6)
# print(t2)

t2[t2<10] = 3
# print(t2)
t2[t2>20] = 20
# print(t2)
t2[3,3] = np.nan
print(t2)

t2[:,0] = 0
print(t2)

# print(np.count_nonzero(t2))

# print(np.count_nonzero(t2!=t2))
# print(np.count_nonzero(np.isnan(t2)))

# t2[np.isnan(t2)] = 0

print(t2)

# nan he renhezhi jinxing jisuan doushi nan
print(np.sum(t2))

t3 = np.arange(12).reshape(3,4)
# print(np.sum(t3))
#
# print(np.sum(t3,axis=0))
# print(np.sum(t3,axis=1))
#
# print(np.sum(t2,axis=0))

print(np.mean(t3))
print(np.mean(t3,axis=1))
print(np.median(t3,axis=0))

# jizhi zhideshi zuidazhi he zuixiaozhi zhicha
print(np.ptp(t3))
# biaozhuncha
print(np.std(t3,axis=0))
