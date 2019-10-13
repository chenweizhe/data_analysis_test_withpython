#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/11上午9:00
"""
# series 一维数组   dataframe二维数组  带索引的数组
import  pandas as pd
t1 = pd.Series([1,2,31,4,5,21])
print(t1) #默认序号

# 指定索引
t2 = pd.Series([1,23,3,2,1],index=list('abcde'))
print(t2)
# 转换类型
print(t2.astype(float))




# 通过字典创建一维数组 也即是键值对 键为索引 值为值
temp_dict = {'name':'xiaohong','age':30,'tel':10086}
t3 = pd.Series(temp_dict)
print(t3)


# series的索引
print(t3['age'])
print(t3[1])

# 取连续多行 取前两行
print(t3[:2])

# 取不连续多行  取 2，3个
print(t3[[1,2]])
print(t3[['name','age']])

# 强行索引 nan

# 布尔索引 选中值大于4的值
print(t2[t2>4])

for i in t3.index:
    print("test",i)

# series 的index和value属性
print(list(t2.index)[:2])
print(t2.values)

print(type(t2.values))


