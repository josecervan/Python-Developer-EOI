import tkinter as tk
import database.db_definitions as db


def check_signup(label, user, passwd, cpasswd, conn):
    u = user.get()
    p = passwd.get()
    cp = cpasswd.get()

    msg = ''

    if u and p and cp:

        if p == cp:
            user.delete(0, tk.END)
            if db.add_new_user_to_db(u, p, conn):
                print('> Signed up')
                msg = "Nice! Go to the start page and log in to reach your colleagues"
            else:
                msg = 'User above already exists'
        elif p != cp:
            msg = "Passwords above don't match"

        passwd.delete(0, tk.END)
        cpasswd.delete(0, tk.END)

    elif u and not p:
        msg = 'Enter the password'
    elif not u and p:
        msg = 'Enter the user'
    elif not u and not p:
        msg = 'User and password missing'
    elif not cp:
        msg = 'Please, confirm the password'

    label.config(text='')
    label.config(text=msg)


def check_login(label, user, passwd, conn):
    u = user.get()

    if db.is_user_in_db(conn, u):
        p = passwd.get()
        if db.is_passwd_correct(conn, u, p):
            user.delete(0, tk.END)
            passwd.delete(0, tk.END)
            print('> Logged in')
            return True
        else:
            msg = 'Password is not correct'
            passwd.delete(0, tk.END)
    else:
        msg = "User above doesn't exists"

    label.config(text='')
    label.config(text=msg)


def lambda_check_login(controller, label, user, passwd):
    return lambda: controller.show_frame('Timeline') if check_login(label,
                                                                    user,
                                                                    passwd,
                                                                    controller.connection) else None
