class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
  
    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
        
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def pesquisa(self, valor):
        if self.primeiro == None:
            print('A lista está vazia')
            return None

        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo
        return atual

    def excluir_inicio(self):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
        
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def excluir_posicao(self, valor):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
        
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        return atual


lista = ListaEncadeada()

while True:
    print('\nOpções:')
    print('\n1 - Mostrar lista')
    print('2 - Inserir no início')
    print('3 - Pesquisar')
    print('4 - Excluir no início')
    print('5 - Excluir na posição')
    print('6 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            lista.mostrar()
        case '2':
            try:
                valor = int(input('\nInforme o valor númerico a ser enfileirado: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.insere_inicio(valor)
        case '3':
            try:
                valor = int(input('\nInforme o valor númerico a ser enfileirado: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.pesquisa(valor)
        case '4':
            lista.excluir_inicio()
        case '5':
            try:
                valor = int(input('\nInforme o valor númerico a ser enfileirado: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.excluir_posicao(valor)
        case '6':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')