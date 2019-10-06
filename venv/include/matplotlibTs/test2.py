# coding = utf-8
import random
import matplotlib
from  matplotlib import pyplot as plt
from  matplotlib import font_manager
y = [random.randint(20,35) for i in range(120)]

x = range(1,121)
_x = list(x)
# 设置字体
# my_font = font_manager.ttfFontProperty(fname="/System/Library/Fonts/PingFang.ttc")
# plt.figure(figsize=(20,8),dpi=80)
# 设置中文字体
plt.rcParams["font.family"] = 'Arial Unicode MS'
plt.plot(x,y)


# 调整x轴的刻度
_xtick_labels = ["10:{}".format(i) for i in range(60)]
_xtick_labels += ["11:{}".format(i-60) for i in range(60,120)]
# 取步长，数字和字符串一一对应，数据的长度是一样的
plt.xticks(_x[::3],_xtick_labels[::3],rotation = 90)

plt.xlabel("时间")
plt.ylabel("温度 单位()")
plt.title("10点到12点每分钟的气温变化情况")



plt.savefig("./test2.png")

plt.show()