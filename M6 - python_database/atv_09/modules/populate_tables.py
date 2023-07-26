from db import conn
import random

def populate_tables(population):
    cur = conn.cursor()

    for i in range(population):
        name = f'Name {i+1}'
        email = f'email_{i+1}@example.com'
        telefone1 = ''.join(str(random.randint(0, 9)) for _ in range(10))
        telefone2 = ''.join(str(random.randint(0, 9)) for _ in range(10))

        cur.execute('INSERT INTO usuario (name, email) VALUES (%s, %s) RETURNING id;', (name, email))
        userid = cur.fetchone()[0]
        cur.execute('INSERT INTO contato (userid, telefone) VALUES (%s, %s), (%s, %s);', (userid, telefone1, userid, telefone2))
    
    conn.commit()
    cur.close()