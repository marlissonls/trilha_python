# Importando o módulo PyMongo
import pymongo

# Conectando ao servidor do MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Selecionando o banco de dados
db = client["meu_banco_de_dados"]

# Criando uma coleção
colecao = db["minha_colecao"]

# Inserindo um documento na coleção
documento = {"nome": "João", "idade": 30}
resultado = colecao.insert_one(documento)

# Imprimindo o ID do documento inserido
print(resultado.inserted_id)




# Criando uma lista de documentos
documentos = [
    {"nome": "Maria", "idade": 25},
    {"nome": "José", "idade": 40},
    {"nome": "Ana", "idade": 35}
]

# Inserindo vários documentos na coleção
resultado = colecao.insert_many(documentos)

# Imprimindo os IDs dos documentos inseridos
print(resultado.inserted_ids)