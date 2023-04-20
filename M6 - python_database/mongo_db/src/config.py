from pymongo import MongoClient
from os import getenv
import dotenv

dotenv.load_dotenv()

class MongoConfigs:
    def __init__(self, collection_name: str):
        self.connection = f"mongodb://{getenv('DBUSER')}:{getenv('DBPASSWORD')}@{getenv('DBHOST')}:{getenv('DBPORT')}/{getenv('DBDATABASE')}?authSource=admin"
        self.client = MongoClient(self.connection)
        self.pymongo_db = self.client[getenv('DBDATABASE')]
        self.collection = self.pymongo_db[collection_name]
        print(f"Tabela `{collection_name}` criada no banco de dados Mongodb.\n")