"""
Questão 4: Um pantograma ou pangrama (do grego, pan ou pantós = todos, + grama = letra) é uma frase em que são usadas todas 
as letras do alfabeto de determinada língua. 

Crie um programa que permita verificar se uma frase é ou não um pantograma. Considere que o usuário digitará apenas uma frase. 

Entrada: A entrada contém uma frase sem acentos que pode ter letras maiúsculas ou minúsculas, ou sinais de pontuação. 

Saída: O programa deve imprimir SIM se a frase corresponde a um pantograma. Caso contrário, o programa deve imprimir NAO (sem acento). 
"""

string = input('\nInforme uma string: ')
lowerString = string.lower()
pantograma = 'SIM'
for i in 'abcdefghijklmnopqrstuvwxyz':
  found = 0
  for j in lowerString:
    if i == j:
      found += 1
  if found == 0:
    pantograma = 'NÃO'
    break
print(pantograma)