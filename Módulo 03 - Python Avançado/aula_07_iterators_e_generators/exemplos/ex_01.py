class Fibonacci:
  def __init__(self, maximo=1000000):
    # Inicializa os dois primeiros numeros
    self.elemento_atual, self.proximo_elemento = 0, 1
    self.maximo = maximo

  def __iter__(self):
    # Retorna o objeto iterável (ele próprio: self)
    return self

  def __next__(self):
    # Fim da iteração, raise StopIteration
    if self.elemento_atual > self.maximo:
      raise StopIteration

    # Salva o valor a ser retornado
    valor_de_retorno = self.elemento_atual

    # Atualiza o próximo elemento da sequencia
    self.elemento_atual, self.proximo_elemento = self.proximo_elemento, self.elemento_atual + self.proximo_elemento

    return valor_de_retorno
        
# Executa nosso código
if __name__ == '__main__':
  # Cria nosso objeto iterável
  objeto_fibonacci = Fibonacci(maximo=1000000)

  # Itera nossa sequencia
  for fibonacci in objeto_fibonacci:
    print("Sequencia: {}".format(fibonacci))