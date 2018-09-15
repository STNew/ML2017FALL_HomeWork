
# coding: utf-8

# In[107]:

import pandas as pd
import numpy as np
import scipy as sc
import csv
import matplotlib.pyplot as plt
# import matplotlib 
# matplotlib.use('Agg')
import os
import pandas as pd
import random 



# # 資料處理

# In[210]:

cs_data=pd.read_csv('./train.csv', engine='python')

'''去除說明欄位'''
cs_data=cs_data.drop(['測站'],axis=1)
cs_data=cs_data.drop(['測項'],axis=1)
cs_data=cs_data.drop([ '日期'],axis=1)
cs_data=cs_data.as_matrix() #轉換成 array


'''轉換為(18監測指標,個小時)之格式 '''

data=np.split(cs_data, 240, axis=0)
data=np.hstack(data)
data=np.delete(data, 10, 0) #去除下雨數值(無用途之數值)
data=data.T.astype(float)
print(data.shape)


#標準化資料
from sklearn import preprocessing
data=preprocessing.scale(data)


# In[253]:

iteration=500
b=1
w=np.ones((9,17))
b_history=[b]
w_history=[w]
lr=10
b_lr =0
w_lr = np.zeros((9,17))
loss_temp=[]
loss_history=[0]
for _ in range(iteration):
    b_grad =0
    w_grad = np.zeros((9,17))
    for i in range(9,5760):
        x=data[i-9:i]
        y=data[i][9]
        loss=y- b - np.sum(w*x)
        b_grad = b_grad - 2.0*(loss)*1.0
        w_grad = w_grad - 2.0*(loss)*x
        loss_temp.append(loss)
        
##TYPE II update fun.
    b_lr = b_lr + b_grad**2
    w_lr = w_lr + w_grad**2
    b = b - lr/np.sqrt(b_lr) * b_grad 
    w = w - lr/np.sqrt(w_lr) * w_grad
##
##TYPE I update fun.
#         b = b - lr * b_grad 
#         w = w - lr * w_grad
##

    b_history.append(b)
    w_history.append(w)
    loss_history.append((sum(loss_temp)**2)/len(loss_temp))
    print((sum(loss_temp)**2)/len(loss_temp))  #評量loss byRMSE
        


# # 畫圖

# In[254]:

plt.plot(loss_history)

plt.show()

