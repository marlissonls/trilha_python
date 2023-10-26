from bson import ObjectId

class MongoServices:
    def __init__(self, collection):
        self.collection = collection

    def create_client_service(self, first_name, last_name, email):
        document = {"first_name": first_name, "last_name": last_name, "email": email}
        result = self.collection.insert_one(document)
        return result

    def get_clients_service(self):
        num_docs = self.collection.count_documents({})
        if num_docs == 0:
            raise Exception(f"Não há clients cadastrados neste banco de dados.\n")
        documents = self.collection.find()
        return documents

    def get_clients_by_filter_service(self, attribute, rule):
        num_docs = self.collection.count_documents({attribute: rule})
        if num_docs == 0:
            raise Exception(f"A busca pelo campo `{attribute}` com o valor `{rule}` não encontrou resultados.\n")
        filtered_documents = self.collection.find({attribute: rule})
        return filtered_documents

    def get_client_by_id_service(self, id):
        document = self.collection.find_one({"_id": ObjectId(id)})
        if document is None:
            raise Exception(f"A busca pelo ID `{id}` não encontrou nenhum resultado.\n")
        return document

    def update_client_by_id_service(self, id, first_name, last_name, email):
        result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": {"first_name": first_name, "last_name": last_name, "email": email}})
        return result

    def delete_client_by_id_service(self, id):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result