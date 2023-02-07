"""Questão 3
Crie um programa que permita verificar se um número N é fatorial ou não. N é fatorial caso exista um número X >= 0 tal que N = X!.
Entrada:
O programa recebe um número inteiro N maior ou igual a zero.

Saída:
O programa deve imprimir Verdadeiro se N é fatorial, caso contrário deve imprimir Falso.

Exemplos: Entrada N e Saída (Verdadeiro ou Falso), não precisa imprimir na mesma linha.

1 Verdadeiro 
2 Verdadeiro
3 Falso
6 Verdadeiro
12 Falso
24 Verdadeiro
7777 Falso
1307674368000 Verdadeiro
943675496 Falso 
"""

N = -1
while N < 0 or N % 1 != 0: 
  N = float(input('\nInforme um número inteiro > ou = 0: '))
  if N < 0 or  N % 1 != 0:
    print('\nO número deve ser inteiro > ou = 0: ')
N = int(N)

if N == 0:
  print('\n', N, 'Verdadeiro')
else:
  fatorial = 1
  i = 1
  while fatorial <= N:
    fatorial *= i
    i += 1
    if fatorial == N:
      print('\n', N, 'Verdadeiro')
      break
  if fatorial != N:
    print('\n', N,'Falso')