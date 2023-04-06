import numpy as np      
import cv2 
import matplotlib.pyplot as plt

# PRIMEIRA ROTINA

f = cv2.imread('img.jpg',0)
f = f[200:550,200:550]
T,img = cv2.threshold(f,0,255,cv2.THRESH_OTSU) #<<<<<<<<<<
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.figure(figsize=(20,12)) 
plt.subplot(121),plt.imshow(f,"gray"),plt.title('Input')
plt.subplot(122),plt.imshow(opening,"gray"),plt.title('Thresholding')
plt.show()
img = opening

def myLabel(img):
  L,C = img.shape
  g = np.zeros(img.shape)
  cor = 1
  pilha = []
  tam_viz = 1 # vizinhança 3x3
  for l in range(L): # varre as linhas da imagem
    for c in range(C): # varre as colunas da image

      if img[l,c] and not g[l,c]: # buscar pixel de objeto não pintado

        pilha.append([l,c]) # colocar na pilha pixel p=[l,c]

        while pilha: # laço para pintar todos os pixel de CADA OBJETO com cor 

          i,j=pilha.pop() # retirar da pilha pixel q=[i,j]

          g[i,j] = cor

          for x in range(-tam_viz,tam_viz+1): # usando uma conectividade fixa 3x3
            for y in range(-tam_viz,tam_viz+1): # ATENÇÃO AQUI!!!

              viz_i = i+x
              viz_j = j+y
              if 0 <= viz_i < L and 0 <= viz_j < C: # está no domínio ?

                # colocar na pilha se é objeto e não foi pintado
                if img[viz_i,viz_j] and not g[viz_i,viz_j]: 

                  pilha.append([viz_i,viz_j]) 

        cor+=1 # incremento para pintar o próximo objeto
  return g


