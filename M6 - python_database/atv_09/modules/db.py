import psycopg2

db_host = 'localhost'
db_port = '5433'
db_name = 'db_views'
db_user = 'postgres'
db_password = 'postgres'

conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)