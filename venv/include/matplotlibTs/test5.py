# coding = utf-8
import matplotlib
from matplotlib import  pyplot as plt
plt.rcParams["font.family"] = 'Arial Unicode MS'
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1,32)
x_10 = range(51,82)
# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 使用scatter方法绘制 散点图
plt.scatter(x_3,y_3,label="3月")
plt.scatter(x_10,y_10,label="10月")


# 调整x轴的刻度
_x  = list(x_3)+list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["3月{}日".format(i-50) for i in x_10]

plt.xticks(_x[::3],_xtick_labels[::3],rotation=90)

# 添加描述信息
plt.xlabel("日期")
plt.ylabel("温度")

plt.title("3月和10月每日温度散点图")

# 添加图例
plt.legend()

# 保存图片
plt.savefig("./test5.png")
plt.show()



