import sqlite3
import faker
from random import randint, choice

NUMBER_USERS = 5
NUMBER_TASKS = 10

def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []
    fake_tasks = []
    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    for _ in range(number_tasks):
        fake_tasks.append((fake_data.sentence(nb_words=3), fake_data.sentence()))

    return fake_users, fake_tasks

def prepare_data(users, tasks):

    for_tasks = []

    for task in tasks:
        for_tasks.append((list(task), randint(1, 3 + 1), randint(1, )))