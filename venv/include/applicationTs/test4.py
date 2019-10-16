#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/16上午6:50
"""
# 对于一组数据的电影分类情况，如何处理数据
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = './IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
print(df.info())

# print(df.head(1 ))
# 统计分类列表，取出其值，通过逗号进行切割，然后list化
temp_list = df['Genre'].str.split(',').tolist() #[[][]] 这里的数据是列表嵌套列表的形式
# print(temp_list)
# 数据展开
genre_list = list(set(i for j in temp_list for i in j)) # 集合（set）是一个无序的不重复元素序列。
# print(genre_list)
# 构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
# print(zero_df)
# 给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    # 将zerodf中与templist相同的列的元素赋值为1
    # zero_df.loc[i,['sci-fi','Biography']] = 1
    zero_df.loc[i,temp_list[i]] = 1

# print(zero_df.head(3))

# 统计每个分类的电影的数量和
genre_count = zero_df.sum(axis=0)
print(genre_count)

# 排序
genre_count = genre_count.sort_values()
_x = genre_count.index
_y = genre_count.values
# 画图
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.savefig('./apptest4.png')
plt.show()

# 思路：字符串转换成数据，相当于将字符串离散化，转换成数据