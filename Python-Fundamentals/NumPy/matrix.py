import numpy as np

# Create a 8x8 matrix and fill it with a checkerboard pattern
a = np.zeros((8,8))
a[::2,::2] = 1
a[1::2,1::2] = 1
b = np.where(a==1, 'X',' ')
print(b)

#create a 10x10 matrix and fill it with $ and * leaving 2 places between them
c = np.zeros((10, 10))
c[::3,::3]=1
c[1::3,1::3]=1
c[2::3,2::3]=1
c = np.where(c==1,'$','*')
print(c)