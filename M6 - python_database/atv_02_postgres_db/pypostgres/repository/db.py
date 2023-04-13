"""
Provides Postgres connection
"""

from config.db import db_connect as db

class Postgres:
    """
    Postgres Abstraction
    """
    def __init__(self) -> None:
        self.connect = db
        self.cursor = self.connect.cursor()

    def execute (self, query:str, values:list|None = None):
        """
        Execute a basic query
        """
        if values is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, values)

    def fetch (self):
        """
        Fetch one query
        """
        return self.cursor.fetchone()

    def fetchall (self):
        """
        Fetch all queries
        """
        return self.cursor.fetchall()

    def commit (self):
        """
        Commit query
        """
        self.connect.commit()

    def rollback (self):
        """
        Commit query
        """
        self.connect.rollback()

    def close (self):
        """
        Close connection
        """
        self.cursor.close()
        self.connect.close()