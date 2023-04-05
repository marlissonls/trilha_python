import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("coins.jpg", 0)

image = image[60:290,100:370]

limiar = 170

plt.figure(figsize=(14,4)) 
plt.subplot(131),plt.imshow(image,"gray"),plt.title('Input')
plt.subplot(132),plt.imshow(image>limiar,"gray"),plt.title('Thresholding')
plt.subplot(133),plt.hist(image.ravel(),256,[0,256]),plt.title('Hist')
plt.show()



precisao = 0.0001

T1 = (int(np.amin(image)) + int(np.amax(image)))/2
print(T1)

done = False
while ~done:
    g = (image >= T1)
    T1next = 0.5*(np.mean(image[g]) + np.mean(image[~g]))
    done = np.abs(T1 - T1next) < precisao
    T1 = T1next 
    print(T1)

T, s1 = cv2.threshold(image,T1,255,cv2.THRESH_BINARY)

hf = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.figure(figsize=(14,4)) 
plt.subplot(131), plt.imshow(image,"gray"), plt.title('Input')
plt.subplot(132), plt.imshow(s1,"gray"), plt.title('Thresholding T1=' + str(T1))
plt.subplot(133), plt.plot(hf), plt.title('Hist')
plt.show()



image = cv2.imread("coins.jpg",0)
image = image[60:290,100:370]
T,c = cv2.threshold(image,0,255,cv2.THRESH_OTSU)
print(T)
plt.figure(figsize=(10,6)) 
plt.subplot(121),plt.imshow(image,"gray"),plt.title('Input')
plt.subplot(122),plt.imshow(c,"gray"),plt.title('Thresholding T='+str(T))
plt.show()