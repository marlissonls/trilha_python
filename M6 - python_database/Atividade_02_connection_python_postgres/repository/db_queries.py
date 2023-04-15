from repository.db_operations import DbOperations

class DbQueries:
    def __init__(self, _db_operations: DbOperations):
        self.db_operations: DbOperations = _db_operations

    def create_table(self, db_cursor, table):
        """ Create a table in Postgres """
        query = f"""
        CREATE TABLE IF NOT EXISTS {table["name"]} (
            {table["columns"]}
            {" ".join(map(str, table["foreigns"]))}
        );"""
        self.db_operations.execute(db_cursor, query)
    
    def create_client(self, db_cursor, first_name, last_name, email):
        """ Create a client on resgister table """
        query = f"""
        INSERT INTO register (first_name, last_name, email) 
        VALUES (%s, %s, %s)
        RETURNING *;"""
        values = [first_name, last_name, email]
        self.db_operations.execute(db_cursor, query, values)
    
    def get_clients(self, db_cursor):
        """ Get the clients list from resgister table """
        query = f'SELECT * FROM register;'
        self.db_operations.execute(db_cursor, query)
    
    def update_client_data(self, db_cursor, id, first_name, last_name, email):
        """ Updates a client data on resgister table """
        query = f"""
        UPDATE register
        SET 
            first_name = %s, 
            last_name = %s, 
            email = %s
        WHERE id = %s;"""
        values = [first_name, last_name, email, id]
        self.db_operations.execute(db_cursor, query, values)
    
    def delete_client(self, db_cursor, id):
        """ Deletes a client registration on register table """
        query = f'DELETE FROM register WHERE id = %s;'
        values = [id]
        self.db_operations.execute(db_cursor, query, values)