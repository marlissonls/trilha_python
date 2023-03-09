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

files = ['pirate.tif', 'lake.tif', 'lena_color_512.tif']

images = []

for file in files:
  filename, file_extension = os.path.splitext(file)

  if file_extension == '.tif':
    img = cv2.imread(f'./standard_test_images/{file}')
    images.append(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(4,4))
    plt.title(filename)
    plt.imshow(img)

imgCinza = np.array(cv2.cvtColor(images[0], cv2.COLOR_BGR2GRAY))
print(f'média níveis cinza "pirate.tif": {np.average(imgCinza)}')

imgColorida = np.array(cv2.cvtColor(images[2], cv2.COLOR_BGR2RGB))
print(f'média faixa vermelho "lena_color_512.tif": {np.average(imgColorida[:,:,0])}')
print(f'média faixa verde "lena_color_512": {np.average(imgColorida[:,:,1])}')
print(f'média faixa azul "lena_color_512.tif": {np.average(imgColorida[:,:,2])}')

if not os.path.exists('recortes'):
   os.mkdir('recortes')
   
cv2.imwrite(f'./recortes/recorteimg.tif',imgColorida[315:385, 240:340])

recortada = cv2.imread(f'./recortes/recorteimg.tif')
plt.figure(figsize=(4,4))
plt.title("recorteimg.tif")
plt.imshow(recortada)
plt.show()

print(f'imagem recortada info:{recortada.shape}')