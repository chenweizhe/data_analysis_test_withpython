#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/25下午11:14
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 2015-2017 25w紧急电话
# 统计不同类型的紧急情况的次数
# 不同月份不同类型紧急电话的次数的变化情况

file_path = './911.csv'
df = pd.read_csv(file_path)

temp_list = df['title'].str.split(': ').tolist()
cate_list = [i[0] for i in temp_list]

df['cate'] = pd.DataFrame(np.array(cate_list).reshape(df.shape[0],1))

# print(df.head(5))
a = df.groupby(by='cate').count()['title']
print(a)