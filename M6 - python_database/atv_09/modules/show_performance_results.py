from db import conn

def show_performance_results():
    search = 'SELECT * FROM compare_results;'
    
    cur = conn.cursor()
    cur.execute(search)
    rows = cur.fetchall()
    cur.close()
    return rows