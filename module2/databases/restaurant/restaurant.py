import sqlite3


def create_db():
    connection = sqlite3.connect("restaurantDB.db")
    cursor = connection.cursor()

    try:
        cursor.execute('''CREATE TABLE categories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) UNIQUE NOT NULL
                )''')
    except sqlite3.OperationalError as error:
        print('exception: {}'.format(error.args))
    else:
        print("Table 'categories' created")

    try:
        cursor.execute('''CREATE TABLE meals(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) UNIQUE NOT NULL, 
                id_cat INTEGER NOT NULL,
                FOREIGN KEY(id_cat) REFERENCES categoria(id)
                )''')
    except sqlite3.OperationalError as error:
        print('exception: {}'.format(error.args))
    else:
        print("Table 'meals' created")

    connection.commit()
    connection.close()


def add_category():
    category = input("New category\n> ")

    connection = sqlite3.connect("restaurantDB.db")
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO categories VALUES (NULL, '{}')".format(category))
    except sqlite3.IntegrityError as error:
        print('exception: {}'.format(error.args))
    else:
        print("Category '{}' added".format(category))

    connection.commit()
    connection.close()


def add_meal():
    connection = sqlite3.connect("restaurantDB.db")
    cursor = connection.cursor()

    categories = cursor.execute("SELECT * FROM categories").fetchall()
    print("Meal category:")

    for cat in categories:
        print("[{}] {}".format(cat[0], cat[1]))

    cat = int(input("> "))
    new_meal = input("New meal\n> ")

    try:
        cursor.execute("INSERT INTO meals VALUES (NULL, '{}', {})".format(new_meal, cat))
    except sqlite3.IntegrityError as error:
        print(error.args)
    else:
        print("Meal '{}' added".format(new_meal))

    connection.commit()
    connection.close()


def show_menu():
    connection = sqlite3.connect("restaurantDB.db")
    cursor = connection.cursor()

    categories = cursor.execute("SELECT * FROM categories").fetchall()
    for cat in categories:
        print(cat[1])
        meals = cursor.execute("SELECT * FROM meals WHERE id_cat={}".format(cat[0])).fetchall()
        for meal in meals:
            print("\t{}".format(meal[1]))

    connection.commit()
    connection.close()


def get_option():
    option = int(input("\nChoose an option:"
                       "\n[1] Add new category"
                       "\n[2] Add new meal"
                       "\n[3] Show menu"
                       "\n[4] Exit\n\n> "))

    return option


def do_nothing():
    pass
