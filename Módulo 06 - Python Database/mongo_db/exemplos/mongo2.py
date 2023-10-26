import pymongo

# Conectando ao servidor do MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Selecionando o banco de dados
db = client["exemplo_db"]

# Selecionando a coleção
colecao = db["exemplo_colecao"]

# Inserindo um documento na coleção
documento = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}
resultado = colecao.insert_one(documento)
print(resultado.inserted_id)

# Lendo todos os documentos na coleção
documentos = colecao.find()
for documento in documentos:
    print(documento)
