import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('user_tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
sql01 = '''
SELECT id, title, description, status_id
FROM tasks
WHERE user_id = 1;
'''

print(execute_query(sql01))

sql02 = '''
SELECT id, title, description
FROM tasks
WHERE status_id = 1
'''

print(execute_query(sql02))


sql03 = '''
UPDATE tasks
SET status_id = 2
WHERE id = 10
'''

execute_query(sql03)

sql04 = '''
SELECT fullname
FROM users
WHERE NOT IN
'''

print(execute_query(sql04))