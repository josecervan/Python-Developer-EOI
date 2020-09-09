import sqlite3
from sqlite3 import Error


def create_connection(path):
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print('> exception: {}'.format(e.args))
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
        print('> exception: {}'.format(e.args))
    else:
        print('> Successful INSERT query')


def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        column_names = [description[0] for description in cursor.description]
    except Error as e:
        print('> exception: {}'.format(e.args))
    else:
        print('> Successful READ query')
        return column_names, cursor.fetchall()
