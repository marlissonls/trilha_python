from repository.db_operations import DbOperations
from repository.db_queries import DbQueries

class DbServices:
    def __init__(self, _db_operations: DbOperations, _db_queries: DbQueries):
        self.db_operations: DbOperations = _db_operations
        self.db_queries: DbQueries = _db_queries

    def create_table(self, table):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.create_table(db_cursor, table)
        except Exception as Error:
            print(Error)
        else:
            return result
        finally:
            self.db_operations.release(db_cursor)

    def create_module(self, table_name, module_name:str):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.create_module(db_cursor, table_name, module_name)
        except Exception as Error:
            print(Error)
        else:
            return result
        finally:
            self.db_operations.release(db_cursor)

    def create_student(self, table_name, first_name, last_name):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.create_student(db_cursor, table_name, first_name, last_name)
        except Exception as Error:
            print(Error)
        else:
            return result
        finally:
            self.db_operations.release(db_cursor)

    def join_student_module(self, table_name, student_id:int, module_id:str):
        db_cursor = self.db_operations.connect()
        try:
            result = self.db_queries.join_student_module(db_cursor, table_name, student_id, module_id)
        except Exception as Error:
            print(Error)
        else:
            return result
        finally:
            self.db_operations.release(db_cursor)

