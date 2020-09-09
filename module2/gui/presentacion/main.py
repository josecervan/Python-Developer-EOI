from tkinter import Tk, Label, messagebox


# Ventana raíz
root = Tk()
root.title('Mi primera ventana')

# Texto de presentación
text = Label(root, text='Este es mi primer mensaje estático')
text.pack()
text.config(width=80, height=20, font=('Consolas', 12), padx=10, pady=5)

# Mensaje de advertencia
messagebox.showwarning('Advertencia', 'Esta es mi primera advertencia')

# Estado de ejecución continua
root.mainloop()
