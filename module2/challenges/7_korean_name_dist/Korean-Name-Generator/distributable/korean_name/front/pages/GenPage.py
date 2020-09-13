import tkinter as tk
from korean_name.back.translator import get_birth_date, get_korean_name

class GenPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # User
        tk.Label(self, text='Birth date (dd/mm/yyyy)',
                 font=('Consolas', 10)).place(relx=0.5, rely=0.40, anchor=tk.N)

        date = tk.Entry(self)
        date.place(relx=0.5, rely=0.45, anchor=tk.N)

        label = tk.Label(self)
        label.config(bg='#F0F0F0', width=70, height=2, bd=0, font=('Consolas', 12))
        label.place(relx=0.5, rely=0.55, anchor=tk.N)

        # Translate button
        tk.Button(self, text='Translate your name',
                  width=18, height=1,
                  font=('Consolas ', 15),
                  bg='#AAAAAA', fg='white',
                  activebackground='#FF0000',
                  command=lambda: [label.config(text=''),
                                   get_birth_date(date, label)]).place(relx=0.5, rely=0.65, anchor=tk.N)

        tk.Button(self, text='Go to the start page',
                  command=lambda: [controller.show_frame('StartPage'),
                                   label.config(text=''),
                                   date.delete(0, tk.END)]).place(relx=0.5, rely=0.77, anchor=tk.N)

