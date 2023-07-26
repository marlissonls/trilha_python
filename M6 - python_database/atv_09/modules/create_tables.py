from db import conn

def create_tables():
    
    tables_query = '''
    CREATE TABLE IF NOT EXISTS usuario (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS contato (
        id SERIAL PRIMARY KEY,
        userid INTEGER REFERENCES usuario(id) NOT NULL,
        telefone VARCHAR(255) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS compare_results (
        requisicao VARCHAR(1) NOT NULL,
        um_mil_registros DOUBLE PRECISION NOT NULL,
        dez_mil_registros DOUBLE PRECISION NOT NULL,
        cem_mil_registros DOUBLE PRECISION NOT NULL,
        um_milhao_registros DOUBLE PRECISION NOT NULL
    );
    '''
    cur = conn.cursor()
    cur.execute(tables_query)
    conn.commit()
    cur.close()