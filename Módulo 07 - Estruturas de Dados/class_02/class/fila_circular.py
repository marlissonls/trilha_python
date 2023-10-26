import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]
    
    def mostrar_fila(self):
        if self.__fila_vazia():
            return '\nA fila está vazia'
        return self.valores

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('\nA fila está cheia')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('\nA fila já está vazia')
            return
        
        temp = self.valores[self.inicio]
        self.inicio += 1
        #if self.inicio == self.capacidade - 1: Corrigido em 05/05/2022
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

while True:
    try:
        capacidade = int(input('\nInforme o valor da capacidade da fila circular: '))
    except ValueError:
        print('\nValor inválido! Informe um número inteiro.')
    else:
        break

fila = FilaCircular(capacidade)

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