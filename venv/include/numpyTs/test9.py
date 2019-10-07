#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/7上午10:45
"""
import numpy as np
from matplotlib import pyplot as plt
# numpy读取数据
us_filePath = "./US_video_data_numbers.csv"
us_videos_Path = "./USvideos.csv"

uk_file_path = "./GB_video_data_numbers.csv"
uk_videos_path = "./GBvideos.csv"

t_us = np.loadtxt(us_filePath,delimiter=',',dtype="int",unpack=True)
# print(t1)
t_uk = np.loadtxt(us_filePath,delimiter=',',dtype="int",unpack=False)

# qudao pinglundeshuju
print(t_us)
t_us_comments = t_us[-1,:]
print(t_us_comments)
t_us_comments = t_us_comments[t_us_comments<=5000]
print(t_us_comments.max(),t_us_comments.min())
d = 50
bin_nums = (t_us_comments.max() - t_us_comments.min())//d

plt.figure(figsize=(20,8),dpi=80)
plt.hist(t_us_comments,bin_nums)
plt.savefig('./test9.png')

plt.show()