#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/25下午11:23
 """
# pandas时间序列问题
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# file_path = './911.csv'
# df = pd.read_csv(file_path)

a = pd.date_range(start='20171230',end='20180131',freq='10D')
a = pd.date_range(start='20171230',periods=10,freq='M')

print(a)
