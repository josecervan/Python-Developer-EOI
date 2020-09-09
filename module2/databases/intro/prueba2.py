import sqlite3

connection = sqlite3.connect('students.db')

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (nombre VARCHAR(100), nota_media INTEGER, email VARCHAR(20))")

cursor.execute("INSERT INTO students VALUES ('Pilar', 8, 'pilar@ejemplo.com')")

connection.close()