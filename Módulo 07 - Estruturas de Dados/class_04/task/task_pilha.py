class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_node(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.first = None

    def empty_list(self):
        return self.first == None
  
    def insert_on_start(self, value):
        new = Node(value)
        new.next = self.first
        self.first = new

    def delete_from_start(self):
        if self.empty_list():
            print('\nThe list is empty!')
            return None
        
        temp = self.first
        self.first = self.first.next
        return temp

    def print_first_item(self):
        if self.empty_list():
            print('\nThe list is empty!') 
        else:
            print(self.first.value)
    
    def print_list(self):
        if self.empty_list():
            print('\nThe list is empty!')
        else:
            current = self.first
            while current is not None:
                print(current.get_node())
                current = current.next

class LinkedListPile:
    def __init__(self):
        self.list = LinkedList()

    def stack_up(self, value):
        self.list.insert_on_start(value)

    def unstack(self):
        return self.list.delete_from_start()
    
    def show_top(self):
        self.list.print_first_item()
    
    def show_all(self):
        self.list.print_list()

pilha = LinkedListPile()

while True:
    print('\nOpções:')
    print('\n1 - Ver topo da pilha')
    print('2 - Ver todos da pilha')
    print('3 - Empilhar')
    print('4 - Desempilhar')
    print('5 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            pilha.show_top()
        case '2':
            pilha.show_all()
        case '3':
            try:
                valor = int(input('\nInforme o valor númerico a ser empilhado: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                pilha.stack_up(valor)
        case '4':
            print('\nItem removido do topo:', pilha.unstack())
        case '5':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')