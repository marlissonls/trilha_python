from config.db_config import connection_config
from config.db_connection import DbConnection
from repository.db_operations import DbOperations
from repository.db_queries import DbQueries
from service.db_service import DbServices
from crud.crud_operations import CrudOperations
from displaydata.displaydata import DisplayData

db_connection = DbConnection(connection_config)
db_operations = DbOperations(db_connection)
db_queries = DbQueries(db_operations)
db_services = DbServices(db_queries, db_operations)
display_data = DisplayData()
crud_operations = CrudOperations(db_services, display_data)

clients_table = {
    "name": "clients",
    "columns": """
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(120) NOT NULL, 
        last_name VARCHAR(120) NOT NULL,
        email VARCHAR(120) NOT NULL UNIQUE
    """,
    "foreigns": [],
}

if __name__ == '__main__':
    try:
        result = db_services.create_table(clients_table)
    except Exception as Error:
        print(Error)
    else:
        print(result)
        crud_operations.operate_crud()