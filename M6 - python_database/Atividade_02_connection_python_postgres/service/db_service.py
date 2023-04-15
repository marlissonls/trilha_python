from repository.db_operations import DbOperations
from repository.db_queries import DbQueries

class DbServices:
    def __init__(self, _db_operations: DbOperations, _db_queries: DbQueries):
        self.db_operations: DbOperations = _db_operations
        self.db_queries: DbQueries = _db_queries

    def create_table(self, table):
        db_cursor = self.db_operations.connect()
        try:
            self.db_queries.create_table(db_cursor, table)
        except Exception as Error:
            return Error
        else:
            return f'CREATE TABLE {table["name"]}'
        finally:
            self.db_operations.release(db_cursor)

    def create_client(self, first_name, last_name, email):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.create_client(db_cursor, first_name, last_name, email)
        except Exception as Error:
            return Error
        else:
            return result
        finally:
            self.db_operations.release(db_cursor)
    
    def get_clients(self):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.get_clients(db_cursor)
        except Exception as Error:
            return Error
        else:
            return result
        finally:
            self.db_operations.release(db_cursor)

    def update_client_data(self, id, first_name, last_name, email):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.update_client_data(db_cursor, id, first_name, last_name, email)
        except Exception as Error:
            return Error
        else:
            return result
        finally:
            self.db_operations.release(db_cursor)
    
    def delete_client(self, id):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.delete_client(db_cursor, id)
        except Exception as Error:
            return Error
        else:
            return result
        finally:
            self.db_operations.release(db_cursor)