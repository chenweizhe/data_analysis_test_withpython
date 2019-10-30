#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/25下午10:28
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 2015-2017 25w紧急电话
# 统计不同类型的紧急情况的次数
# 不同月份不同类型紧急电话的次数的变化情况

file_path = './911.csv'

df = pd.read_csv(file_path)

# print(df.info)
# 不同类型的紧急情况次数
# 获取分类情况
# df['title'].str.split(': ')
temp_list = df['title'].str.split(': ').tolist()
cate_list = list(set([i[0] for i in temp_list]))
print(cate_list)

# gouzao全为0的数组

zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)
# 赋值
for cate in cate_list:
    zeros_df[cate][df['title'].str.contains(cate)] = 1

sum_set = zeros_df.sum(axis = 0)
print(sum_set)
# print(zeao_df)