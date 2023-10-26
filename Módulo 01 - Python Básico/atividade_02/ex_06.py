"""
Exercício 002-6: Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do **Imposto de Renda**, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o **Sindicato** e que o **FGTS** corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10% negrito
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220)  : R$ 1100,00 (-) IR (5%)  : R$ 55,00 (-) INSS ( 10%)  : R$ 110,00 FGTS (11%)  : R$ 121,00 Total de descontos  : R$ 165,00 Salário Liquido  : R$ 935,00
"""

valorHora = float(input("Informe o valor da hora de trabalho: "))
horasTotais = float(input("Informe o número total de horas trabalhadas:"))
sBruto = valorHora * horasTotais
if sBruto <= 900:
  IR = 0
elif sBruto <= 1500:
  IR = 0.05
elif sBruto <= 2500:
  IR = 0.1
elif sBruto > 2500:
  IR = 0.2
sindicato = 0.03
FGTS = 0.11
descIR = sBruto * IR
descSindicato = sBruto * sindicato
descTotal = descIR + descSindicato
calcFGTS = sBruto * FGTS
sLiquido = sBruto - descTotal

print("Salário Bruto: (", valorHora, "*", horasTotais, "): R$", sBruto, "(-) IR(",IR*100, "%): R$", descIR, "(-) Sindicato(", sindicato*100, "%): R$", descSindicato, ". FGTS(", FGTS*100, "%): R$", calcFGTS, ". Total de descontos: R$", descTotal, ". Salário líquido: R$", sLiquido)