"""
Defina uma função chamada weird_prod que recebe como argumento uma lista de números inteiros e devolve 
o produto do primeiro elemento, pelo quadrado do segundo, pelo cubo do terceiro, e assim sucessivamente.
"""

from functools import reduce

#print('Informe alguns números inteiros separados por um espaço: ')
#integers = [int(i) for i in input().split()]

# O método split() converte a string em uma lista[str] de números inteiros.
integers = input("Informe alguns números inteiros separados por um espaço: ").split()

# O método map() converte a lista[str] de números inteiros em uma list[int] de números inteiros.
integers = list(map(int, integers))

# A List comprehension cria uma lista a partir da lista integers, elevando seus elementos a uma potência de acordo com a progressão aritmética 1, 2, 3, 4 ....
# O método reduce() reduz a a lista resultante a um número que é o produto de todos os seus elementos.
weird_prod = reduce((lambda x, y: x * y ), [integers[i] ** (i + 1) for i in range(len(integers))])

print('Usando o método reduce() e List comprehension:')
print(weird_prod)

# Usando o commando for para verificação do código acima
w_prod = 1
for i in range(len(integers)): w_prod = w_prod * integers[i] ** (i + 1)

print('Usando o comando de repetição for:')
print(w_prod)


"""
A linha de código abaixo não funciona quando há elementos repetidos na lista. 
O método list.index(elemento) sempre pega o índice do primeiro elemento repetido.

weird_list = list(map(lambda el: el ** (integers.index(el) + 1), integers))
"""