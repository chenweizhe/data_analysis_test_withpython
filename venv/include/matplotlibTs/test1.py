# coding = utf-8
import pandas
import numpy as np
# from matplotlib import pyplot as plt
from matplotlib import  pyplot as plt

# x = np.arange(1,11)
# y = 2 * x +5
# plt.title("demo")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(x,y)
# plt.show()

#设置图片大小
fig = plt.figure(figsize=(20,8),dpi=80)
# 画图
x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]
plt.plot(x,y)

# 设置x的刻度
_xticks_labels = [i/2 for i in range(4,49)] #x 每0。5取一次
plt.xticks(_xticks_labels[::3]) #每隔3取一个

plt.yticks(range(min(y),max(y)+1))
# 保存
# plt.savefig("./sig_size.svg")
# 显示
plt.show()

