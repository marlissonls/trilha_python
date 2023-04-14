class DbConnection:
    def __init__(self, connection):
        self.connect = connection

    def connect_db(self):
        return self.connect
    
    def disconnect_db(self):
        return self.connect.close()