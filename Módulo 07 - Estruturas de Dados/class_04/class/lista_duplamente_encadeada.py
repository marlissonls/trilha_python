class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None
  
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp

    def excluir_final(self):
        temp = self.ultimo
        if self.primeiro.proximo == None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp

    def excluir_posicao(self, valor):
        atual = self.primeiro
        while atual.valor != valor:
            atual = atual.proximo
        if atual == None:
            return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def mostrar_frente(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_tras(self):
        atual = self.ultimo
        while atual != None:
            atual.mostra_no()
            atual = atual.anterior


lista = ListaDuplamenteEncadeada()

while True:
    print('\nOpções:')
    print('\n1 - Mostrar início da lista')
    print('2 - Mostrar Final da lista')
    print('3 - Inserir no início da lista')
    print('4 - Inserir no final da lista')
    print('5 - Excluir do início da lista')
    print('6 - Excluir do final da lista')
    print('7 - Excluir uma posição da lista')
    print('8 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            lista.mostrar_frente()
        case '2':
            lista.mostrar_tras()
        case '3':
            try:
                valor = int(input('\nInforme o valor númerico a ser inserido no início da lista: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.insere_inicio(valor)
        case '4':
            try:
                valor = int(input('\nInforme o valor númerico a ser inserido no final da lista: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.insere_final(valor)
        case '5':
            lista.excluir_inicio()
        case '6':
            lista.excluir_final()
        case '7':
            try:
                valor = int(input('\nInforme o valor da posição do número a ser deletado: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.excluir_posicao(valor)
        case '8':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')