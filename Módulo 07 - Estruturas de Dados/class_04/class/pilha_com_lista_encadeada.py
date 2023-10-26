class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def lista_vazia(self):
        return self.primeiro == None
  
    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def excluir_inicio(self):
        if self.lista_vazia():
            print('A lista está vazia')
            return None
        
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

class PilhaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeada()

    def empilhar(self, valor):
        self.lista.insere_inicio(valor)

    def desempilhar(self):
        return self.lista.excluir_inicio()

    def pilha_vazia(self):
        return self.lista.lista_vazia()

    def ver_topo(self):
        if self.lista.primeiro == None:
            return -1
        return self.lista.primeiro.valor

pilha = PilhaListaEncadeada()

while True:
    print('\nOpções:')
    print('\n1 - Ver primeiro')
    print('2 - Empilhar')
    print('3 - Desempilhar')
    print('4 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            print('\n', pilha.ver_topo())
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