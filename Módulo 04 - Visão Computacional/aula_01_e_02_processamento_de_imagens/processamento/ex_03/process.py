import cv2
import zipfile
import requests
import matplotlib.pyplot as plt
import os
import io
import numpy as np

if os.path.isdir(f'{os.path.dirname(__file__)}/standard_test_images') is False:
  print('downloading images')
  url = "http://www.imageprocessingplace.com/downloads_V3/root_downloads/image_databases/standard_test_images.zip"
  zipName = url.split('database/')
  r = requests.get(url, stream=True)
  z = zipfile.ZipFile(io.BytesIO(r.content))
  z.extractall()

files = ['peppers_gray.tif', 'walkbridge.tif']

images = []

for file in files:
  filename, file_extension = os.path.splitext(file)

  if file_extension == '.tif':
    img = cv2.imread(f'./standard_test_images/{file}')
    images.append(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

imgCinza = np.array(cv2.cvtColor(images[0], cv2.COLOR_BGR2GRAY), dtype = np.uint8)
plt.figure(figsize=(4,4))
plt.title(files[0])
plt.imshow(imgCinza, 'gray')
print(f'jetplane.tif info: {imgCinza.shape}')

img8 = np.array(cv2.cvtColor(images[1], cv2.COLOR_BGR2GRAY), dtype = np.uint8)
plt.figure(figsize=(4,4))
plt.title(files[1])
plt.imshow(img8, 'gray')
print(f'livingroom.tif info: {img8.shape}')

plt.figure(figsize=(4,4))
plt.title(f'{files[0]} 1-bit')
plt.imshow(imgCinza > 100, 'gray')

img8 = img8 / 256
plt.figure(figsize=(4,4))
plt.title(f'{files[1]} 1-bit')
plt.imshow(img8 > 100, 'gray')
plt.show()