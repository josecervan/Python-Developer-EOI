m_app as sma
import sql_queries as sql


# Create connection to DB
conn = sma.create_connection('sm_app.db')

# Create tables
sma.execute_query(conn, sql.create_users_table)
sma.execute_query(conn, sql.create_posts_table)
sma.execute_query(conn, sql.create_comments_table)
sma.execute_query(conn, sql.create_likes_table)

# Add users, posts, comments and likes
sma.execute_query(conn, sql.create_users)
sma.execute_query(conn, sql.create_posts)
sma.execute_query(conn, sql.create_comments)
sma.execute_query(conn, sql.create_likes)

# Read data
columns, users = sma.execute_read_query(conn, sql.select_users)
print(columns)
for user in users:
    print(user)

columns, posts = sma.execute_read_query(conn, sql.select_posts)
print(columns)
for post in posts:
    print(post)

columns, users_posts = sma.execute_read_query(conn, sql.select_users_posts)
print(columns)
for users_post in users_posts:
    print(users_post)

columns, posts_comments_users = sma.execute_read_query(conn, sql.select_posts_comments_users)
print(columns)
for pcu in posts_comments_users:
    print(pcu)

columns, post_likes = sma.execute_read_query(conn, sql.select_posts_likes)
print(columns)
for pl in post_likes:
    print(pl)

# Close connection to DB
conn.close()
