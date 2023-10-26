def fibonacci(maximo):
  # Inicialização dos elementos
  elemento_atual, proximo_elemento = 0, 1
  
  # Defina a condição de parada
  while elemento_atual < maximo:
    # Retorna o valor do elemento atual
    yield elemento_atual

    elemento_atual, proximo_elemento = \
        proximo_elemento, elemento_atual + proximo_elemento

if __name__ == '__main__':
  # Cria um generator de números fibonacci menor que 1 milhão
  fibonacci_generator = fibonacci(1000000)

  # Mostra na tela toda a sequencia
  for numero_fibonacci in fibonacci_generator:
    print(numero_fibonacci)