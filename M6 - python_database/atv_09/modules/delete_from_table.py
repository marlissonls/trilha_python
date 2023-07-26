from db import conn

def delete_from_table():
    cur = conn.cursor()
    cur.execute('DELETE FROM user_table;')
    conn.commit()
    cur.close()