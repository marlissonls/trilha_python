from os import getenv
import dotenv

dotenv.load_dotenv()

from src.config import MongoConnection
from src.service import MongoServices
from src.crud import CrudOperations

try:
    mongo_connection = MongoConnection()
    print("mongoDB is connected!")
    mongo_db = mongo_connection.client[getenv('DBDATABASE')]
    print(f"mongoDB database `{getenv('DBDATABASE')}` created!")
    collection_name = "clients"
    collection = mongo_db[collection_name]
    print(f"Collection `{collection_name}` created on `{getenv('DBDATABASE')}` database.\n")
except Exception as Error:
    print(Error)
else:
    mongo_services = MongoServices(collection)
    mongo_crud = CrudOperations(mongo_services)
finally:
    mongo_crud.operate_crud()