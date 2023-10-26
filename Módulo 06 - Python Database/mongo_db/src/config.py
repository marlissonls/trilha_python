from pymongo import MongoClient
from os import getenv
import dotenv

dotenv.load_dotenv()

class MongoConnection:
    def __init__(self):
        self.connection = f"mongodb://{getenv('DBUSER')}:{getenv('DBPASSWORD')}@{getenv('DBHOST')}:{getenv('DBPORT')}/{getenv('DBDATABASE')}?authSource=admin"
        self.client = MongoClient(self.connection)