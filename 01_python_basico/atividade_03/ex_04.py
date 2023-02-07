""" Questão 4
Crie um programa que permita imprimir uma representação de um tabuleiro de xadrez. 

Entrada:
O programa recebe um número inteiro, maior ou igual a 1, que indica a dimensão do tabuleiro.

Saída:
O programa deve desenhar o tabuleiro com dois caracteres que representam as divisões em cores diferentes 
conforme exemplos apresentados a seguir. (dica: print(“x”,end=””) não muda de linha)
"""

D = -1
while D <= 0 or D % 1 != 0: 
  D = float(input('\nInforme a dimensão do tabuleiro: '))
  if D < 0 or  D % 1 != 0:
    print('\nO número deve ser inteiro > ou = 0: ')
D = int(D)

count = 0
for i in range(D):
  for j in range(D):
    if count % 2 == 0:
      print('O', end=' ')
    else:
      print('X', end=' ')
    count += 1
  print('\r')
  if D % 2 == 0:
    count += 1