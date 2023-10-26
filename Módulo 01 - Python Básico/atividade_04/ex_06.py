"""
Questão 6: O jogo Street Fighter foi um dos primeiros jogos eletrônicos do gênero conhecido como jogos de luta. 
Neste jogo, um mestre de artes marciais, chamado Ryu, enfrenta outros lutadores em um torneio internacional de artes marciais. 
Cada combate entre Ryu e um oponente se dá em uma série de rounds. No início de cada round, cada jogador está com 100 pontos de vida. 
O objetivo é atacar o oponente com diferentes golpes, sendo que cada golpe aplicado subtrai certa quantidade de pontos de vida do outro combatente.
Perde o round aquele jogador cujos pontos de vida chegar primeiro à zero. Vence a luta quem ganhar o maior número de rounds. 

Crie um programa que simule uma luta entre Ryu e Ken e determine quem ganhou a luta. 

Entrada: 
A entrada consiste de uma sequência de inteiros, um em cada linha, representando os valores dos golpes aplicados (valores positivos) e 
recebidos (valores negativos) por Ryu. A luta termina quando o inteiro lido for 0. Um round só termina quando um dos jogadores fica 
com 0 ou menos pontos de vida. Você pode assumir que em cada round pelo menos um golpe será aplicado. 

Saída:
A saída deverá conter apenas uma linha, contendo somente “Ryu venceu”, “Ken venceu” ou “Empate”, de acordo com o resultado geral da luta. 

Exemplo comentado:
Suponha que a sequência de entrada seja composta pelos números: 40, 5, -32, 9, -45, 48, -27, -64, 75, 6, 4, -7, 3, - 39, 0. 
Então temos dois rounds. O primeiro round tem 6 golpes e Ryu ganha, pois 40 + 5 + 9 + 48 = 102 ≥ 100. 
O segundo round tem 8 golpes e Ken ganha, pois 27 + 64 + 7 + 39 = 137 ≥ 100. Logo, o resultado da luta é “Empate”. 
"""

ryuHealth = 100
kenHealth = 100
ryuRounds = 0
kenRounds = 0
RYU = 'RYU WINS'
KEN = 'KEN WINS'
firstPunch = False

round = 1
print('RYU VS KEN')
print('ROUND 01')
print('FIGHT!\n')
while True:
  golpe = int(input())
  if firstPunch == False and golpe == 0:
    print('\nO primeiro golpe não pode ser 0!\n')
  else:
    firstPunch = True
    if golpe > 0:
      kenHealth -= golpe
      if kenHealth <= 0:
        ryuRounds += 1
        if ryuRounds == 2:
          break
        else:
          ryuHealth = 100
          kenHealth = 100
          print('\n'+RYU)
          if round == 1:
            round = 2
            print('\nROUND 02')
            print('FIGHT!\n')
    if golpe < 0:
      ryuHealth += golpe
      if ryuHealth <= 0:
        kenRounds += 1
        if kenRounds == 2:
          break
        else:
          ryuHealth = 100
          kenHealth = 100
          print('\n'+KEN)
          if round == 1:
            round = 2
            print('\nROUND 02')
            print('FIGHT!\n')
    if ryuRounds + kenRounds == 2:
      break
    if golpe == 0:
      if ryuHealth > kenHealth:
        ryuRounds += 1
        print('\n'+RYU)
        break
      if kenHealth > ryuHealth:
        kenRounds += 1
        print('\n'+KEN)
        break
      if ryuHealth == kenHealth:
        print('\nROUND EMPATADO')
        break

if ryuRounds > kenRounds:
  print('\n*'+RYU+'*')
elif kenRounds > ryuRounds:
  print('\n*'+KEN+'*')
else:
  print('\n*EMPATE*')