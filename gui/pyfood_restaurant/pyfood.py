from tkinter import *


# Variables globales
PAX1 = 0
PAX2 = 0
MAXPAX = 20

SITTING1_MIN = 12
SITTING1_MAX = 14

SITTING2_MIN = 14
SITTING2_MAX = 16


# Comandos
def reservar():
    global PAX1, PAX2

    pax = int(people.get())
    h, m = [int(i) for i in time.get().split(':')]

    if SITTING1_MIN <= h < SITTING1_MAX:
        if PAX1 + pax <= MAXPAX:
            PAX1 += pax
            if m < 10:
                m = '0' + str(m)
            text1.insert(INSERT, 'Reserva realizada\nTurno: 1\nHora: {}:{}\nPersonas: {}'.format(h, m, pax))
        else:
            text1.insert(INSERT, 'ATENCIÓN:\nNo hay espacio suficiente disponible.\nDisculpen las molestias.')
    
    elif SITTING2_MIN <= h < SITTING2_MAX:
        if PAX2 + pax <= MAXPAX:
            PAX2 += pax
            if m < 10:
                m = '0' + str(m)
            text1.insert(INSERT, 'Reserva realizada\nTurno 2\nHora: {}:{}\nPersonas: {}'.format(h, m, pax))
        else:
            text1.insert(INSERT, 'ATENCIÓN:\nNo hay espacio suficiente disponible.\nDisculpen las molestias.')
    else:
        text1.insert(INSERT, 'ATENCIÓN: PyFood está cerrado a la hora indicada')

    actualizar_info()

    btn1['state'] = DISABLED


def limpiar_reserva():
    people.delete(0, 'end')
    time.delete(0, 'end')
    text1.delete(1.0, 'end')

    btn1['state'] = ACTIVE


def actualizar_info():
    text2.delete(1.0, 'end')
    text = 'Plazas disponibles\nTurno 1: {}\nTurno 2: {}'.format(MAXPAX - PAX1, MAXPAX - PAX2)
    text2.insert(INSERT, text)


if __name__ == '__main__':
    root = Tk()
    root.title('Restaurante PyFood')
    root.config(bd=15, relief='groove', bg='#999999')
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    
    # Mensaje de bienvenida
    lab1 = Label(root)
    lab1.config(text='PyFood: portal de reservas', font=('Consolas', 20), bg='#999999')
    lab1.grid(row=0, column=0, columnspan=2, padx=200, pady=5)
    
    # Número de personas
    lab2 = Label(root)
    lab2.config(text='Número de personas:', font=('Consolas', 12), bg='#999999')
    lab2.grid(row=1, column=0, columnspan=2, padx=100, pady=5, sticky=W)
    
    people = Entry(root)
    people.grid(row=1, column=1, padx=100, pady=5, sticky=W)
    
    # Hora de la reserva
    lab3 = Label(root)
    lab3.config(text='Hora (hh:mm):', font=('Consolas', 12), bg='#999999')
    lab3.grid(row=2, column=0, columnspan=2, padx=100, pady=5, sticky=W)
    
    time = Entry(root)
    time.grid(row=2, column=1, padx=100, pady=5, sticky=W)
    
    # Botón 'Reserva'
    btn1 = Button(root)
    btn1.config(text='Reservar', command=reservar, bg='#CCCCCC')
    btn1.grid(row=3, column=0, columnspan=2, padx=200, pady=5)

    # Campo de texto para mensajes informativos
    text1 = Text(root)
    text1.config(width=50, height=5, bg='#999999', bd=0, font=('Consolas', 12))
    text1.grid(row=4, column=0, columnspan=2, padx=100, pady=5, sticky=W)

    # Plazas disponibles en turno
    text2 = Text(root)
    text2.config(width=50, height=5, bg='#999999', bd=0, font=('Consolas', 12))
    text2.grid(row=5, column=0, columnspan=2, padx=100, pady=5, sticky=W)
    actualizar_info()

    # Botón 'Nueva reserva'
    btn2 = Button(root)
    btn2.config(text='Nueva reserva', command=limpiar_reserva, bg='#CCCCCC')
    btn2.grid(row=6, column=0, columnspan=2, padx=200, pady=5)

    root.mainloop()
    
