"""
Questão 5: Dado um vetor V de n elementos (suponha que n é ímpar e positivo), o semiparticionado de V é obtido pelas seguintes operações: 
a. se o primeiro elemento de V for maior do que o último elemento V, trocar a posição desses dois elementos;
b. se o segundo elemento de V for maior do que penúltimo elemento V, trocar a posição desses dois elementos;
c. se o terceiro elemento de V for maior do que o antepenúltimo elemento de V, trocar a posição desses dois elementos;
…

assim por diante até que as posições dos elementos vizinhos do elemento do meio sejam trocadas, caso necessário.
Se V contém apenas um elemento, o semiparticionado de V é o próprio V. Faça um programa que: 
a. leia um número inteiro n estritamente positivo ímpar (não precisa fazer validação, isto é, suponha que n é fornecido corretamente); 
b. cria um vetor V e lê n valores inteiros do usuário e armazena-os em V;
c. transforme V no semiparticionado de V;
d. imprima o semiparticionado de V.

Entrada: A entrada é um número inteiro n estritamente positivo ímpar, seguidos dos elementos do vetor V. 

Saída: Seu programa deve imprimir na tela o particionado do vetor V. 
"""

#while True:
#  N = input("\nInforme um número positivo ímpar: ")
#  if N.isdigit() == True:
#    N = int(N)
#    if N % 2 != 0 and N >= 1:
#      break

N = int(input("\nInforme um número positivo ímpar: "))

V = []
for i in range(N):
  while True:
    strNumber = input('\nInforme o ' + str(i+1) + 'º número inteiro do vetor: ')
    try:
      V.append(int(strNumber))
      break
    except ValueError:
      print('Informe um número inteiro!')

for i in range(len(V) // 2):
  if V[i] > V[len(V)-i-1]:
    temp = V[i]
    V[i] = V[len(V)-i-1]
    V[len(V)-i-1] = temp

print('\n')
print(V)