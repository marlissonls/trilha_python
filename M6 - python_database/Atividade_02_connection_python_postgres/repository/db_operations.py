from config.db_connection import DbConnection

class DbOperations:
    def __init__(self, _db_connection: DbConnection):
        self.connection = _db_connection
        self.db_connect = self.connection.connect_db()

    def execute(self, db_cursor, query: str, values: list | None = None):
        if values is None:
            db_cursor.execute(query)
        else:
            db_cursor.execute(query, values)

    def connect(self):
        return self.db_connect.cursor()

    def release(self, db_cursor):
        db_cursor.close()

    def fetch(self, db_cursor):
        return db_cursor.fetchone()

    def fetchall(self, db_cursor):
        return db_cursor.fetchall()

    def commit(self):
        self.db_connect.commit()

    def rollback(self):
        self.db_connect.rollback()