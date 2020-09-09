import tkinter as tk

def clicked():
    lbl.configure(text="Button was clicked !!")

win = tk.Tk()
win.geometry('800x600')
win.title('My window')

lbl = tk.Label(win, text='Hello', font=('Arial Bold', 12))
lbl.grid(column=0, row=0)

btn = tk.Button(win, text='Click', bg='black', fg='white', command=clicked)
btn.grid(column=1, row=0)

txt = tk.Entry(win, width=10)
txt.grid(column=2, row=0)



win.mainloop()