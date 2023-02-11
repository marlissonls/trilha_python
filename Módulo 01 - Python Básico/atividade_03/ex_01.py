""" Questão 1
Desenvolva um programa que simule o funcionamento de uma máquina de somar.

Entrada:
O seu programa receberá um número inteiro não negativo N que denota a quantidade de números que seu programa receberá para computar o valor total da soma. Na sequência seu programa receberá N números reais.

Saída:
O seu programa deve imprimir a frase “Total: ” seguida do valor da soma (com duas casas decimais de precisão).
"""

N = 0
while N <= 0 or N % 1 != 0: 
  N = float(input('\nInforme um número: '))
  if N <= 0 or  N % 1 != 0:
    print('\nO número deve ser inteiro positivo!')
N = int(N)
soma = 0
for i in range(N):
  realNumber = float(input('\nInforme o %.fº número real: ' %(i+1)))
  soma += realNumber

print("\nTotal: %.2f" %soma)