# Importa el módulo GUI tkinter
import tkinter as tk

def coste():
	cost = 15

	if (jarron.get()):
		cost = cost + 5
	if (regalo.get()):
		cost = cost + 2
	cost_label.config(text="El coste total es {}€".format(cost))

# Crea ventana raíz para interfaz de usuario
root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

toscana = tk.PhotoImage(file="descarga.jpg")
jarron = tk.IntVar()
regalo = tk.IntVar()


tk.Label(frame,image=toscana).pack()
tk.Label(frame,text="Elige los extras para tu ramo de este mes").pack()



cost_label = tk.Label(root, text="El coste es 15€")
cost_label.pack()

# Llama al método mainloop para mantener la ejecución
root.mainloop()