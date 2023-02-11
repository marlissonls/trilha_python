"""
Exercício 001-4: Leia dois números inteiros a, b, e dois números em ponto flutuante x, y. Então calcule a expressão:

a + bx - sqrt(b) + ( (a+b) / (x-y) )

atribuindo o resultado à variável expressao. A seguir, mostre a variável expressao com a mensagem correspondente, conforme 
exemplos abaixo. A saída deve imprimir duas casas decimais.
"""

import math
a = int(input("Informe o número inteiro a: "))
b = int(input("Informe o número inteiro b: "))
x = float(input("Informe o número real x: "))
y = float(input("Informe o número real y: "))
expressao = a + b * x - math.sqrt(b) + ((a + b) / (x - y))
print("Valor da expressão: ", round(expressao, 2))