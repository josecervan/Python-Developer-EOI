import tkinter as tk
import back.definitions as defs


class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # User
        tk.Label(self, text='User',
                 font=('Consolas', 10)).place(relx=0.5, rely=0.35, anchor=tk.N)

        user = tk.Entry(self)
        user.place(relx=0.5, rely=0.39, anchor=tk.N)

        # Password
        tk.Label(self, text='Password',
                 font=('Consolas', 10)).place(relx=0.5, rely=0.43, anchor=tk.N)

        passwd = tk.Entry(self)
        passwd.place(relx=0.5, rely=0.48, anchor=tk.N)
        passwd.config(show='*')

        # Confirm password
        tk.Label(self, text='Confirm password',
                 font=('Consolas', 10)).place(relx=0.5, rely=0.53, anchor=tk.N)

        cpasswd = tk.Entry(self)
        cpasswd.place(relx=0.5, rely=0.58, anchor=tk.N)
        cpasswd.config(show='*')

        label = tk.Label(self)
        label.config(bg='#F0F0F0', width=70, height=1, bd=0, font=('Consolas', 12))
        label.place(relx=0.5, rely=0.63, anchor=tk.N)

        # Sign up button
        tk.Button(self, text='Sign Up',
                  width=15, height=1,
                  font=('Consolas ', 15),
                  bg='#AAAAAA', fg='white',
                  activebackground='#FF0000',
                  command=lambda: defs.check_signup(label,
                                                    user,
                                                    passwd,
                                                    cpasswd,
                                                    controller.connection)).place(relx=0.5, rely=0.68, anchor=tk.N)

        tk.Button(self, text='Go to the start page',
                  command=lambda: (controller.show_frame('StartPage'),
                                   label.config(text=''))).place(relx=0.5, rely=0.8, anchor=tk.N)

