from tkinter import *
from my_buttons import buttons


if __name__ == '__main__':
    # Ventana raíz
    root = Tk()

    # Título de la ventana
    root.title('Rockola')

    # Ventaba de tamaño fijo
    root.config(bd=15, relief='groove', bg='#999999')
    root.geometry("800x600")
    root.resizable(width=False, height=False)

    # Subtítulo explicativo
    label = Label(root)
    label.config(bg='black', fg='white', font=('Consolas', 18),
                 text='Choose your favourite song:')
    label.pack(side='top')

    buttons()

    root.mainloop()
