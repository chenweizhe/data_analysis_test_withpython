#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/15上午10:34
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
runtime_data = df['Rating'].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数
# print(max_runtime - min_runtime)
# # num_bin = (max_runtime - min_runtime)//0.5
# num_bin_list = [1.6]
# i = 1.6
# while i<=max_runtime:
#     i += 0.5
#     num_bin_list.append(i)
num_bin = 15



# 绘制图形大小
plt.figure(figsize=(20,8),dpi=80)
plt.hist(runtime_data,num_bin)

_x = [1.6]
i = 1.6
while i<=max_runtime:
    i += 0.5
    _x.append(i)



plt.xticks(_x)
plt.show()

