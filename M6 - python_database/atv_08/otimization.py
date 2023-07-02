import pandas as pd
from sqlalchemy import create_engine

db_host = 'localhost'
db_port = '5433'
db_name = 'db_otimization'
db_user = 'postgres'
db_password = 'postgres'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

sql_create_tables = '''
CREATE TABLE user_table (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);

CREATE INDEX name_index ON user_table (name);

CREATE TABLE comparacao_resultados (
  requisicao VARCHAR(1),
  quantidade_dados VARCHAR(10),
  tempo_execucao DOUBLE PRECISION
);
'''

with engine.connect() as connection:
    connection.execute(sql_create_tables)

def populate_table(population):
    sql_insert = f'INSERT INTO user_table (name, email) VALUES '

    for i in range (population):
        sql_insert += f'''('Name {i+1}', 'email{i+1}@example.com'), '''

    sql_insert = sql_insert[:-2] +';'

    with engine.connect() as connection:
        connection.execute(sql_create_tables)

def delete_from_table():
    with engine.connect() as connection:
        connection.execute('DELETE FROM user_table;')

def select_from_table():
    search1 = '''EXPLAIN ANALYZE SELECT * FROM user_table WHERE name LIKE 'Name 500%';'''

    search2 = '''EXPLAIN ANALYZE SELECT * FROM user_table WHERE name = 'Name 500';'''

    search3 = '''EXPLAIN ANALYZE SELECT * FROM user_table WHERE email = 'email500@example.com';'''

    with engine.connect() as connection:
        connection.execute(search1)