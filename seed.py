import sqlite3
import faker
from random import randint

NUMBER_USERS = 5
NUMBER_TASKS = 8

def generate_fake_data(number_users, number_tasks) -> tuple[list, list]:
    fake_users = []
    fake_tasks = []
    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    for _ in range(number_tasks):
        fake_tasks.append((fake_data.sentence(nb_words=3), fake_data.sentence()))

    return fake_users, fake_tasks

def prepare_data(tasks):

    for_tasks = []

    for task in tasks:
        for_tasks.append((task[0], task[-1], randint(1, 3), randint(1, NUMBER_USERS)))

    return for_tasks

def insert_data_to_db(users, tasks):
    with sqlite3.connect("user_tasks.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")

        sql_to_status = """
        INSERT INTO status (name)
        VALUES (?)"""

        statuses = [('new',), ('in progress',), ('completed',)]

        cur.executemany(sql_to_status, statuses)

        sql_to_users = """
        INSERT INTO users (fullname, email) 
        VALUES (?,?)
        """

        cur.executemany(sql_to_users, users)

        sql_to_tasks = """
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (?,?,?,?)
        """

        cur.executemany(sql_to_tasks, tasks)

        con.commit()

if __name__ =="__main__":
    users, tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    tasks02 = prepare_data(tasks)
    insert_data_to_db(users, tasks02)
