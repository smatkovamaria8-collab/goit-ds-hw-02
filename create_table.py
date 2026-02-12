import sqlite3

def create_tabl():
    with open('script.sql', 'r') as file:
        sql = file.read()

    with sqlite3.connect('user_tasks.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ == "__main__":
    create_tabl()