#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/24上午7:50
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
# 使用matplotlib呈现出店铺总数前十的国家
# 使用matplotlib呈现出大陆每个城市的店铺数量
file_path = './starbucks_store_worldwide.csv'
df = pd.read_csv(file_path)


# 使用matplotlib呈现出店铺总数前十的国家
# 准备数据  ascending = false 降序排列
data1 = df.groupby(by="Country").count()['Brand'].sort_values(ascending=False)[:10]

_x = data1.index
_y = data1.values

# 画图
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x)
plt.show()