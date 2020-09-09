import tkinter as tk


# Ventana raíz
root = tk.Tk()
root.config(width=480, height=320, bd=15, relief='groove')
root.title('Sign up')

# Frame 1: nombre y apellidos
fr1 = tk.Frame(root, width=300, height=200)
fr1.pack()
fr1.config(bg='lightgray', bd=10, relief='sunken')

lbl_name = tk.Label(fr1, text='Name')
lbl_name.pack()
entry_name = tk.Entry(fr1)
entry_name.pack()
entry_name.config(justify='center')

lbl_surname = tk.Label(fr1, text='Surname')
lbl_surname.pack()
entry_surname = tk.Entry(fr1)
entry_surname.pack()
entry_surname.config(justify='center')

# Frame 2: usuario y contraseña
fr2 = tk.Frame(root, width=300, height=200)
fr2.pack()
fr2.config(bg='lightgray', bd=10, relief='sunken')

lbl_user = tk.Label(fr2, text='User')
lbl_user.pack()
entry_user = tk.Entry(fr2)
entry_user.pack()
entry_user.config(justify='center')

lbl_password = tk.Label(fr2, text='Password')
lbl_password.pack()
entry_password = tk.Entry(fr2)
entry_password.pack()
entry_password.config(justify='center', show='*')

# Frame 3: botón de registro
fr3 = tk.Frame(root, width=300, height=200)
fr3.pack()
fr3.config(bg='lightgray', bd=10, relief='sunken')

button = tk.Button(fr3,
                   text='Sign up',
                   width=15, height=5,
                   bg='gray', fg='white',
                   activebackground='#FF0000')
button.pack()

root.mainloop()
