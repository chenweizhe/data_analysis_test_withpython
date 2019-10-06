# coding = utf-8
import numpy as np

# 轴  axis = 0,1,2...

# numpy读取数据
us_filePath = "./US_video_data_numbers.csv"
us_videos_Path = "./USvideos.csv"

uk_file_path = "./GB_video_data_numbers.csv"
uk_videos_path = "./GBvideos.csv"

# t1 = np.loadtxt(us_filePath,delimiter=',',dtype="int",unpack=True)
# print(t1)
t2 = np.loadtxt(us_filePath,delimiter=',',dtype="int",unpack=False)
print(t2)

print("*"*100)
# numpy切片
# 取行
# print(t2[2])

# print('*'*100)
#取连续多行
# print(t2[2:])

# 取不连续多行数据 ,取第2行，第8行,第10行 方括号
print(t2[[2,8,10]])

# qulie douhao qian qu hang hou qulie
# print(t2[,2])
# # qu diyihang maohaobiaoshimeiyiliedouyao
# print(t2[1,:])
# # quduohang
# print(t2[2:,:])
# # qu bulianxuduohang
# print(t2[[2,10,3],:])

print('*'*100)
# qulie
print(t2[:,0])
print('*'*100)

# qulianxuduolie
print(t2[:,2:])
print('*'*100)

# qu bulianxu duolie
print(t2[:,[0,2]])

#qu duohang duolie 3hang4liedezhi
print('*'*100)
a = t2[2,3]
print(a)
print(type(a))

print('*'*100)

# qudisanhangdaodisihang dierliedaodisilie
# qudeshihanghelie jiaochadiande weizhi
b = t2[2:5,1:4]
print(b)

print('*'*19)
# qu duoge buxianglin de dian (0,0)he(2,1)lianggedian
c = t2[[0,2,2],[0,1,3]] #qianmianshihanghao houmianshiliehao
print(c)