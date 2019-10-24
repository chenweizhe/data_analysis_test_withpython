#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/24上午8:48
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc')
# 使用matplotlib呈现出店铺总数前十的国家
# 使用matplotlib呈现出大陆每个城市的店铺数量
file_path = './starbucks_store_worldwide.csv'
df = pd.read_csv(file_path)
# xuanzhong中国
df = df[df['Country'] == 'CN']

# 使用matplotlib呈现出店铺总数前十的国家
# 准备数据  ascending = false 降序排列
data1 = df.groupby(by="City").count()['Brand'].sort_values(ascending=False)[:25]

_x = data1.index
_y = data1.values

# 画图
plt.figure(figsize=(20,12),dpi=80)
plt.barh(range(len(_x)),_y,height=0.3,color='orange')

plt.yticks(range(len(_x)),_x,fontproperties=my_font)

plt.savefig('./test8.png')

plt.show()
