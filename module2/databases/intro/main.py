import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None

    try:
        connection = sqlite3.connect(path)
        print('Conexión a la base de datos realizada con éxito')