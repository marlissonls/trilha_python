import cv2
from matplotlib import pyplot as plt

image = cv2.imread("coins.jpg", 0)

plt.figure(figsize=(13,5)) 
plt.subplot(121), plt.imshow(image, "gray"), plt.title('Input')
plt.subplot(122), plt.hist(image.ravel(), 256, [0, 256]), plt.title('Hist')
plt.show()

plt.figure(figsize=(13,5)) 
plt.imshow(image > 175, "gray"), plt.title('Thresholding')
plt.show()