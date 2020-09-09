import tkinter as tk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Sign up button
        tk.Button(self, text='Sign Up',
                  width=15, height=1,
                  font=('Consolas ', 15),
                  bg='#AAAAAA', fg='white',
                  activebackground='#FF0000',
                  command=lambda: controller.show_frame('SignUp')).place(relx=0.5, rely=0.4, anchor=tk.N)

        # Log in buton
        tk.Button(self, text='Log in',
                  width=15, height=1,
                  font=('Consolas ', 15),
                  bg='#AAAAAA', fg='white',
                  activebackground='#FF0000',
                  command=lambda: controller.show_frame('LogIn')).place(relx=0.5, rely=0.5, anchor=tk.N)
