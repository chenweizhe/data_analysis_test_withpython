#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/14上午7:07
"""
# pandas读取外部数据
import pandas as pd
# 读取csv中的文件
df = pd.read_csv('./dogNames2.csv')
print(df)

# pd.read_sql()

# 读取mongodb
