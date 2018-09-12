from PIL  import Image
import numpy as np
import os
import scipy
os.chdir(r'C:\Users\M10609309\PYTHON_ALL\ML2017FALL_HomeWork\hw0') #我的位置起始有誤，因此才重新設定
im=Image.open('rainbow.png')
im_arry=np.array(im)
im_arry=im_arry[:,:,0:3] #output 不知道位什麼是4-d array，故須要轉換
im_arry=im_arry/2
im_arry=im_arry.astype(np.int8) #會有小數點問題

arrayTimg=Image.fromarray(im_arry,'RGB')
arrayTimg.save('rainbow_new.jpg')
print("OUTPUT OVER")