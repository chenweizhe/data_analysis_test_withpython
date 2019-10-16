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

# pandas布尔索引
# 联合布尔索引 不能连着写，需要括号括起来，然后用&符号连接起来
print(df[(df["Count_AnimalName"]>800) & (df["Count_AnimalName"]<1000)])

# 使用次数超过700 and 名字长度大于4
print(df[(df["Row_Labels"].str.len()>4) & (df["Count_AnimalName"]>700)])
