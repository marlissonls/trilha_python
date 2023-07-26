from db import conn

def insert_performance_results(req, mil, dezmil, cemmil, milhao):
    sql_insert = '''INSERT INTO compare_results (requisicao, um_mil_registros, dez_mil_registros, cem_mil_registros, um_milhao_registros) 
    VALUES (%s, %s, %s, %s, %s);'''
    values = (req, mil, dezmil, cemmil, milhao)

    cur = conn.cursor()
    cur.execute(sql_insert, values)
    conn.commit()
    cur.close()