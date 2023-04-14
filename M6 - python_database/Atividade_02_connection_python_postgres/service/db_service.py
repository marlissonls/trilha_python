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

