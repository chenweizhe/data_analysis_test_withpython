#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/24上午9:02
 """

# 全球排名靠前的10000本书 统计几个问题
# 不同年份书的数量
# 不同年份书的平均评分情况
from matplotlib import pyplot as plt
import pandas as pd

file_path = './books.csv'
df = pd.read_csv(file_path)

# df.dropna()

data1 = df[pd.notnull(df["original_publication_year"])]
grouped = data1.groupby(by='original_publication_year').count()['title']

# todo
print(grouped)
_x = grouped.index
_y = grouped.values


plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(list(range(len(_x)))[::10],_x[::10])
plt.savefig('./test9.png')
plt.show()

# 不同年份书的平均评分情况

