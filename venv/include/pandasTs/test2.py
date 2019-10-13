#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/14上午7:13
 """
# 读取mongodb
from  pymongo import MongoClient
import pandas as pd

client = MongoClient()

collection = client['local']['test']
data = list(collection.find())
t1 = data[0]
pd.Series(t1)
print(t1)