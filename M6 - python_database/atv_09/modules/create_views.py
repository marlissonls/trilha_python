from db import conn

def create_views():
    views = '''
    CREATE EXTENSION IF NOT EXISTS pg_materializedview;

    CREATE VIEW view_dados_usuario AS
    SELECT u.id, u.name, u.email, STRING_AGG(t.telefone, ', ') AS telefones
    FROM usuario AS u
    INNER JOIN telefone AS t ON u.id = t.userid
    GROUP BY u.id, u.name, u.email;

    CREATE MATERIALIZED VIEW view_materializada_dados_usuario AS
    SELECT * FROM view_dados_usuario;

    REFRESH MATERIALIZED VIEW view_materializada_dados_usuario;'''
    
    cur = conn.cursor()
    cur.execute(views)
    conn.commit()
    cur.close()