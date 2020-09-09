from front.pages.PyNet import PyNet


import database.db_definitions as db
import database.tables as tables



# Create database or connect if already exists
connection = db.connect_database('database\pynetDB.db')

# Create tables
db.execute_query(connection, tables.create_users_table)
db.execute_query(connection, tables.create_posts_table)
db.execute_query(connection, tables.create_comments_table)
db.execute_query(connection, tables.create_likes_table)

app = PyNet(connection)
app.mainloop()
