#coding = utf-8
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = 'Arial Unicode MS'


x = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5\n：最后的骑士","摔跤吧！爸爸","加勒比海盗5\n：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：\n终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3\n：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]

y =[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

#设置图形大小
plt.figure(figsize=(20,15),dpi=80)

# x不能直接传字符串进去，所以需要使用range方法
# 都要传数字 bar函数绘制条形图
plt.bar(range(len(x)),y,width=0.3)

# 设置映射 字符串在x轴上
plt.xticks(range(len(x)),x,rotation=90)


plt.savefig("./test6.png")
plt.show()