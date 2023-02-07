"""
Exercício 001-5: Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de 
vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 5% de comissão sobre 
suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
"""

vendedor = input("Nome do vendedor: ")
salarioFixo = float(input("Salário do vendedor: "))
totalVendas = float(input("Total em vendas do vendedor: "))
comissao = (5 / 100) * totalVendas
salario = salarioFixo + comissao
print("O vendedor", vendedor, "receberá no fim do mês o salário de", round(salario, 2))