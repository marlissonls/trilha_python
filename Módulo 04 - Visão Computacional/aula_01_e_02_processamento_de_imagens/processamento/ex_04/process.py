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

if os.path.isdir(f'{os.path.dirname(__file__)}/imgs/DIP3E_CH08_Original_Images') is False:
    print('downloading images')
    url = "http://www.imageprocessingplace.com/downloads_V3/dip3e_downloads/dip3e_book_images/DIP3E_CH08_Original_Images.zip"
    zipName = url.split('database/')
    r = requests.get(url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('imgs')

pasta = './imgs/DIP3E_CH08_Original_Images/'

img2_1 = Image.open(pasta+'Fig0840_0959.tif')
img2_1 = np.array(img2_1)# + np.array(img2_1[:,:,1]) + np.array(img2_1[:,:,2]))/(255*3)
img2_1 = (np.array(img2_1[:,:]))# + np.array(img2_1[:,:,1]) + np.array(img2_1[:,:,2]))
plt.figure(figsize=(4,4))
plt.title('Escala de cinza')
_ = plt.imshow(img2_1,'gray')

img2_2 = Image.open(pasta+'Fig0819(a).tif')
img2_2 = np.array(img2_2)
plt.figure(figsize=(4,4))
plt.title('Colorida 8bits')
_ = plt.imshow(img2_2)

print('Imagem em escala de cinza: ' + str(img2_1.shape) + ' ' + str(img2_1.dtype)) 
print('Imagem em com 8 bits de cor: '+ str(img2_2.shape)+ ' ' + str(img2_2.dtype)) 

img2_1_2 = img2_1 > 127
plt.figure(figsize=(4,4))
plt.title('Preto e branco (1bit)')
_ = plt.imshow(img2_1_2,'gray')


img2_2_2 = (img2_2 > 127)*255
plt.figure(figsize=(4,4))
plt.title('RGB 1bit')
_ = plt.imshow(np.array(img2_2_2))

plt.show()