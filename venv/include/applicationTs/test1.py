#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/15上午7:24
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
file_path = './IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())

# rating runtime分布情况
# 选择图形 连续数据的统计--直方图
runtime_data = df['Runtime (Minutes)'].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数
print(max_runtime - min_runtime)
num_bin = (max_runtime - min_runtime)//5
# 绘制图形大小
plt.figure(figsize=(20,8),dpi=80)
plt.hist(runtime_data,num_bin)
plt.xticks(range(min_runtime,max_runtime+5,5))
plt.show()

