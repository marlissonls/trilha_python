"""
Exercício 001-2: Faça um programa que leia os comprimentos dos 3 lados a, b, c de um paralelepípedo. 
Então calcule o seu volume e sua diagonal principal, dados pelas seguintes expressões, respectivamente:

V = a . b . c
d = sqrt ( a2 + b2 +c2 ), sendo sqrt a função raiz quadrada da biblioteca math.

atribuindo os resultados às variáveis V e d. A seguir, apresente as variáveis com as mensagens 
correspondentes, conforme exemplos abaixo. A saída deve imprimir duas casas decimais.
"""
import math
a = float(input("Informe a largura: "))
b = float(input("Informe o comprimento: "))
c = float(input("Informe a altura: "))
V = a * b * c
d = math.sqrt(a ** 2 + b ** 2 + c ** 2)
print("Volume do paralelepípedo: %.2f" %V)
print("Diagonal do paralelepípedo: %.2f" %d)