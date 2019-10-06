# coding = utf-8
import  matplotlib
from  matplotlib import pyplot as plt


# 设置中文
plt.rcParams["font.family"] = 'Arial Unicode MS'

x = range(1,21)
_x = list(x)
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
_xtick_labels = ["{}岁".format(i+10) for i in _x]
plt.xticks(_x,_xtick_labels,rotation=270)
plt.yticks(range(0,9))
########绘制网格#############
# alpha设置透明度
plt.grid(alpha=0.2)
#----------------------
plt.plot(x,y)
plt.xlabel("年龄")
plt.ylabel("个数")
plt.title("11岁到30岁交的女朋友个数")
plt.savefig("./test3.png")
plt.show()
