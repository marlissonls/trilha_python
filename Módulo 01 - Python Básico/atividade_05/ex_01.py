"""
Questão 1
Desenvolva um programa com as seguintes funcionalidades: 

Ler e preencher um vetor com N valores inteiros informados pelo usuário. 
A variável N deve ser lida inicialmente (portanto por usar um comando for para ler os elementos do vetor). 
No vetor lido verificar se há vizinhos consecutivos iguais. 
Imprimir os índices das posições de todos os vizinhos repetidos (veja os exemplos de entrada e saída).

Entrada: um número inteiro N positivo seguido de N valores inteiros. 
Saída: Índices do vetor com vizinhos contendo o mesmo valor.
"""

#def isfloat(num):
#  try:
#     float(num)
#     return True
#  except ValueError:
#     return False

while True:
  N = input('\nInforme o tamanho do vetor: ')
  if N.isdigit() == True:
    N = int(N)
    if N > 1:
      break
    else:
      print('Informe um vetor com pelo menos 2 elementos')

V = []
for i in range(N):
  while True:
    element = input('\nInforme o ' + str(i+1) + 'º elemento numérico inteiro do vetor: ')
    if element.isdigit() == True:
      element = int(element)
      break
  V.append(element)

print('\n')
for i in range(len(V) - 1):
  if V[i] == V[i+1]:
    print('Pos ' + str(i) + ' e ' + str(i+1))