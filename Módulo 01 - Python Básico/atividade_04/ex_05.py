"""
Questão 5: Faça um programa que lê uma string e conta o número de vogais, consoantes, 
espaços e pontuações (caracteres “.”, “,”, “!”, “?”, "-"). 

Observação: é proibido o uso de funções auxiliares, como o count(), por exemplo. 

Entrada: Uma string podendo conter apenas vogais, consoantes, espaços e pontuações (caracteres “.”,“,”,“!”,“?”,"-"). 

Saída: A saída do programa deve ser a porcentagem de cada tipo de caractere na string, com 2 casas após a vírgula. 
"""

string = input('\nInforme uma string: ')
lowerString = string.lower()
qEspaco = 0
qVogal = 0
qpont = 0
qcons = 0
for espaco in lowerString:
  if espaco == ' ':
    qEspaco += 1
for pontuacao in lowerString:
  if pontuacao == '.' or pontuacao == ',' or pontuacao == '!' or pontuacao == '?' or pontuacao == '-':
    qpont += 1
for vogal in lowerString:
  if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
    qVogal += 1
for cons in lowerString:
  if cons == 'b' or cons == 'c' or cons == 'd' or cons == 'f' or cons == 'g' or cons == 'h' or cons == 'j' or cons == 'k' or cons == 'l' or cons == 'm' or cons == 'n' or cons == 'p' or cons == 'q' or cons == 'r' or cons == 's' or cons == 't' or cons == 'v' or cons == 'w' or cons == 'x' or cons == 'y' or cons == 'z':
    qcons += 1

qEspaco *= 100/len(lowerString)
qVogal *= 100/len(lowerString)
qpont *= 100/len(lowerString)
qcons *= 100/len(lowerString)

print('\nPontuações: %.2f' %qpont,'%')
print('\nEspaços: %.2f' %qEspaco,'%')
print('\nVogais: %.2f' %qVogal,'%')
print('\nConsoantes: %.2f' %qcons,'%')