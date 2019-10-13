#-*-coding:utf-8-*- 
"""
 @anthor:coingzhe
 @contact:codingzhe@gmail.com
 @time:2019/10/7上午10:24
"""
import numpy as np


# print(t1) 将数组中的nan替换成数组的均值

def fill_narray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:,i] #qiankaobei
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:
            temp_not_nan_col = temp_col[temp_col == temp_col]
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()

    return t1

if __name__ == '__main__':
    t1 = np.arange(24).reshape((4, 6)).astype(float)
    t1[1, 2:] = np.nan
    print(t1)
    print('*'*100)
    t1 = fill_narray(t1)
    print(t1)

