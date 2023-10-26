from modules.db import conn

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

    CREATE EXTENSION IF NOT EXISTS pg_materializedview;

    CREATE VIEW view_dados_usuario AS
    SELECT u.id, u.name, u.email, STRING_AGG(t.telefone, ', ') AS telefones
    FROM usuario AS u
    INNER JOIN telefone AS t ON u.id = t.userid
    GROUP BY u.id, u.name, u.email;

    CREATE MATERIALIZED VIEW view_materializada_dados_usuario AS
    SELECT * FROM view_dados_usuario;
    '''
    cur = conn.cursor()
    cur.execute(tables_query)
    conn.commit()
    cur.close()

    print('''
        Tabelas criadas: usuario e contato.
        Views criadas: view_dados_usuario e view_materializada_dados_usuario.
    ''')