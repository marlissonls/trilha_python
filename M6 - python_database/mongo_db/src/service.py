class MongoServices:
    def __init__(self, configs):
        self.collection = configs.collection

    def create_client_service(self, first_name, last_name, email):
        document = {"fist_name": first_name, "last_name": last_name, "email": email}
        result = self.collection.insert_one(document)
        return result

    def get_clients_service(self):
        documents = self.collection.find()
        return documents

    def get_clients_by_filter_service(self, attribute, rule):
        filtered_documents = self.collection.find({attribute: rule})
        return filtered_documents

    def get_client_by_id_service(self, id):
        document = self.collection.find_one({"_id": id})
        return document

    def update_client_by_id_service(self, id, first_name, last_name, email):
        result = self.collection.update_one({"_id": id}, {"$set": {"fist_name": first_name, "last_name": last_name, "email": email}})
        return result

    def delete_client_by_id_service(self, id):
        result = self.collection.delete_one({"_id": id})
        return result