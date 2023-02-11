"""
**Exercício 001-3:** A conversão de graus Fahrenheit para Celsius é dada pela expressão:

C . 1.8 = F - 32

e a conversão de Kelvin para graus Celsius é dada por

C = k - 273.15

Faça um programa que recebe como entrada a temperatura em graus Celsius e realize duas 
conversões: uma para Fahrenheit e outra para Kelvin.
"""

C = float(input("Informe a temperatura em °C: "))
F = (C * 9/5) + 32
K = C + 273.15
print("Temperatura em Fahrenheit: %.2f" %F)
print("Temperatura em Kelvin: %.2f" %K)