import sqlite3

try:
    conn = sqlite3.connect('list.db')

    cursor = conn.cursor()

    sql_table = """CREATE TABLE if not exists activities(
    activity TEXT NOT NULL,
    status INT NOT NULL
    )"""

    cursor.execute(sql_table)
    conn.commit()

    
except sqlite3.Error as error:
    print(error)