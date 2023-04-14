from repository.db_operations import DbOperations

class DbQueries:
    def __init__(self, _db_operations: DbOperations):
        self.db_operations: DbOperations = _db_operations

    def create_table(self, db_cursor, table):
        """ Create a table in Postgres """
        query = f'CREATE TABLE IF NOT EXISTS {table["name"]} ({table["columns"]}{" ".join(map(str, table["foreigns"]))});'
        self.db_operations.execute(db_cursor, query)

    def create_module(self, db_cursor, table_name, module_name:str): #table
        """ Create some module """
        query = f'INSERT INTO {table_name} (name) VALUES (%s) RETURNING id'
        values = [module_name]
        self.db_operations.execute(db_cursor, query, values)
        return self.db_operations.fetch(db_cursor)[0]

    def create_student(self, db_cursor, table_name, first_name:str, last_name:str):
        """ Create some student """
        query = f'INSERT INTO {table_name} (first_name, last_name) VALUES (%s, %s) RETURNING id'
        values = [first_name, last_name]
        self.db_operations.execute(db_cursor, query, values)
        return self.db_operations.fetch(db_cursor)[0]

    def join_student_module(self, db_cursor, table_name, student_id:int, module_id:str):
        """ Join some student with some module """
        query = f'INSERT INTO {table_name} (student_id, module_id) VALUES (%s, %s) RETURNING *'
        values = [student_id, module_id]
        self.db_operations.execute(db_cursor, query, values)
        return self.db_operations.fetch(db_cursor)