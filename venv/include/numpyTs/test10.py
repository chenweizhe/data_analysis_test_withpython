#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/7上午11:39
"""
import numpy as np
from matplotlib import pyplot as plt
# numpy读取数据
us_filePath = "./US_video_data_numbers.csv"
us_videos_Path = "./USvideos.csv"

uk_file_path = "./GB_video_data_numbers.csv"
uk_videos_path = "./GBvideos.csv"

t_uk = np.loadtxt(uk_file_path,delimiter=',',dtype="int")
# xuanze xihuanshubi 50wan xiao
t_uk = t_uk[t_uk[:,1]<=500000]

t_uk_comment = t_uk[:,-1]
t_uk_like = t_uk[:,1]



plt.figure(figsize=(20,8),dpi=80)
plt.scatter(t_uk_like,t_uk_comment)

plt.savefig('./test10.png')

plt.show()

#sandiantu