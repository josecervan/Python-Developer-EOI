user_exists_in_users = '''
    SELECT
        name
    FROM
        users
    WHERE
        name = '{}';
'''

create_new_user = '''
    INSERT INTO
        users(name, password)
    VALUES
        ('{}', '{}')
'''

# is_passwd_correct = '''
#     SELECT
#         password
#     FROM
#         users
#     WHERE
#         password = '{}');
# '''

is_passwd_correct = '''
    SELECT EXISTS (
        SELECT * FROM users WHERE name = '{}' AND password = '{}'
)
'''
