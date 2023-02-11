"""
Questão 1: Faça um programa que lê um caractere C (uma string de tamanho 1) e uma string S. 
O programa deve imprimir a string S com todos os caracteres C (maiúsculos e minúsculos) removidos. 

(Dica 1: Você pode usar o comando str.lower() para converter uma string str para letras minúsculas).
(dica 2: não vale usar a função replace).
"""

C = input('\nInforme um caracter: ')
while len(C) != 1:
  print('\nVocê deve informar apenas um caracter!')
  C = input('\nInforme apenas um caracter: ')
C = C.lower()

S = input('\nInforme uma palavra ou frase: ')
while len(S) < 1:
  print('\nVocê deve informar uma frase com pelo menos 1 caracter!')
  S = input('\nInforme uma palavra ou frase: ')
S = S.lower()

outroS = ''
for i in S:
  if C != S[S.index(i)]:
    outroS += S[S.index(i)]

print(outroS)

#C = input('\nInforme uma letra: ')
#while len(C) != 1 or C.isdigit() == True:
#  print('\nVocê deve informar apenas uma letra!')
#  C = input('\nInforme uma letra: ')

#S = input('\nInforme uma palavra ou frase: ')
#while len(S) < 1 or S.isdigit() == True:
#  print('\nVocê deve informar uma frase com pelo menos 1 caracter!')
#  S = input('\nInforme uma palavra ou frase: ')
#  if S.isdigit() == True:
#    print('\nVocê deve informar ao menos uma letra!')