"""
Exercício 001-1: A fórmula para calcular a área de uma circunferência é: área = pi . raio². 
Crie um programa para ler o valor do raio e efetuar o cálculo da área. Entrada: A entrada contém 
um número real, positivo, representando o raio. Saída: Seu programa deve imprimir na tela a área 
do círculo com 4 casas após o ponto decimal.
"""
pi = 3.14
raio = float(input("Raio da circunferência: "))
area = pi * raio ** 2
print("Área da circunferência: %.4f" %area)
#print("Área da circunferência:", round(area, 4))