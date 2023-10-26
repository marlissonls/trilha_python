import cv2
import zipfile
from PIL import Image
import requests
from matplotlib import pyplot as plt
import os
import io
import numpy as np
#from skimage import io
#from google.colab.patches import cv2_imshow

if os.path.isdir(f'{os.path.dirname(__file__)}/imgs') is False:
    print('downloading images')
    url = "http://www.imageprocessingplace.com/downloads_V3/dip3e_downloads/dip3e_book_images/DIP3E_CH06_Original_Images.zip"
    zipName = url.split('database/')
    r = requests.get(url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('imgs')

pasta = './imgs/DIP3E_Original_Images_CH06/'

img1 = Image.open(pasta+'Fig0631(a)(strawberries_coffee_full_color).tif')
img1 = np.array(img1)
img1 = img1[:,:,0]
plt.figure(figsize=(4,4))
plt.title('Escala de cinza')
_ = plt.imshow(np.array(img1),'gray')

img2 = Image.open(pasta+'Fig0636(woman_baby_original).tif')
img2 = np.array(img2)
plt.figure(figsize=(4,4))
plt.title('Colorida')
_ = plt.imshow(np.array(img2))


img3 = cv2.imread(pasta+'Fig0628(a)(jupiter-moon.-Io).tif')
img3 = np.array(img3)
plt.figure(figsize=(4,4))
plt.title('Jupiter moon')
_ = plt.imshow(img3[:,:,2],'Blues')

cv2.imwrite('./recortes/recortada.tif', img2[430:500, 380:480,:])

img4 = cv2.imread('./recortes/recortada.tif')
img4 = np.array(img4)

plt.figure(figsize=(4,4))
plt.title('Recorte')
_ = plt.imshow(img4)

plt.show()

print('Nível médio de brilho da imagem em escala de cinza: ' + str(np.average(img1)))
print('Valor médio das faixas RGB, respectivamente: ' + str(np.average(img2[:,:,0])) + ' '
                                                      + str(np.average(img2[:,:,1])) + ' '
                                                      + str(np.average(img2[:,:,2])))