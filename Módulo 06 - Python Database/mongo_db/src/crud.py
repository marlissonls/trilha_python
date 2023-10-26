class CrudOperations:
    def __init__(self, mongo_services):
        self.services = mongo_services

    def create_client(self):
        try:
            first_name = input("Informe o primeiro nome do cliente: ")
            last_name = input("Informe o sobrenome do cliente: ")
            email = input("Informe e-mail do cliente: ")
            if len(first_name) < 3 or len(last_name) < 3 or len(email) < 3 or '@' not in email:
                raise Exception('Dados incorretos!\n')
            result = self.services.create_client_service(first_name, last_name, email)
        except Exception as Error:
            print('Erro:', Error)
        else:
            print('\n', result.inserted_id, '\n', sep='')
            #self.display_data.generate_table(result)

    def get_clients(self):
        try:
            result = self.services.get_clients_service()
        except Exception as Error:
            print('Erro:', Error)
        else:
            for document in result:
                print(document)
            print('\n')
            #self.display_data.generate_table(result)

    def get_clients_by_filter(self):
        try:
            attribute = input("Informe um dos atributos: first_name, last_name ou email? ")
            rule = input("Informe o argumento da busca. ex1: james: ")
            result = self.services.get_clients_by_filter_service(attribute, rule)    
        except Exception as Error:
            print('\n','Erro: ', Error, sep="")
        else:
            print('\n')
            for document in result:
                print(document)
            print('\n')
            #self.display_data.generate_table(result)

    def get_client_by_id(self, id = None):
        try:
            if id is None:
                id = input("Informe o ID do cliente: ")
            result = self.services.get_client_by_id_service(id)
        except Exception as Error:
            print('\n', 'Erro: ', Error, '\n', sep="")
            return False
        else:
            print('\n', result, '\n', sep="")
            #self.display_data.generate_table(result)
            return True

    def update_client_by_id(self):
        try:
            id = input("Informe o ID do cliente a ter dados atualizados: ")
            first_name = input("Atualize o primeiro nome do cliente: ")
            last_name = input("Atualize o sobrenome do cliente: ")
            email = input("Atualize e-mail do cliente: ")
            if len(first_name) < 3 or len(last_name) < 3 or (len(email) < 3 or '@' not in email):
                raise Exception('Dados incorretos!')
            result = self.services.update_client_by_id_service(id, first_name, last_name, email)
        except Exception as Error:
            print('Erro:', Error)
        else:
            if result.acknowledged:
                print("Operação de atualização bem sucedida\n")
            else:
                print("Falha na operação de atualização\n")
            #self.display_data.generate_table(result)

    def delete_client_by_id(self):
        try:
            id = input("Informe o ID do cliente a ser deletado: ")
            option = None
            if self.get_client_by_id(id):
                print('Gostaria de deletar este cliente?')
                print('1 - Sim.')
                print('2 - Não!')
                option = input('Digite o número da sua uma escolha: ')
            else:
                return
            if option == '1':
                result = self.services.delete_client_by_id_service(id)
            elif option == '2':
                print('Ok. O cliente continua ativo.\n')
                return
            else:
                print('Opção inválida!\n')
                return
        except Exception as Error:
            print('Erro:', Error)
        else:
            if result.acknowledged:
                print("\nOperação de exclusão bem sucedida!\n")
            else:
                print("\nFalha na operação de exclusão!\n")
            #self.display_data.generate_table(result)

    def operate_crud(self):
        while True:
            print("1 - Cadastrar cliente.")
            print("2 - Ver a lista de clientes.")
            print("3 - Filtrar clientes por nome, sobrenome ou email.")
            print("4 - Ver dados de um cliente pelo ID.")
            print("5 - Atualizar dados de um cliente pelo ID.")
            print("6 - Deletar um cliente pelo ID.")
            print("7 - Encerrar operações.")

            option = input("\nSelecione o número de uma das operações: ")
            print('\n')
            match option:
                case '1':
                    self.create_client()
                case '2':
                    self.get_clients()
                case '3':
                    self.get_clients_by_filter()
                case '4':
                    self.get_client_by_id()
                case '5':
                    self.update_client_by_id()
                case '6':
                    self.delete_client_by_id()
                case '7':
                    print("Operações encerradas!")
                    break
                case _:
                    print("Opção inválida!")