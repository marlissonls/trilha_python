# Exercício 002-1: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Valor: '))
if valor > 0:
  print('O valor informado é positivo')
elif valor < 0:
  print('O valor informado é negativo')
else:
  print('O valor informado é igual a zero')