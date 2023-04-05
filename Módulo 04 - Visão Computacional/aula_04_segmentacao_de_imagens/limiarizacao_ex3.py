import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("coins.jpg", 0)

limiar = 50

plt.figure(figsize=(13,4)) 
plt.subplot(131), plt.imshow(image, "gray"), plt.title('Input')
plt.subplot(132), plt.hist(image.ravel(), 256, [0, 256]), plt.title('Hist')
plt.subplot(133), plt.imshow(image < limiar, "gray"), plt.title('Input')
plt.show()

f = cv2.imread("coins.jpg",0)

limiar = 50

g = np.zeros((f.shape))
L, C = g.shape
for i in range(0,L):
    for j in range(0,C):
        if f[i,j] < limiar:
            g[i,j] = 1
plt.figure(figsize=(10,10)) 
plt.subplot(121), plt.imshow(g, "gray")
plt.subplot(122), plt.imshow(f < limiar, "gray")
plt.show()