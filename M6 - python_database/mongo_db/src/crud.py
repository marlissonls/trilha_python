class CrudOperations:
    def __init__(self, mongo_services):
        self.services = mongo_services

    def create_client(self):
        try:
            first_name = input("Informe o primeiro nome do cliente: ")
            last_name = input("Informe o sobrenome do cliente: ")
            email = input("Informe e-mail do cliente: ")
            if len(first_name) < 3 or len(last_name) < 3 or len(email) < 3 or '@' not in email:
                raise Exception('Dados incorretos!')
            result = self.services.create_client_service(first_name, last_name, email)
        except Exception as Error:
            print('Erro:', Error)
        else:
            print(result)
            #self.display_data.generate_table(result)

    def get_clients(self):
        try:
            result = self.services.get_clients_service()
        except Exception as Error:
            print('Erro:', Error)
        else:
            print(result)
            #self.display_data.generate_table(result)

    def get_clients_by_filter(self):
        try:
            result = self.services.get_clients_by_filter_service(attribute, rule)
        except Exception as Error:
            print(result)
            #self.display_data.generate_table(result)

    def get_client_by_id(self):
        try:
            if id is None:
                id = int(input("Informe o ID do cliente: "))
            result = self.services.get_client_by_id_service(id)
        except ValueError:
            print('Erro: O ID informado é inválido!')
            return False
        except Exception as Error:
            print('Erro:', Error)
            return False
        else:
            print(result)
            #self.display_data.generate_table(result)
            return True

    def update_client_by_id(self):
        try:
            id = int(input("Informe o ID do cliente a ter dados atualizados: "))
            first_name = input("Atualize o primeiro nome do cliente: ")
            last_name = input("Atualize o sobrenome do cliente: ")
            email = input("Atualize e-mail do cliente: ")
            if len(first_name) < 3 or len(last_name) < 3 or (len(email) < 3 or '@' not in email):
                raise Exception('Dados incorretos!')
            result = self.services.update_client_by_id_service(id, first_name, last_name, email)
        except ValueError:
            print('Erro: O ID informado é inválido!')
        except Exception as Error:
            print('Erro:', Error)
        else:
            print(result)
            #self.display_data.generate_table(result)

    def delete_client_by_id(self):
        try:
            id = int(input("Informe o ID do cliente a ser deletado: "))
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
                print('Ok. O cliente continua ativo.')
                return
            else:
                print('Opção inválida!')
                return
        except ValueError:
            print('Erro: O ID informado é inválido!')
        except Exception as Error:
            print('Erro:', Error)
        else:
            print(result)
            #self.display_data.generate_table(result)

    def operate_crud(self):
        while True:
            print("\n")
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