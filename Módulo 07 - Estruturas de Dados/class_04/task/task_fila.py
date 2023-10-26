class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_node(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def empty_list(self):
        return self.first == None
    
    def delete_from_start(self):
        if self.empty_list():
            return '\nThe list is empty!'
        
        temp = self.first
        if self.first.next == None:
            self.last = None
        self.first = self.first.next
        return temp

    def insert_at_end(self, value):
        new = Node(value)
        if self.empty_list():
            self.first = new
        else:
            self.last.next = new
        self.last = new
    
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

class LinkedListRow:
    def __init__(self):
        self.list = LinkedList()

    def add_to_end(self, value):
        self.list.insert_at_end(value)

    def remove_from_front(self):
        return self.list.delete_from_start()
    
    def show_first(self):
        self.list.print_first_item()
    
    def show_all(self):
        self.list.print_list()

fila = LinkedListRow()

while True:
    print('\nOpções:')
    print('\n1 - Ver primeiro da fila')
    print('2 - Ver todos da fila')
    print('3 - Enfileirar')
    print('4 - Desenfileirar')
    print('5 - Sair')
    op = input('\nInforme a opção: ')
    match op:
        case '1':
            fila.show_first()
        case '2':
            fila.show_all()
        case '3':
            try:
                value = int(input('\nInforme o valor númerico a ser enfileirado: '))
            except ValueError:
                print('\nValor inválido! Informe um número inteiro.')
            else:
                fila.add_to_end(value)
        case '4':
            print('\nItem removido:', fila.remove_from_front())
        case '5':
            print('\nSaindo...')
            break
        case _:
            print('\nOpção inválida!')