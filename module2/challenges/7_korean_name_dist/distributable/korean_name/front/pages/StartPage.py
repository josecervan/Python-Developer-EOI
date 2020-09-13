import tkinter as tk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Sign up button
        tk.Button(self, text='Start',
                  width=15, height=1,
                  font=('Consolas ', 15),
                  bg='#AAAAAA', fg='white',
                  activebackground='#FF0000',
                  command=lambda: controller.show_frame('GenPage')).place(relx=0.5, rely=0.4, anchor=tk.N)
