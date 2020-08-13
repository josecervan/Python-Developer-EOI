from tkinter import *


# Ventana raíz
root = Tk()

# Título de la ventana
root.title('Rockola')

# Ventaba de tamaño fijo
root.config(bd=15, relief='groove', bg='#999999')
root.geometry("800x600")
# root.resizable(width=False, height=False)

# Subtítulo explicativo
label = Label(root)
label.config(bg='black', fg='white', font=('Consolas', 18),
             text='Choose your favourite song:')
label.pack(side='top')

# Títulos de las canciones
songs = ["Stairway to heaven",
         "Still loving you",
         "Thriller",
         "Roxanne",
         "Heaven's on fire",
         "Start me up",
         "Civil war",
         "Show must go on",
         "Nothing else matters",
         "Unchain my heart"]

buttons = list()
x1 = 206
y1 = 40

x2 = 449
y2 = 40

for i in range(len(songs)):
    buttons.append(Button(root, text=songs[i],
                          command=lambda s=songs[i]: lab.config(text='Playing: ' + s)))
    buttons[i].pack()
    buttons[i].config(width=15, height=5, bg='gray', fg='white', activebackground='#FF0000')

    if i < 5:
        buttons[i].place(x=x1, y=y1)
        y1 += 90
    else:
        buttons[i].place(x=x2, y=y2)
        y2 += 90


lab = Label(root)
lab.pack(side=BOTTOM)

root.mainloop()
