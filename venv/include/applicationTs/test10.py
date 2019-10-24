#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/24上午9:16
 """

# 不同年份书的平均评分情况
from matplotlib import pyplot as plt
import pandas as pd

file_path = './books.csv'
df = pd.read_csv(file_path)
# 去除nan的行
data1 = df[pd.notnull(df['original_publication_year'])]
# 不同年份书的平均评分情况
grouped = data1['average_rating'].groupby(by=data1['original_publication_year']).mean()
print(grouped)

_x = grouped.index
_y = grouped.values

plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y)
# 数量太多太恶心 取步长
plt.xticks(list(range(len(_x)))[::10],_x[::10].astype(int),rotation=45)
plt.savefig('./test10.png')
plt.show()
