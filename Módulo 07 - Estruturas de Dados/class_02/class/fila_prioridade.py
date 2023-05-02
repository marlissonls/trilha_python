import numpy as np

class FilaPrioridade:
  
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def primeiro(self):
        if self.__fila_vazia():
            return '\nA fila está vazia'
        return self.valores[self.numero_elementos - 1]
    
    def mostrar_fila(self):
        if self.__fila_vazia():
            return '\nA fila está vazia'
        return self.valores
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('\nA fila está cheia')
            return
        
        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('\nA fila está vazia')
            return

        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor

while True:
    try:
        capacidade = int(input('\nInforme o valor da capacidade da fila: '))
    except ValueError:
        print('\nValor inválido! Informe um número inteiro.')
    else:
        break

fila = FilaPrioridade(capacidade)

while True:
    print('\nOpções:')
    print('\n1 - Ver primeiro')
    print('2 - Mostrar fila')
    print('3 - Enfileirar')
    print('4 - Desenfileirar')
    print('5 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            print('\n', fila.primeiro())
        case '2':
            print('\n', fila.mostrar_fila())
        case '3':
            try:
                valor = int(input('\nInforme o valor númerico a ser enfileirado: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                fila.enfileirar(valor)
        case '4':
            fila.desenfileirar()
        case '5':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')