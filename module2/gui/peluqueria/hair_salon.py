from tkinter import *


tcost = 0

prices = {'Haircut': 10,
          'Comb': 10,
          'Dye': 20,
          'Permanent waving': 30,
          'Hair mask': 25,
          'Anti-hair loss': 35}


def book():
    report.delete(1.0, 'end')
    if not option.get():
        report.insert(INSERT, 'Please, choose a time slot')
        btn1['state'] = DISABLED
        return

    if not any([haircut.get(), comb.get(), dye.get(), pwaving.get(), hmask.get(), ahloss.get()]):
        report.insert(INSERT, 'Please, select any service')
        btn1['state'] = DISABLED
        return

    if option:
        global tcost

        servs = ''

        if haircut.get():
            tcost += prices.get('Haircut')
            servs += 'haircut\n'
        if comb.get():
            tcost += prices.get('Comb')
            servs += 'comb\n'
        if dye.get():
            tcost += prices.get('Dye')
            servs += 'dye\n'
        if pwaving.get():
            tcost += prices.get('Permanent waving')
            servs += 'permanent waving\n'
        if hmask.get():
            tcost += prices.get('Hair mask')
            servs += 'hair mask\n'
        if ahloss.get():
            tcost += prices.get('Anti-hair loss')
            servs += 'anti-hair loss\n'

        btn1['state'] = DISABLED
        report.insert(INSERT, 'Total cost: {}€\n{}'.format(tcost, servs))


def clean_booking():
    global tcost, option, haircut, comb, dye, pwaving, hmask, ahloss
    tcost = 0
    option = IntVar()

    report.delete(1.0, 'end')
    btn1['state'] = ACTIVE


if __name__ == '__main__':
    # Configuración de la ventana raíz
    root = Tk()
    root.title('PySalon hairdressing')
    root.config(bd=15, relief='groove', bg='#999999')
    root.geometry("800x700")
    root.resizable(width=False, height=False)

    # Mensaje de bienvenida
    welcoming = Label(root)
    msg1 = 'PySalon: make a reservation'
    welcoming.config(text=msg1, font=('Consolas', 20), bg='#999999')
    welcoming.grid(row=0, column=0, columnspan=2, padx=200, pady=5)

    # Opciones de tramo horario
    time = Label(root)
    msg2 = 'Choose a time slot'
    time.config(text=msg2, font=('Consolas', 15), bg='#999999')
    time.grid(row=1, column=0, columnspan=2, padx=200, pady=5)

    option = IntVar()

    rbtn1 = Radiobutton(root, text="10:00 - 10:55", variable=option, value=1)
    rbtn1.grid(row=2, column=0, columnspan=2, padx=200)
    rbtn2 = Radiobutton(root, text="11:00 - 11:55", variable=option, value=2)
    rbtn2.grid(row=3, column=0, columnspan=2, padx=200)
    rbtn3 = Radiobutton(root, text="12:00 - 12:55", variable=option, value=3)
    rbtn3.grid(row=4, column=0, columnspan=2, padx=200)

    # Opciones de servicio
    services = Label(root)
    msg3 = 'Choose your options'
    services.config(text=msg3, font=('Consolas', 15), bg='#999999')
    services.grid(row=5, column=0, columnspan=2, padx=200, pady=5)

    haircut = IntVar()
    cbtn1 = Checkbutton(root, text='Haircut ({}€)'.format(prices.get('Haircut')),
                        variable=haircut, onvalue=1, offvalue=0)
    cbtn1.config(width=18, height=1)
    cbtn1.grid(row=6, column=0, columnspan=2, padx=200)

    comb = IntVar()
    cbtn2 = Checkbutton(root, text='Comb ({}€)'.format(prices.get('Comb')), variable=comb, onvalue=1, offvalue=0)
    cbtn2.config(width=18, height=1)
    cbtn2.grid(row=7, column=0, columnspan=2, padx=200)

    dye = IntVar()
    cbtn3 = Checkbutton(root, text='Dye ({}€)'.format(prices.get('Dye')), variable=dye, onvalue=1, offvalue=0)
    cbtn3.config(width=18, height=1)
    cbtn3.grid(row=8, column=0, columnspan=2, padx=200)

    pwaving = IntVar()
    cbtn4 = Checkbutton(root, text='Permanent waving ({}€)'.format(prices.get('Permanent waving')),
                        variable=pwaving, onvalue=1, offvalue=0)
    cbtn4.config(width=18, height=1)
    cbtn4.grid(row=9, column=0, columnspan=2, padx=200)

    hmask = IntVar()
    cbtn5 = Checkbutton(root, text='Hair mask ({}€)'.format(prices.get('Hair mask')),
                        variable=hmask, onvalue=1, offvalue=0)
    cbtn5.config(width=18, height=1)
    cbtn5.grid(row=10, column=0, columnspan=2, padx=200)

    ahloss = IntVar()
    cbtn6 = Checkbutton(root, text='Anti-hair loss ({}€)'.format(prices.get('Anti-hair loss')),
                        variable=ahloss, onvalue=1, offvalue=0)
    cbtn6.config(width=18, height=1)
    cbtn6.grid(row=11, column=0, columnspan=2, padx=200)

    # Botón 'Book'
    btn1 = Button(root)
    btn1.config(text='Make a reservation', command=book, bg='#CCCCCC')
    btn1.grid(row=12, column=0, columnspan=2, padx=200, pady=5)

    # Informe de reserva realizada
    report = Text(root)
    report.config(width=50, height=10, bg='#999999', bd=0, font=('Consolas', 12))
    report.grid(row=13, column=0, columnspan=2, padx=100, pady=5)

    # Botón 'Nueva reserva'
    btn2 = Button(root)
    btn2.config(text='New booking', command=clean_booking, bg='#CCCCCC')
    btn2.grid(row=14, column=0, columnspan=2, padx=200, pady=5)

    root.mainloop()
