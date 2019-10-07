# coding utf-8
import numpy as np
# jiazai guojia shuju
us_data = "./US_video_data_numbers.csv"
# us_videos_Path = "./USvideos.csv"
uk_data = "./GB_video_data_numbers.csv"
# uk_videos_path = "./GBvideos.csv"

us_data = np.loadtxt(us_data,delimiter=",",dtype=int)
uk_data = np.loadtxt(uk_data,delimiter=',',dtype=int)

# tianjiaguojia xinxi
# gouzao quanwei0 de shuju
zero_data = np.zeros((us_data.shape[0],1)).astype(int)
one_data  = np.ones((uk_data.shape[0],1)).astype(int)

us_data = np.hstack((us_data,zero_data))
uk_data = np.hstack((uk_data,one_data))
# pingjieliangzu shuju
# cuizhi pingjie
final_data = np.vstack((us_data,uk_data))
# print(final_data)

# chuangjian quanwei 0 de shuzu
# print(np.zeros((2,3)))
# print(np.ones((3,4)))
#
# # duijiaoxian quanwei 1 de shuzu  jishi danwei shuzu
# print(np.eye(5))

# huoquzuidazhizuixiaozhide weizhi
t = np.eye(4)
# print(np.argmax(t,axis=0))

t[t==1] = -1
# print(np.argmin(t,axis=1))


# chansheng suijishu weidu junyunfenbu
# print(np.random.rand(3,2,2))

# zhengtaifenbu
# print(np.random.randn(3,4))

# youfanweide suiji zhengshu
# print(np.random.randint(10,20,(3,4)))

# chansheng junyunfenbu de shuzu
# print(np.random.uniform(10,30,(4,4)))

# suiji zhongzishu gudinghao zhongzi hou zhihouchanshengde suijishu jiubuhui gaibian
# np.random.seed(10)
# print(np.random.uniform(1,10,(2,2)))

# view he a=b doushi qiankaobei a he b xianghu yinxiang

# shen kaobei
a = np.arange(10)
b = a.copy() #a he b huxiang buyinxiang
