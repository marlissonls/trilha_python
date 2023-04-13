"""
Main script
"""

from repository.db import Postgres

postgres = Postgres()




create_table(table1)
create_table(table2)
create_table(table3)

postgres.commit()

try:
    module1 = create_module("Banco de Dados")
    student1 = create_student("Luis Gustavo", "Zanetti")

    student_module1 = join_studant_module(student1, module1)

    postgres.commit()
except:
    postgres.rollback()

postgres.commit()
postgres.execute(f'SELECT * from {table3["name"]}')
print(postgres.fetchall())