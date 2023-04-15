from service.db_service import DbServices
from displaydata.displaydata import DisplayData

class CrudOperations:
    def __init__(self, db_service: DbServices, display_data: DisplayData):
        self.services: DbServices = db_service
        self.display_data: DisplayData = display_data

    def create_client(self):
        first_name = input("Informe o primeiro nome do cliente: ")
        last_name = input("Informe o sobrenome do cliente: ")
        email = input("Informe e-mail do cliente: ")
        result = self.services.create_client_service(first_name, last_name, email)
        self.display_data.generate_table(result)

    def get_clients_list(self):
        result = self.services.get_clients_list_service()
        self.display_data.generate_table(result)
    
    def get_client_by_id(self):
        id = int(input("Informe o ID do cliente: "))
        result = self.services.get_client_by_id_service(id)
        self.display_data.generate_table(result)

    def update_client_data_by_id(self):
        id = int(input("Informe o ID do cliente a ter dados atualizados: "))
        first_name = input("Atualize o primeiro nome do cliente: ")
        last_name = input("Atualize o sobrenome do cliente: ")
        email = input("Atualize e-mail do cliente: ")
        result = self.services.update_client_data_by_id_service(id, first_name, last_name, email)
        self.display_data.generate_table(result)

    def delete_client_by_id(self):
        id = int(input("Informe o ID do cliente a ser deletado: "))
        result = self.services.delete_client_by_id_service(id)
        self.display_data.generate_table(result)
    
    def operate_crud(self):
        while True:
            print("\n")
            print("1 - Cadastrar cliente.")
            print("2 - Ver a lista de clientes.")
            print("3 - Ver dados do cliente pelo ID.")
            print("4 - Atualizar dados de um cliente pelo ID.")
            print("5 - Deletar um cliente pelo ID.")
            print("6 - Encerrar operações.")

            option = input("\nSelecione o número de uma das operações: ")
            print('\n')
            match option:
                case '1':
                    self.create_client()
                case '2':
                    self.get_clients_list()
                case '3':
                    self.get_client_by_id()
                case '4':
                    self.update_client_data_by_id()
                case '5':
                    self.delete_client_by_id()
                case '6':
                    print("Operações encerradas!")
                    self.services.db_operations.connection.disconnect_db()
                    break
                case _:
                    print("Opção inválida!")