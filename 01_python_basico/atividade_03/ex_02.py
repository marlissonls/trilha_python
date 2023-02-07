""" Questão 2
Faça um temporizador de segundos (contagem regressiva) que passe a atualizar o tempo mais raramente. 
A contagem com o intervalo entre cada atualização fique dois segundos maior após cada uma delas.
Por exemplo, se ele iniciar o temporizador com 50 segundos, então receberá atualizações dizendo que 
faltam 50, 48, 44, 38, 30, 20 e 8 segundos (note que os intervalos entre as notificações foram 2, 4, 6, 8, 10 e 12 segundos).
Desenvolva um programa que exiba em quais segundos o temporizador receberá atualizações, 
dado que o programa tenha sido inicializado com um tempo igual a N.
Entrada:
O seu programa deve receber um número inteiro positivo N, que é o tempo inicial do temporizador.
Saída:
Seu programa deve escrever a saída conforme os exemplos abaixo.
"""

N = 0
while N <= 0 or N % 1 != 0: 
  N = float(input('\nInforme o tempo do temporizador (segundos): '))
  if N <= 0 or  N % 1 != 0:
    print('\nO número deve ser inteiro positivo!')
N = int(N)

counter = 0
interval = 0
dec = 2
for i in range(N):
  if interval == counter:
    print('Faltam',N,'segundos')
    interval += dec
    dec += 2
  counter += 1
  N -= 1
print('Acabou')