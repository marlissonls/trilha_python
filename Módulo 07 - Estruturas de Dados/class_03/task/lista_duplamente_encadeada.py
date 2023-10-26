class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def vazia(self):
        return self.tamanho == 0

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        if self.vazia():
            self.ultimo = novo_no
        else:
            self.primeiro.anterior = novo_no
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no
        self.tamanho += 1

    def inserir_fim(self, valor):
        novo_no = No(valor)
        if self.vazia():
            self.primeiro = novo_no
        else:
            self.ultimo.proximo = novo_no
            novo_no.anterior = self.ultimo
        self.ultimo = novo_no
        self.tamanho += 1

    def remover_inicio(self):
        if self.vazia():
            raise Exception('Lista vazia')
        dado_removido = self.primeiro.valor
        if self.tamanho == 1:
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None
        self.tamanho -= 1
        return dado_removido

    def remover_fim(self):
        if self.vazia():
            raise Exception('Lista vazia')
        dado_removido = self.ultimo.valor
        if self.tamanho == 1:
            self.primeiro = None
            self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None
        self.tamanho -= 1
        return dado_removido

    def __str__(self):
        if self.vazia():
            return 'Lista vazia'
        string = ''
        atual = self.primeiro
        while atual:
            string += str(atual.valor) + ' <-> '
            atual = atual.proximo
        return string[:-5]  # remove o último '<->'


# Exemplo de uso
lista = ListaDuplamenteEncadeada()

while True:
    print('\nOpções:')
    print('\n1 - Mostrar lista')
    print('2 - Inserir no início da lista')
    print('3 - Inserir no final da lista')
    print('4 - Excluir do início da lista')
    print('4 - Excluir do fim da lista')
    print('5 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            print(lista)
        case '2':
            try:
                valor = int(input('\nInforme o valor númerico a ser inserido no início da lista: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.inserir_inicio(valor)
        case '3':
            try:
                valor = int(input('\nInforme o valor númerico a ser inserido no final da lista: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.inserir_fim(valor)
        case '4':
            lista.remover_inicio()
        case '5':
            lista.remover_fim()
        case '6':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')
