import numpy as np

x_data = [[ 1,2,3,4,5,6],[1,2,3,4,5,6]]
y_data = [  640.  , 633. ,  619.  , 393.  , 428. ,   27.  , 193.  ,  66. ,  226. , 1591.]
x_np=np.array(x_data)
y_np=np.array(y_data)

x_np=np.concatenate((x_np,x_np), axis=0)
# x_np=x_np+x_np
print(x_np)

print(x_np.shape)