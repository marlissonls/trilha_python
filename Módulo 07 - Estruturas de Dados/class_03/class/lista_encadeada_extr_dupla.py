class No: 
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
  
    def __lista_vazia(self):
        return self.primeiro == None
    
    def mostrar(self):
        if self.__lista_vazia():
            print('\nA lista está vazia')
            return
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('\nA lista está vazia')
            return

        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp


lista = ListaEncadeadaExtremidadeDupla()

while True:
    print('\nOpções:')
    print('\n1 - Mostrar lista')
    print('2 - Inserir no início da lista')
    print('3 - Inserir no final da lista')
    print('4 - Excluir do início da lista')
    print('5 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            lista.mostrar()
        case '2':
            try:
                valor = int(input('\nInforme o valor númerico a ser inserido no início da lista: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.insere_inicio(valor)
        case '3':
            try:
                valor = int(input('\nInforme o valor númerico a ser inserido no final da lista: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                lista.insere_final(valor)
        case '4':
            lista.excluir_inicio()
        case '5':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')