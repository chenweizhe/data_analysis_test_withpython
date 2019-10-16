#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/14上午7:34
 """
# pandas的DataFrame 二维的 series容器
import pandas as pd
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(t1)

# index行索引 column列索引
t1 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list('abc'),columns=list('WXYZ'))
print(t1)

# 那么问题来了：
# DataFrame和Series有什么关系呢？ series容器
#
# Series能够传入字典，那么DataFrame能够传入字典作为数据么？那么mongodb的数据是不是也可以这样传入呢？
#
# 对于一个dataframe类型，既有行索引，又有列索引，我们能够对他做什么操作呢

# 定义字典
d1 = {'name':['xiaoming','xiaohong'],'age':[20,32],'tel':[10086,10010]}
# 传入字典
p1 = pd.DataFrame(d1)
print(p1)

# 传入列表字典
d2 = [{'name':'xiaoming','age':32,'tel':10010},{'name':'xiaogang','tel':10000},{'name':'xiaowang','age':22}]
p1 = pd.DataFrame(d2)
print(p1)

# nan数据填充
print(p1.fillna(0))
print(p1.fillna(100))
# 一般来说会填充均值
print(p1.fillna(p1.mean()))
# 也可以只填充其中的一列
print(p1['age'].fillna(p1['age'].mean()))

# p1['age'] = p1['age'].fillna(p1['age'].mean())
print(p1)

# 处理为0的数据，计算均值时，可以将0处理成nan，nan不会参与到运算，而0会 所以
# 当然并不是所有的0都需要处理


