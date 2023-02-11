"""
Questão 2:
Escreva um programa que receba uma sequência de palavras e as imprima em ordem inversa. 

Entrada: A primeira linha da entrada consiste de um número inteiro N representando o número de palavras que serão fornecidas. 
As próximas N linhas consistem de uma única palavra por linha. 

Saída: A saída do seu programa deve consistir de N linhas, onde cada linha consiste de uma única palavra. 
"""

while True:
  N = input('\nInforme a quantidade de palavras: ')
  if N.isdigit() == True:
    N = int(N)
    if N > 0:
      break
    else:
      print('Informe um número inteiro!')

V = []
for i in range(N):
  while True:
    word = input('\nEscreva a ' + str(i+1) + 'ª palavra: ')
    if len(word) > 1:
      V.append(word)
      break

print('\n')
for i in range(len(V)):
  print(V[len(V)-i-1])