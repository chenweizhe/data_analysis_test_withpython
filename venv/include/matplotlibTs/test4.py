# coding = utf-8

import  matplotlib
from  matplotlib import pyplot as plt


# 设置中文
plt.rcParams["font.family"] = 'Arial Unicode MS'

x = range(1,21)
_x = list(x)
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

_xtick_labels = ["{}岁".format(i+10) for i in _x]
plt.xticks(_x,_xtick_labels,rotation=270)
########绘制网格#############
# alpha设置透明度
plt.grid(alpha=0.2,linestyle=':')
#----------plot两次,在一个图中绘制两个图片--color传颜色-label传标签---------
plt.plot(x,y1,label="自己",color="orange",linestyle=':')
plt.plot(x,y2,label="同桌",color="cyan",linestyle='-.')
plt.xlabel("年龄")
plt.ylabel("个数")
plt.title("11岁到30岁交的女朋友个数")

# -----添加图例--指定在左上角-
plt.legend(loc="upper left")

plt.savefig("./test4.png")
plt.show()


# test1-test4为折线图绘制
