import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("coins.jpg")

plt.figure(figsize=(10,10)) 
plt.imshow(image, "gray"), plt.title('Input')
plt.show()


img_ori = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

plt.figure(figsize=(15,10)) 
plt.subplot(121), plt.imshow(image,"gray"), plt.title('Input')
plt.subplot(122), plt.imshow(thresh,"gray"), plt.title('Thresholding')
plt.show()


kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

plt.figure(figsize=(15,10)) 
plt.subplot(121),plt.imshow(opening,"gray"),plt.title('opening')
plt.subplot(122),plt.imshow(sure_bg,"gray"),plt.title('sure_bg')
plt.show()


dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
print(dist_transform.max())
print(0.7*dist_transform.max())
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

plt.figure(figsize=(15,10)) 
plt.subplot(121),plt.imshow(dist_transform,"gray"),plt.title('dist_transform')
plt.subplot(122),plt.imshow(sure_fg,"gray"),plt.title('sure_fg')
plt.show()


plt.imshow(unknown,"gray")
plt.show()


ret, markers = cv2.connectedComponents(sure_fg)
print(markers.min(), markers.max())

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

plt.figure(figsize=(15,10)) 
plt.imshow(markers,"pink"),plt.title('markers')
plt.show()


plt.imshow((markers==24)*255,"gray")
print(np.sum(markers==24)*1)
plt.show()


markers = cv2.watershed(image,markers)
plt.figure(figsize=(15,10)) 
plt.imshow(markers,"gray"),plt.title('markers')
plt.show()


plt.figure(figsize=(15,10)) 
plt.imshow((markers==-1)*255,"gray")
plt.show()


img = img_ori.copy()
img[markers == -1] = [255,0,255]

print(np.amin(markers),np.amax(markers))

plt.figure(figsize=(15,10)) 
plt.imshow(img,"gray"),plt.title('img')
plt.show()
