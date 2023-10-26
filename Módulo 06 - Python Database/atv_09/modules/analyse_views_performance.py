from modules.db import conn

def analyse_views_performance(option, id):
    value = id

    match option:
        case '1':
            search = '''EXPLAIN ANALYZE SELECT u.name, u.email, STRING_AGG(t.telefone, ", ") AS telefones 
            FROM usuario AS u 
            INNER JOIN telefone AS t ON u.id = t.userid 
            WHERE u.id = %s 
            GROUP BY u.id, u.name, u.email;'''
        case '2':
            search = '''EXPLAIN ANALYZE SELECT * FROM view_dados_usuario
            WHERE id = %s;'''
        case '3':
            search = '''EXPLAIN ANALYZE SELECT * FROM view_materializada_dados_usuario
            WHERE id = %s;'''
    
    cur = conn.cursor()
    cur.execute(search, (value,))
    rows = cur.fetchall()
    cur.close()
    return rows