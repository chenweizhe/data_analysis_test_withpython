#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/30下午4:27
"""
# 现在有北上广、深圳、和沈阳5个城市空气质量数据，绘制5个城市PM2.5随时间的变化情况
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = './PM2.5/BeijingPM20100101_20151231.csv'
df = pd.read_csv(file_path)

# print(df.head())
# print(df.info())
# PeriodIndex是时间段 DatatimeIndex是时间戳
# 把分开的时间段转成pandas的时间类型
periods = pd.PeriodIndex(year=df['year'],month=df['month'],day=df['day'],hour=df['hour'],freq='H')
df['datatime'] = periods
# print(periods)
# print(type(periods))
# print(df.head())
# print(type(df['datatime']))
# 把datatime设置成索引
df.set_index('datatime',inplace=True)
# 进行降采样 gaichengyuefentongji
df = df.resample('7D').mean()

# 处理缺失数据 删除
# print(df['PM_US Post'])
# data = df['PM_US Post'].dropna()
# data_CN = df['PM_Dongsi'].dropna()

data = df['PM_US Post']
data_CN = df['PM_Dongsi']
# print(data)
# 画图
_x = data.index
_x = [i.strftime('%Y%m%d') for i in _x]
_x_CN = [i.strftime('%Y%m%d') for i in data_CN.index]
_y = data.values
_y_CN = data_CN.values

plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y,label='US_PM')
plt.plot(range(len(_x)),_y_CN,label='CN_PM')
plt.xticks(range(0,len(_x_CN),10),list(_x)[::10],rotation=45)
# plt.xticks(range(0,len(_x),10),list(_x_CN)[::10],rotation=45)

plt.legend(loc='best')

plt.show()
