"""
Questão 4: Faça um programa que faz o seguinte: 
a. lê um número inteiro par N fornecido pelo usuário. O programa deve continuar solicitando o número N enquanto o valor entrado não for par;
b. preenche uma lista de tamanho N com números inteiros fornecidos pelo usuário;
c. faz a “dobra ao meio” do vetor. Ou seja, você irá criar um vetor com a metade do número de elementos do vetor original, 
cujas entradas são dadas pela soma dos valores que se encontram quando o vetor é “dobrado ao meio”. Como no exemplo abaixo:

Se o vetor original é dado por:
  v = [4, 5, 8, 9, 3, 7, 6, 1]
O vetor resultante da dobra ao meio será:
  v’ = [5, 11, 15, 12] (em que, 5=4+1, 11=5+6, 15=8+7 e 12=9+3).
"""

while True:
  N = input("\nInforme um número natural par: ")
  if N.isdigit() == True:
    N = int(N)
    if N % 2 == 0 and N >= 2:
      break

V = []
for i in range(N):
  while True:
    strNumber = input('\nInforme o ' + str(i+1) + 'º número inteiro do vetor: ')
    try:
      V.append(int(strNumber))
      break
    except ValueError:
      print('Informe um número inteiro!')

DoubleHalf = []
for i in range(len(V) // 2):
  DoubleHalf.append(V[i]+V[len(V)-i-1])

print('\n')
print(DoubleHalf)