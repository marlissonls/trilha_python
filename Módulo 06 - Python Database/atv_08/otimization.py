import psycopg2

db_host = 'localhost'
db_port = '5433'
db_name = 'db_otimization'
db_user = 'postgres'
db_password = 'postgres'

conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)

def create_tables():
    sql_create_tables = '''
    CREATE TABLE user_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
    );

    CREATE INDEX name_index ON user_table (name);

    CREATE TABLE compare_results (
    requisicao VARCHAR(1),
    um_mil_registros DOUBLE PRECISION,
    dez_mil_registros DOUBLE PRECISION,
    cem_mil_registros DOUBLE PRECISION,
    um_milhao_registros DOUBLE PRECISION
    );
    '''
    cur = conn.cursor()
    cur.execute(sql_create_tables)
    conn.commit()
    cur.close()

def populate_table(population):
    cur = conn.cursor()

    for i in range(population):
        name = f'Name {i+1}'
        email = f'email{i+1}@example.com'
        cur.execute("INSERT INTO user_table (name, email) VALUES (%s, %s)", (name, email))
    
    conn.commit()
    cur.close()

def delete_from_table():
    cur = conn.cursor()
    cur.execute('DELETE FROM user_table;')
    conn.commit()
    cur.close()

def select_from_user_table(option):
    search = 'EXPLAIN ANALYZE SELECT * FROM user_table WHERE '
    match option:
        case '1':
            search += 'name LIKE %s;'
            value = 'Name 500%'
        case '2':
            search += 'name = %s;'
            value = 'Name 500'
        case '3':
            search += 'email = %s;'
            value = 'email500@example.com'

    cur = conn.cursor()
    cur.execute(search, (value,))
    rows = cur.fetchall()
    cur.close()
    return rows

def insert_result(req, mil, dezmil, cemmil, milhao):
    sql_insert = 'INSERT INTO compare_results (requisicao, um_mil_registros, dez_mil_registros, cem_mil_registros, um_milhao_registros) VALUES (%s, %s, %s, %s, %s)'
    values = (req, mil, dezmil, cemmil, milhao)

    cur = conn.cursor()
    cur.execute(sql_insert, values)
    conn.commit()
    cur.close()

def select_from_results():
    search = 'SELECT * FROM compare_results'
    
    cur = conn.cursor()
    cur.execute(search)
    rows = cur.fetchall()
    cur.close()
    return rows

while True:
    print("\n")
    print("1 - Criar tabelas.")
    print("2 - Popular as tabelas com os dados.")
    print("3 - Limpar dados da tabela users_table.")
    print("4 - Realizar uma busca na tabela users_table.")
    print("5 - Inserir resultado da busca na tabela compare_results.")
    print("6 - Monstrar tabela compare_results.")
    print('7 - Encerrar operações')

    option = input("\nSelecione o número de uma das operações: ")
    print('\n')
    match option:
        case '1':
            create_tables()
        case '2':
            population = int(input('Digite o número da quantidade de dados: '))
            populate_table(population)
        case '3':
            delete_from_table()
        case '4':
            print('1 - Fazer a busca: name LIKE "Name 500%"')
            print('2 - Fazer a busca: name = "Name 500"')
            print('3 - Fazer a busca: email = "email500@example.com"')
            option = input('Digite a opção: ')
            if option in ['1', '2', '3']:
                result = select_from_user_table(option)
                print(result)
            else: print('Opção inválida.')
        case '5':
            req = input('Informe a requisição: ')
            mil = input(f'Informe o tempo da requsicao "{req}" com população de 1 mil registros: ')
            dezmil = input(f'Informe o tempo da requsicao "{req}" com população de 10 mil registros: ')
            cemmil = input(f'Informe o tempo da requsicao "{req}" com população de 100 mil registros: ')
            milhao = input(f'Informe o tempo da requsicao "{req}" com população de 1 milhão registros: ')
            insert_result(req, mil, dezmil, cemmil, milhao)
        case '6':
            result = select_from_results()
            print(result)
        case '7':
            print("Operações encerradas!")
            conn.close()
            break
        case _:
            print("Opção inválida!")