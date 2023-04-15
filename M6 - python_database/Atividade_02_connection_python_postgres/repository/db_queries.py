from repository.db_operations import DbOperations

class DbQueries:
    def __init__(self, _db_operations: DbOperations):
        self.db_operations: DbOperations = _db_operations

    def create_table(self, db_cursor, table):
        query = f'CREATE TABLE IF NOT EXISTS {table["name"]} ({table["columns"]}{" ".join(map(str, table["foreigns"]))});'
        self.db_operations.execute(db_cursor, query)
    
    def create_client_query(self, db_cursor, first_name, last_name, email):
        query = f'INSERT INTO register (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING *;'
        values = [first_name, last_name, email]
        self.db_operations.execute(db_cursor, query, values)
        return self.db_operations.fetch(db_cursor)
    
    def get_clients_list_query(self, db_cursor):
        query = f'SELECT * FROM register;'
        values = None
        self.db_operations.execute(db_cursor, query, values)
        return self.db_operations.fetchall(db_cursor)
    
    def get_client_by_id_query(self, db_cursor, id):
        query = f'SELECT * FROM register WHERE id = %s;'
        values = [id]
        self.db_operations.execute(db_cursor, query, values)
        return self.db_operations.fetch(db_cursor)
    
    def update_client_data_by_id_query(self, db_cursor, id, first_name, last_name, email):
        query = f'UPDATE register SET first_name = %s, last_name = %s, email = %s WHERE id = %s RETURNING *;'
        values = [first_name, last_name, email, id]
        self.db_operations.execute(db_cursor, query, values)
        return self.db_operations.fetch(db_cursor)
    
    def delete_client_by_id_query(self, db_cursor, id):
        query = f'DELETE FROM register WHERE id = %s RETURNING *;'
        values = [id]
        self.db_operations.execute(db_cursor, query, values)
        return self.db_operations.fetch(db_cursor)