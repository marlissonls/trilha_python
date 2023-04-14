from config.db_config import connection_config
from config.db_connection import DbConnection
from repository.db_operations import DbOperations
from repository.db_queries import DbQueries
from service.db_service import DbServices

db_connection = DbConnection(connection_config)
db_operations = DbOperations(db_connection.connect_db())
db_queries = DbQueries(db_operations)
db_services = DbServices(db_operations, db_queries)

table1 = {
"name": "students",
"columns": "id SERIAL PRIMARY KEY, first_name VARCHAR(120) NOT NULL, last_name VARCHAR(120) NOT NULL",
"foreigns": [],
}

table2 = {
    "name": "modules",
    "columns": "id uuid DEFAULT gen_random_uuid() PRIMARY KEY, name VARCHAR(60)",
    "foreigns": [],
}

table3 = {
    "name": "students_modules",
    "columns": "student_id INTEGER NOT NULL, module_id uuid NOT NULL, PRIMARY KEY (student_id , module_id)",
    "foreigns": [
        ", FOREIGN KEY (student_id) REFERENCES students (id) ON UPDATE CASCADE ON DELETE CASCADE"
        ", FOREIGN KEY (module_id) REFERENCES modules (id) ON UPDATE CASCADE ON DELETE CASCADE"
    ],
}

db_services.create_table(table1)
db_services.create_table(table2)
db_services.create_table(table3)

db_operations.commit()

try:
    module1 = db_services.create_module(table2['name'], 'Banco de Dados')
    student1 = db_services.create_student(table1['name'], 'Azedo', 'Leite')
    student_module1 = db_services.join_student_module(table3['name'], student1, module1)
except Exception as Error:
    print(Error)
    db_operations.rollback()
else:
    db_operations.commit()
    print(module1)
    print(student1)
    print(student_module1)

db_connection.disconnect_db()