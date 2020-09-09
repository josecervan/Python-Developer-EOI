import sqlite3
from sqlite3 import Error

import database.queries as qs


def connect_database(path):
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print('> Exception: {}'.format(e.args))
    else:
        print('> Successful connection to database')
        return connection
    return


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print('> Exception: {}'.format(e.args))
    else:
        print('> Successful query')


def is_user_in_db(conn, user):
    cursor = conn.cursor()
    try:
        cursor.execute(qs.user_exists_in_users.format(user))
        conn.commit()
    except Error as e:
        print('> Exception: {}'.format(e.args))
    else:
        print('> User exists')
        return cursor.fetchone()


def is_passwd_correct(conn, user, passwd):
    cursor = conn.cursor()
    try:
        cursor.execute(qs.is_passwd_correct.format(user, passwd))
        conn.commit()
    except Error as e:
        print('> Exception: {}'.format(e.args))
    else:
        return cursor.fetchone()[0]


def add_new_user_to_db(user, passwd, conn):
    if is_user_in_db(conn, user):   # user already exists; do not add user
        return False
    else:   # user does not exist; add new user
        execute_query(conn, qs.create_new_user.format(user, passwd))
        print('> New user created')
        return True