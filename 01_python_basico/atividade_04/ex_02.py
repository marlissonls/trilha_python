"""
Questão 2: Faça um programa que leia uma string e remova todas as suas vogais. 
Considere que o usuário digitará apenas palavras (strings) sem acento. 

Entrada: 
A entrada contém uma única string, sem acento, que pode ter letras maiúsculas ou minúsculas.

Saída: 
Seu programa deve imprimir na tela a string resultante da exclusão de todas as suas vogais. 
Se o usuário digitar uma palavra que contém apenas vogais, o programa deve imprimir a string 
vazia (“”), o que corresponde a uma saída “em branco”. 
"""

S = input('\nInforme uma palavra ou frase sem acentuações: ')
while len(S) < 1:
  print('\nVocê deve informar uma frase com pelo menos 1 caracter!')
  S = input('\nInforme uma palavra ou frase sem acentuações: ')

outroS = ''
for i in S:
  if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U':
    outroS += i

print(outroS)