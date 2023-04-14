from config.db_config import connection_config
from config.db_connection import DbConnection
from repository.db_operations import DbOperations
from repository.db_queries import DbQueries
from service.db_service import DbServices

db_connection = DbConnection(connection_config)
db_operations = DbOperations(db_connection.connect_db())
db_queries = DbQueries(db_operations)
db_services = DbServices(db_operations, db_queries)

registration_table = {
"name": "register",
"columns": """
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(120) NOT NULL, 
    last_name VARCHAR(120) NOT NULL,
    email VARCHAR(120) NOT NULL
""",
"foreigns": [],
}

if __name__ == '__main__':
    try:
        result:str = db_services.create_table(registration_table)
    except Exception as Error:
        print(Error)
        db_operations.rollback()
    else:
        print(result)
        db_operations.commit()

db_connection.disconnect_db()