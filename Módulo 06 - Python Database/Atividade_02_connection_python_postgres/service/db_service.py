from repository.db_queries import DbQueries
from repository.db_operations import DbOperations

class DbServices:
    def __init__(self, _db_queries: DbQueries, _db_operations: DbOperations):
        self.db_queries: DbQueries = _db_queries
        self.db_operations: DbOperations = _db_operations

    def create_table(self, table):
        db_cursor = self.db_operations.connect()
        try:
            self.db_queries.create_table(db_cursor, table)
        except Exception as Error:
            self.db_operations.rollback()
            raise Error
        else:
            self.db_operations.commit()
            return f"A tabela '{table['name']}' foi criada ou já existe no banco de dados."
        finally:
            self.db_operations.release(db_cursor)

    def create_client_service(self, first_name, last_name, email):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.create_client_query(db_cursor, first_name, last_name, email)
        except Exception as Error:
            self.db_operations.rollback()
            raise Error
        else:
            self.db_operations.commit()
            return result
        finally:
            self.db_operations.release(db_cursor)
    
    def get_clients_list_service(self):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.get_clients_list_query(db_cursor)
        except Exception as Error:
            self.db_operations.rollback()
            raise Error
        else:
            self.db_operations.commit()
            return result
        finally:
            self.db_operations.release(db_cursor)
    
    def get_client_by_id_service(self, id):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.get_client_by_id_query(db_cursor, id)
        except Exception as Error:
            self.db_operations.rollback()
            raise Error
        else:
            self.db_operations.commit()
            return result
        finally:
            self.db_operations.release(db_cursor)

    def update_client_data_by_id_service(self, id, first_name, last_name, email):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.update_client_data_by_id_query(db_cursor, id, first_name, last_name, email)
        except Exception as Error:
            self.db_operations.rollback()
            raise Error
        else:
            self.db_operations.commit()
            return result
        finally:
            self.db_operations.release(db_cursor)
    
    def delete_client_by_id_service(self, id):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.delete_client_by_id_query(db_cursor, id)
        except Exception as Error:
            self.db_operations.rollback()
            raise Error
        else:
            self.db_operations.commit()
            return result
        finally:
            self.db_operations.release(db_cursor)