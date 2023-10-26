import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self._capacidade = capacidade
        self._topo = -1
        self._valores = np.empty(self._capacidade, dtype=int)

    def pilha_cheia(self):
        return self._topo == self._capacidade - 1

    def pilha_vazia(self):
        return self._topo == -1

    def empilhar(self, valor):
        if self.pilha_cheia():
            print('\nA pilha está cheia!')
        else:
            self._topo += 1
            self._valores[self._topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print('\nA pilha está vazia!')
        else:
            self._topo -= 1

    def ver_topo(self):
        if self._topo != -1:
            return self._valores[self._topo]
        else:
            return '\nA pilha está vazia!'
while True:
    try:
        capacidade = int(input('\nInforme o valor da capacidade da pilha: '))
    except ValueError:
        print('\nValor inválido! Informe um número inteiro.')
    else:
        break

pilha = Pilha(capacidade)

while True:
    print('\nOpções:')
    print('\n1 - Ver topo')
    print('2 - Empilhar')
    print('3 - Desempilhar')
    print('4 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            print(pilha.ver_topo())
        case '2':
            try:
                valor = int(input('\nInforme o valor númerico a ser empilhado: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                pilha.empilhar(valor)
        case '3':
            pilha.desempilhar()
        case '4':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')