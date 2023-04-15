from service.db_service import DbServices

class CrudOperations:
    def __init__(self, db_service: DbServices):
        self.services: DbServices = db_service

    def create_client(self):
        first_name = input("Informe o primeiro nome do cliente: ")
        last_name = input("Informe o sobrenome do cliente: ")
        email = input("Informe e-mail do cliente: ")
        self.services.create_client(first_name, last_name, email)

    def get_clients(self):
        self.services.get_clients()

    def update_client_data(self):
        id = int(input("Informe o ID do cliente a ter dados atualizados: "))
        first_name = input("Atualize o primeiro nome do cliente: ")
        last_name = input("Atualize o sobrenome do cliente: ")
        email = input("Atualize e-mail do cliente: ")
        self.services.update_client_data(id, first_name, last_name, email)

    def delete_client(self):
        id = int(input("Informe o ID do cliente a ser deletado: "))
        self.delete_client(id)
    
    def operate_crud(self):
        while True:
            print("0 - Encerrar operações.")
            print("1 - Cadastrar cliente.")
            print("2 - Ver a lista de clientes.")
            print("3 - Atualizar dados de um cliente pelo ID.")
            print("4 - Deletar um cliente pelo ID.")

            option = int(input("\nEscolha o número de uma das operações: "))
            match option:
                case 0:
                    print("\nOperações encerradas!")
                    self.services.db_operations.connection.disconnect_db()
                    break
                case 1:
                    self.create_client()
                case 2:
                    self.get_clients()
                case 3:
                    self.update_client_data()
                case 4:
                    self.delete_client()
                case _:
                    print("\nOpção inválida!")
