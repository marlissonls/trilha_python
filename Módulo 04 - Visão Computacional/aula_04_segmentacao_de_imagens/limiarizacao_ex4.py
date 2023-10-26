import cv2
from matplotlib import pyplot as plt

image = cv2.imread("coins.jpg", 0)

limiar = 160

plt.figure(figsize=(12,4)) 
plt.subplot(131), plt.imshow(image, "gray"), plt.title('Input')
plt.subplot(132), plt.imshow(image < limiar, "gray"), plt.title('Thresholding')
plt.subplot(133), plt.hist(image.ravel(), 256, [0, 256]), plt.title('Hist')
plt.show()