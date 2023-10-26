import numpy as np

class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade - 1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1
    
    def mostrar_deque(self):
        if self.__deque_vazio():
            return 'O deque está vazio'
        
        return self.valores
  
    def get_inicio(self):
        if self.__deque_vazio():
            return 'O deque está vazio'
        
        return self.valores[self.inicio]

    def get_final(self):
        if self.__deque_vazio() or self.final < 0:
            return 'O deque está vazio'
        
        return self.valores[self.final]

    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return

        # Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Início estiver na primeira posição
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1
        else:
            self.inicio -= 1
        
        self.valores[self.inicio] = valor

    def insere_final(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return

        # Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Final estiver na última posição
        elif self.final == self.capacidade - 1:
            self.final = 0
        else:
            self.final += 1

        self.valores[self.final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio():
            print('O deque já está vazio')
            return

        # Possui somente um elemento
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        else:
        # Volta para a posição inicial
            if self.inicio == self.capacidade - 1:
                self.inicio = 0
            else:
                # Incrementar início para remover o início atual
                self.inicio += 1

    def excluir_final(self):
        if self.__deque_vazio():
            print('O deque já está vazio')
            return
        
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        elif self.inicio == 0:
            self.final = self.capacidade - 1
        else:
            self.final -= 1

while True:
    try:
        capacidade = int(input('\nInforme o valor da capacidade do deque: '))
    except ValueError:
        print('\nValor inválido! Informe um número inteiro.')
    else:
        break

deque = Deque(5)

while True:
    print('\nOpções:')
    print('\n1 - Ver o primeiro')
    print('2 - Ver o último')
    print('3 - Mostrar deque')
    print('4 - Inserir no início')
    print('5 - Inserir no final')
    print('6 - Excluir primeiro')
    print('7 - Excluir último')
    print('8 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            print('\n', deque.get_inicio())
        case '2':
            print('\n', deque.get_final())
        case '3':
            print('\n', deque.mostrar_deque())
        case '4':
            try:
                valor = int(input('\nInforme o valor númerico a ser inserido no ínicio: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                deque.insere_inicio(valor)
        case '5':
            try:
                valor = int(input('\nInforme o valor númerico a ser inserido no final: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                deque.insere_final(valor)
        case '6':
            deque.excluir_inicio()
        case '7':
            deque.excluir_final()
        case '8':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')