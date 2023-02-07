# Exercício 002-4: Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
num3 = float(input('Número 3: '))

if num1 >= num2 and num1 >= num3 and num2 >= num3:
  print(num1, num2, num3)
elif num1 >= num2 and num1 >= num3 and num3 > num2:
  print(num1, num3, num2)

elif num2 >= num1 and num2 >= num3 and num1 >= num3:
  print(num2, num1, num3)
elif num2 >= num1 and num2 >= num3 and num3 > num1:
  print(num2, num3, num1)

elif num3 >= num1 and num3 >= num2 and num1 >= num2:
  print(num3, num1, num2)
elif num3 >= num1 and num3 >= num2 and num2 > num1:
  print(num3, num2, num1)