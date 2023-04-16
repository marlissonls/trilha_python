from repository.db_operations import DbOperations

class DbQueries:
    def __init__(self, _db_operations: DbOperations):
        self.db_operations: DbOperations = _db_operations

    def create_table(self, db_cursor, table):
        query = f'CREATE TABLE IF NOT EXISTS {table["name"]} ({table["columns"]}{" ".join(map(str, table["foreigns"]))});'
        self.db_operations.execute(db_cursor, query)
    
    def create_client_query(self, db_cursor, first_name, last_name, email):
        query = f'INSERT INTO clients (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING *;'
        values = [first_name, last_name, email]
        self.db_operations.execute(db_cursor, query, values)
        result = self.db_operations.fetchall(db_cursor)
        if len(result) == 0:
            raise Exception('Não foi possível cadastrar este cliente.')
        return result
    
    def get_clients_list_query(self, db_cursor):
        query = f'SELECT * FROM clients;'
        values = None
        self.db_operations.execute(db_cursor, query, values)
        result = self.db_operations.fetchall(db_cursor)
        if len(result) == 0:
            raise Exception('Esta busca não encontrou nenhum cliente.')
        return result
    
    def get_client_by_id_query(self, db_cursor, id):
        query = f'SELECT * FROM clients WHERE id = %s;'
        values = [id]
        self.db_operations.execute(db_cursor, query, values)
        result = self.db_operations.fetchall(db_cursor)
        if len(result) == 0:
            raise Exception(f'Não foi possível encontrar o cliente com id = {id}.')
        return result
    
    def update_client_data_by_id_query(self, db_cursor, id, first_name, last_name, email):
        query = f'UPDATE clients SET first_name = %s, last_name = %s, email = %s WHERE id = %s RETURNING *;'
        values = [first_name, last_name, email, id]
        self.db_operations.execute(db_cursor, query, values)
        result =  self.db_operations.fetchall(db_cursor)
        if len(result) == 0:
            raise Exception(f'Não foi possível atualizar o cliente com id = {id}.')
        return result
    
    def delete_client_by_id_query(self, db_cursor, id):
        query = f'DELETE FROM clients WHERE id = %s RETURNING *;'
        values = [id]
        self.db_operations.execute(db_cursor, query, values)
        result = self.db_operations.fetchall(db_cursor)
        if len(result) == 0:
            raise Exception(f'Não foi possível deletar o cliente com id = {id}.')
        return result