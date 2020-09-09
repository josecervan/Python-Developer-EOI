from tkinter import *


# Ventana raíz
root = Tk()

# Tamaño de la ventana, color de fondo y estilo de borde
root.config(width=480, height=320, bg='lightgray', bd=10, relief='groove')
root.geometry("480x320")

# Título de la ventana
root.title('Test auditivo')

# Etiqueta
Label(root, bg='darkgray', fg='white',
      text="Pulse todos los botones que correspondan a cada sonido").pack(side='top')

# Botones
b1 = Button(root, text="Agudo", width=12, height=5, bg="blue", fg="white", activebackground="#00FF00")
b1.pack()
b1.place(x=180, y=40)

b2 = Button(root, text="Grave", width=12, height=5, bg="orange", fg="white", activebackground="#00FF00")
b2.pack()
b2.place(x=180, y=200)

b3 = Button(root, text="Izquierdo", width=12, height=8, bg="black", fg="white", activebackground="#00FF00")
b3.pack()
b3.place(x=60, y=100)

b4 = Button(root, text="Derecho", width=12, height=8, bg="white", fg="black", activebackground="#00FF00")
b4.pack()
b4.place(x=300, y=100)

# Ejecución de la ventana
root.mainloop()
