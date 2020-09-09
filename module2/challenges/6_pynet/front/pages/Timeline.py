import tkinter as tk


class Timeline(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text='Notifications')
        label1.config(bg='lightgray', relief='groove', fg='black', width=15, height=1, font=('Consolas', 20))
        label1.place(relx=0.25, rely=0.35, anchor=tk.N)

        label2 = tk.Label(self, text='Timeline')
        label2.config(bg='lightgray', relief='groove', fg='black', width=15, height=1, font=('Consolas', 20))
        label2.place(relx=0.75, rely=0.35, anchor=tk.N)

        tk.Button(self, text='Log Out',
                  command=lambda: controller.show_frame('StartPage')).place(relx=0.5, rely=0.8, anchor=tk.N)
