from pymongo import MongoClient
from os import getenv
import dotenv

# Carregando as variáveis de ambiente definidas no arquivo .env
dotenv.load_dotenv()

# Conectando ao servidor do MongoDB
connection = f"mongodb://{getenv('DBUSER')}:{getenv('DBPASSWORD')}@{getenv('DBHOST')}:{getenv('DBPORT')}/{getenv('DBDATABASE')}?authSource=admin"

# Criando o cliente de acesso ao mongodb
client = MongoClient(connection)

# Selecionando o banco de dados
pymongo_db = client[getenv('DBDATABASE')]

# Selecionando a coleção
collection = pymongo_db["clients"]

# CREATE
# Inserindo um documento na coleção
def create_client_service(fist_name, last_name, email):
    document = {"fist_name": fist_name, "last_name": last_name, "email": email}
    result = collection.insert_one(document)
    return result

# READ
# Lendo todos os documentos na coleção
def get_clients_service():
    documents = collection.find()
    return documents

# Lendo documentos com regra de filtragem
def get_clients_by_filter_service(attribute, rule):
    filtered_documents = collection.find({attribute: rule})
    return filtered_documents
#doc = get_clients_by_filter("first_name", "joão")
#doc2 = get_clients_by_filter("age", {"$gt": 30})

# Lendo um documento específico por ID
def get_client_by_id_service(id):
    document = collection.find_one({"_id": id})
    return document

# UPDATE
# Atualizando um documento
def update_client_by_id_service(id, attribute, value):
    result = collection.update_one({"_id": id}, {"$set": {attribute: value}})
    return result
#doc = get_clients_by_filter(id, attribute, value)

# DELETE
# Deletando um documento
def delete_client_by_id_service(id):
    result = collection.delete_one({"_id": id})
    return result

