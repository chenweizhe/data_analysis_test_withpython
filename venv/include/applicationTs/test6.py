#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/16上午11:09
"""
# 索引和复合索引
import pandas as pd
import numpy as np
from  matplotlib import pyplot as plt
file_path = './starbucks_store_worldwide.csv'
df = pd.read_csv(file_path)
# print(df.head(1))
print(df.info())
# 按照国家进行分组
grouped = df.groupby(by="Country")
# print(grouped)
# 可以进行遍历
# for i,j in grouped:  #元组遍历
#     print(i)
#     print(j)
#     print('*'*100)

# 聚合操作
# 统计数量
country_count = grouped["Brand"].count()

US_count = country_count['US']
# print(US_count)

CHN_count  = country_count['CN']
# print(CHN_count)
# 按省份进行分组
china_data = df[df['Country'] == 'CN'].groupby(by='State/Province').count()['Brand']
# print(china_data)

# 对两个字段同时进行分组统计
# 数据按照多个条件进行分组
grouped = df['Brand'].groupby(by=[df['Country'],df['State/Province']]).count()
# print(grouped)
grouped = df.groupby(by=[df['Country'],df['State/Province']])['Brand'].count()
# print(grouped)
grouped = df.groupby(by=[df['Country'],df['State/Province']]).count()['Brand']
# print(grouped)
# 以上 有三种写法  类型为series

# # 以上操作但是返回dataframe类型 方括号嵌套方括号
# grouped = df[['Brand']].groupby(by=[df['Country'],df['State/Province']]).count()
# # print(type(grouped))
# grouped = df.groupby(by=[df['Country'],df['State/Province']])[['Brand']].count()
# print(type(grouped))

# 获取索引和复合索引
print(grouped.index)

# 获取index：df.index
# 指定index ：df.index = ['x','y']
# 重新设置index : df.reindex(list("abcedf"))
# 指定某一列作为index ：df.set_index("Country",drop=False)
# 返回index的唯一值：df.set_index("Country").index.unique()





