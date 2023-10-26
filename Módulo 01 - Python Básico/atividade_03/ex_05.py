""" Questão 5
Ao observar a curva de velocidade de um motor, um engenheiro percebeu que sempre ocorria uma queda de velocidade 
quando medições eram feitas em intervalos de 10 ms. Após realizar alguns testes, ele observou que tais quedas 
não ocorriam necessariamente no mesmo momento. Intrigado pela falta de padrão, agora ele quer a sua ajuda para 
saber: dado um caso de teste, qual a primeira medição em que ocorreu uma queda de velocidade?

Entrada:
A primeira linha contém um número inteiro N (1 < N ≤ 100) representando a quantidade de medições de velocidade do 
motor em um determinado teste. Cada uma das próximas N linhas consiste de um único inteiro M (0 ≤ M ≤ 10000) 
representando o número de RPM (rotações por minuto) daquela medida.

Saída:
A saída é o índice da medição em que ocorreu a primeira queda de velocidade. Caso não aconteça nenhuma queda, o seu 
programa deve imprimir o número 0. (dica: não precisa armazenar os valores em nenhuma lista, já no mesmo instante 
da leitura deve ser feito o cálculo se o valor lido é menor que o número imediatamente anterior).
"""

while True:
  try:
    N = int(input('\nInforme um número inteiro entre 2 e 100: '))
    if N > 1 and N <= 100:
      break
  except ValueError:
    print('\nO número deve ser um valor inteiro entre 2 e 100: ')
N = int(N)

indice = 0
anterior = 0
queda = False

for i in range(N):
  novo = int(input('\nInforme a %.fª leitura: ' %(i+1)))
  if anterior <= novo:
    anterior = novo
  elif queda == False:
    queda = True
    indice = i + 1
print('\nÍndice:', indice)