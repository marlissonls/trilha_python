from repository.db_operations import DbOperations

class DbQueries:
    def __init__(self, _db_operations: DbOperations):
        self.db_operations: DbOperations = _db_operations

    def create_table(self, db_cursor, table):
        """ Create a table in Postgres """
        query = f'CREATE TABLE IF NOT EXISTS {table["name"]} ({table["columns"]}{" ".join(map(str, table["foreigns"]))});'
        self.db_operations.execute(db_cursor, query)