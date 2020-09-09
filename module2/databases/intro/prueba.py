import sqlite3

connection = sqlite3.connect('students.db')

cursor = connection.cursor()


cursor.execute('''
       CREATE TABLE IF NOT EXISTS students (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nombre VARCHAR(100),
       nota_media INTEGER,
       email VARCHAR(20)
       )
''')

lst = [('Leonidas', 5, 'leo@ejemplo.com'),
       ('Marcos', 6.5, 'marcos@ejemplo.com'),
       ('Pepe', 7, 'pepe@ejemplo.com')]

cursor.executemany("INSERT INTO students VALUES (NULL,?,?,?)", lst)
# cursor.execute("SELECT * FROM students")
# students = cursor.fetchall()

# for student in students:
#        print(student)

# cursor.execute("INSERT INTO students VALUES ('Leonidas', 5, 'leo@ejemplo.com')")
# cursor.execute("INSERT INTO students VALUES ('Marcos', 6.5, 'marcos@ejemplo.com')")
# cursor.execute("SELECT * FROM students")
# student = cursor.fetchone()

# cursor.execute("UPDATE students SET nombre = 'Roberto', nota_media = 9.9 WHERE dni = '12345678A'")

# cursor.execute("DELETE FROM students WHERE dni = '12345678A'")
# cursor.execute("DELETE FROM students")


connection.commit()
connection.close()