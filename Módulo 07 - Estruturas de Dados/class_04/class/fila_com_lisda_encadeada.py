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

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo
  
    def excluir_inicio(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp

class FilaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeadaExtremidadeDupla()

    def fila_vazia(self):
        return self.lista.__lista_vazia()
  
    def enfileirar(self, valor):
        self.lista.insere_final(valor)

    def desenfileirar(self):
        return self.lista.excluir_inicio()

    def ver_inicio(self):
        if self.lista.primeiro == None:
            return 'A fila está vazia'
        return self.lista.primeiro.valor

fila = FilaListaEncadeada()

while True:
    print('\nOpções:')
    print('\n1 - Ver primeiro')
    print('2 - Enfileirar')
    print('3 - Desenfileirar')
    print('4 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            print('\n', fila.ver_inicio())
        case '2':
            try:
                valor = int(input('\nInforme o valor númerico a ser enfileirado: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                fila.enfileirar(valor)
        case '3':
            fila.desenfileirar()
        case '4':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')