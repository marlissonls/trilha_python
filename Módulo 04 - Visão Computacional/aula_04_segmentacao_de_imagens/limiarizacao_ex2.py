import cv2
from matplotlib import pyplot as plt

image = cv2.imread("coins.jpg", 0)

plt.figure(figsize=(13,5)) 
plt.subplot(121), plt.imshow(image, "gray"), plt.title('Input')
plt.subplot(122), plt.hist(image.ravel(), 256, [0, 256]), plt.title('Hist')
plt.show()

limiar = 50
plt.figure(figsize=(13,5)) 
plt.subplot(121), plt.imshow(image, "gray"), plt.title('Input')
plt.subplot(122), plt.imshow(image < limiar, "gray"), plt.title('Valor Baixo: ' + str(limiar))
plt.show()

limiar = 125
plt.figure(figsize=(13,5)) 
plt.subplot(121), plt.imshow(image, "gray"), plt.title('Input')
plt.subplot(122), plt.imshow(image < limiar, "gray"), plt.title('Valor Alto: ' + str(limiar))
plt.show()

limiar = 68
plt.figure(figsize=(13,5)) 
plt.subplot(121), plt.imshow(image, "gray"), plt.title('Input')
plt.subplot(122), plt.imshow(image < limiar, "gray"), plt.title('Valor ideal (???): ' + str(limiar))
plt.show()