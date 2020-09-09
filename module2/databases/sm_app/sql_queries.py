import sm_app_data as data


# Create tables: users, posts, comments, likes
create_users_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        nationality TEXT
)
'''

create_posts_table = '''
    CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
)
'''

create_comments_table = '''
    CREATE TABLE IF NOT EXISTS comments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        post_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(post_id) REFERENCES posts(id)
)
'''

create_likes_table = '''
    CREATE TABLE IF NOT EXISTS likes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        post_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(post_id) REFERENCES posts(id)
)
'''

# Insert records
create_users = '''
    INSERT INTO
        users(name, age, gender, nationality)
    VALUES
        {};
'''.format(data.users)

create_posts = '''
    INSERT INTO
        posts(title, description, user_id)
    VALUES
        {};
'''.format(data.posts)

create_comments = '''
    INSERT INTO
        comments(description, user_id, post_id)
    VALUES
        {};    
'''.format(data.comments)

create_likes = '''
    INSERT INTO
        likes(user_id, post_id)
    VALUES
        {};
'''.format(data.likes)

# Read data in DB
select_users = "SELECT * FROM users"
select_posts = "SELECT * FROM posts"

select_users_posts = '''
    SELECT
        users.id,
        users.name,
        posts.description
    FROM
        posts
        INNER JOIN users ON users.id = posts.user_id
    ORDER BY
        users.id
'''

select_posts_comments_users = '''
    SELECT
        posts.description AS post,
        comments.description AS comment,
        users.name
    FROM
        posts
            INNER JOIN comments ON posts.id = comments.post_id
            INNER JOIN users ON users.id = comments.user_id
    ORDER BY
        users.name
'''

select_posts_likes = '''
    SELECT
        description AS Post,
        COUNT(likes.id) AS Likes
    FROM
        likes,
        posts
    WHERE
        posts.id = likes.post_id
    GROUP BY
        likes.post_id
'''

update_post_description = """
    UPDATE
        posts
    SET
        description = 'The weather has become pleasant now'
    WHERE
        id = 2
"""

