import sqlite3
from tkinter import *


def show_menu():
    # Root window
    root = Tk()
    root.title('PyFood Restaurant')
    root.config(bd=20, relief='groove')

    Label(root, text="PyFood Restaurant", fg="darkgreen", font=("Times New Roman", 25, "bold italic")).pack()
    Label(root, text="Menú", fg="green", font=("Times New Roman",24,"bold italic")).pack()

    connection = sqlite3.connect("restaurantDB.db")
    cursor = connection.cursor()

    categories = cursor.execute("SELECT * FROM categories").fetchall()
    for cat in categories:
        Label(root, text=cat[1], fg="black", font=("Times New Roman",20,"bold italic")).pack()
        meals = cursor.execute("SELECT * FROM meals WHERE id_cat={}".format(cat[0])).fetchall()

        for meal in meals:
            Label(root, text=meal[1], fg="gray", font=("Verdana", 15, "italic")).pack()

    connection.close()

    Label(root, text="15.5€", fg="darkgreen", font=("Times New Roman",20,"bold italic")).pack(side="bottom")

    root.mainloop()
