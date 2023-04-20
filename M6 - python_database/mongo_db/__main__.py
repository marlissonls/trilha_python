from src.config import MongoConfigs
from src.service import MongoServices
from src.crud import CrudOperations

collection_name = "clients"
configs = MongoConfigs(collection_name)
service = MongoServices(configs)
crud = CrudOperations(service)

crud.operate_crud()