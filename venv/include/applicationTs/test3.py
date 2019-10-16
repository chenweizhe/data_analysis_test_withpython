#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/15上午11:19
 """
import  pandas as pd
import numpy as np
from matplotlib import  pyplot as plt

file_path = './IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)

# print(df.info())
# 求平均分 导演人数信息

# get mean
print(df['Rating'].mean())
# print(df['Actors'].head(1))
# 获取导演的人数
# print(df['Director'].tolist())
print(len(set(df['Director'].tolist())))

print(len(df['Director'].unique()))
# 获取演员的人数
temp_actors_list = df['Actors'].str.split(', ').tolist()
actor_list =  [i for j in temp_actors_list for i in j]
# actors_num = len(set(actor_list))
# actor_list = list(np.array(temp_actors_list).flatten())
actors_num = len(set(actor_list))

print(actors_num)