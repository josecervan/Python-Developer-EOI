import tkinter as tk

# Variables globales
height = 50


# Definiciones
def add_product(entry):
    global height

    if entry != "" and entry not in lst:
        lst.append(entry)

        tk.Label(text="--> " + entry).place(x=305, y=height)
        height += 20

    products.delete(0, "end")


if __name__ == '__main__':

    # Lista de productos
    lst = list()

    # Ventana raíz
    root = tk.Tk()
    root.title("Lista de la compra")

    # Etiquetas
    label1 = tk.Label(text="Introduzca un producto:")
    label1.place(x=20, y=20)

    label2 = tk.Label(text="Lista de productos")
    label2.place(x=300, y=20)

    # Entrada de productos
    products = tk.Entry(root)
    products.place(x=20, y=75)

    # Botones
    boton = tk.Button(text="Añadir producto", width=15, height=1, bg="white", command=lambda: add_product(products.get()))
    boton.place(x=20, y=100)

    # Ejecución de la ventana
    root.mainloop()
