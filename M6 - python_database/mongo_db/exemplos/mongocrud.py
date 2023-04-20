from pymongo import MongoClient
from os import getenv
import dotenv

dotenv.load_dotenv()

# Conectando ao servidor do MongoDB

connection = f"mongodb://{getenv('DBUSER')}:{getenv('DBPASSWORD')}@{getenv('DBHOST')}:{getenv('DBPORT')}/{getenv('DBDATABASE')}?authSource=admin"

client = MongoClient(connection)

# Selecionando o banco de dados
db = client[getenv('DBDATABASE')]

# Selecionando a coleção
colecao = db["clients"]

# CREATE
# Inserindo um documento na coleção
documento1 = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}
resultado1 = colecao.insert_one(documento1)
print(dir(resultado1))
print(resultado1.acknowledged)
print(resultado1.inserted_id)
print(dir(resultado1._raise_if_unacknowledged))

""" documento2 = {"nome": "João", "idade": 35, "cidade": "Rio de Janeiro"}
resultado2 = colecao.insert_one(documento2)
print(resultado2.inserted_id)

# READ
# Lendo todos os documentos na coleção
documentos = colecao.find()
for documento in documentos:
    print(documento)

# Lendo um documento específico por ID
documento = colecao.find_one({"_id": resultado1.inserted_id})
print(documento)

# Lendo documentos com filtro
documentos_filtrados = colecao.find({"idade": {"$gt": 30}})
for documento in documentos_filtrados:
    print(documento)

# UPDATE
# Atualizando um documento
filtro = {"_id": resultado1.inserted_id}
novo_valor = {"$set": {"idade": 26}}
colecao.update_one(filtro, novo_valor)

# Lendo o documento atualizado
documento_atualizado = colecao.find_one({"_id": resultado1.inserted_id})
print(documento_atualizado)

# DELETE
# Deletando um documento
filtro = {"_id": resultado1.inserted_id}
colecao.delete_one(filtro)

# Lendo a coleção após a exclusão
documentos = colecao.find()
for documento in documentos:
    print(documento) """
