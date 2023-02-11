"""
Exercício 002-7: O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

    TIPO DE CARNE         ATÉ 5KG - PREÇO       ACIMA DE 5KG - PREÇO
     File Duplo               R$ 5,80                  R$ 4,90
      Alcatra                 R$ 6,80                  R$ 5,90
      Picanha                 R$ 7,80                  R$ 6,90

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara, o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 

- tipo e quantidade de carne;
- preço total;
- tipo de pagamento;
- valor do desconto; e
- valor a pagar.
"""

print("Qual o tipo de carne?")
print("1 - File Duplo")
print("2 - Alcatra")
print("3 - Picanha")
tipo = int(input("Informe o número do tipo da carne: "))
peso = float(input("Informe o peso em quilos da carne: "))
print("Qual o tipo de pagamento?")
print("1 - Cartão Tabajara")
print("2 - Outra forma de pagamento")
pagamento = int(input("Informe o número do tipo de pagamento: "))

if tipo == 1 or tipo == 2 or tipo == 3:
  if pagamento == 1 or pagamento == 2:
    if peso > 0:
      if tipo == 1:
        carne = 'File Duplo'
        if peso <= 5:
          preco = 5.8
        else:
          preco = 4.9
      elif tipo == 2:
        carne = 'Alcatra'
        if peso <= 5:
          preco = 6.8
        else:
          preco = 5.9
      elif tipo == 3:
        carne = 'Picanha'
        if peso <= 5:
          preco = 7.8
        else:
          preco = 6.9
      else:
        print('Tipo incorreto.')
      
      if pagamento == 1:
        tipoPag = "Sim"
        precoTotal = preco * peso * 0.95
      else:
        tipoPag = "Não"
        precoTotal = preco * peso

      desconto = preco*peso - precoTotal
      print("-----------------------------------")
      print(carne, "-", peso, "kg")
      print("Preço Total: R$", preco*peso)
      print("Pagamento com Cartão Tabajara:", tipoPag)
      print("Desconto: R$", round(desconto, 2))
      print("Valor a pagar: R$", precoTotal)
      print("-----------------------------------")
    else:
      print("Peso incorreto.")
  else:
    print("Forma de pagamento incorreta.")
else: 
  print("Tipo incorreto.")