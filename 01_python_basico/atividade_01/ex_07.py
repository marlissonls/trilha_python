"""
Exercício 001-7: Faça um programa que leia um valor inteiro representando um valor em reais e calcule o menor número de cédulas possíveis no qual o valor pode ser decomposto. As cédulas consideradas são as de 200, 100, 50, 20, 10, 5, 2 e 1 reais. Seu programa deve imprimir a quantidade de cada cédula. 

Dica: divisão inteira usa // e resto da divisão usa %.

Assim, o valor total 1317,00 tem quantas notas de R$ 200,00?

qtdNotas200 = valorTotal // 200

resulta 6 notas de 200 e agora o resto seria

restoValor = valorTotal % 200

resulta 117
"""

quantia = int(input("Informe um valor inteiro em reais: "))
notas200 = quantia // 200
resto200 = quantia % 200
notas100 = resto200 // 100
resto100 = resto200 % 100
notas50 = resto100 // 50
resto50 = resto100 % 50
notas20 = resto50 // 20
resto20 = resto50 % 20
notas10 = resto20 // 10
resto10 = resto20 % 10
notas5 = resto10 // 5
resto5 = resto10 % 5
notas2 = resto5 // 2
resto2 = resto5 % 2
notas1 = resto2 // 1
resto1 = resto2 % 1
print("Qtd nodas de R$200:", notas200)
print("Qtd nodas de R$100:", notas100)
print("Qtd nodas de R$50:", notas50)
print("Qtd nodas de R$20:", notas20)
print("Qtd nodas de R$10:", notas10)
print("Qtd nodas de R$5:", notas5)
print("Qtd nodas de R$2:", notas2)
print("Qtd nodas de R$1:", notas1)