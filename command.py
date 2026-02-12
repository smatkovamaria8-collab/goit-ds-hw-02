import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('user_tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
sql01 = '''
SELECT id, title, description, status_id
FROM tasks
WHERE user_id = 5;
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
SELECT u.fullname
FROM users as u
WHERE u.id NOT IN 
(SELECT t.user_id FROM tasks t);
'''

print(execute_query(sql04))

sql05 = '''
INSERT INTO tasks(title, description, status_id, user_id)
VALUES ('Housechore', 'Iron the clothes', 2, 5);
'''

print(execute_query(sql05))

sql06 = '''
SELECT id, title, description, user_id
FROM tasks
WHERE status_id IN (1, 2);
'''

print(execute_query(sql06))

sql07 = '''
DELETE 
FROM tasks
WHERE id = 1;
'''

print(execute_query(sql07))

sql08 = '''
SELECT fullname, email 
FROM users
WHERE email LIKE '%la%';
'''

print(execute_query(sql08))

sql09 = '''
UPDATE users
SET fullname = 'Josh Lurei'
WHERE id = 3;
'''

print(execute_query(sql09))


sql10 = '''
SELECT status_id, COUNT(*)
FROM tasks
GROUP BY status_id;
'''

print(execute_query(sql10))


sql11 = '''
SELECT t.id, t.title, t.description, t.status_id, t.user_id
FROM tasks t
JOIN users as u ON u.id = t.user_id
WHERE u.email LIKE '%@example.com%';
'''
print(execute_query(sql11))

sql12 = '''
SELECT id, title, description, status_id, user_id
FROM tasks
WHERE description IS NULL;
'''
print(execute_query(sql12))

sql13 = '''
SELECT u.fullname, t.title, t.description, t.status_id, t.user_id
FROM tasks t
JOIN users as u ON u.id = t.user_id
WHERE t.status_id = 2;
'''
print(execute_query(sql13))

sql14 = '''
SELECT u.fullname, COUNT(t.id)
FROM users u
LEFT JOIN tasks as t ON u.id = t.user_id
GROUP BY u.fullname;
'''
print(execute_query(sql14))