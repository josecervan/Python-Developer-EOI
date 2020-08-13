from tkinter import *


def convert():
    msg.delete(1.0, 'end')
    if eur.get():
        msg.insert(INSERT, '{} EUR = {} GBP'.format(eur.get(), float(eur.get()) * 0.9))

    elif gbp.get():
        msg.insert(INSERT, '{} GBP = {} EUR'.format(gbp.get(), float(gbp.get()) * 1.11))

    else:
        msg.insert(INSERT, 'Insert any amount (EUR or GBP)')


if __name__ == '__main__':
    # Ventana raíz
    root = Tk()
    root.title('Exchange rate')
    root.config(bd=15, relief='groove', bg='#999999')
    root.geometry("800x600")
    # root.resizable(width=False, height=False)

    # Etiqueta de título
    title = Label(root)
    title.config(text='Exchange rate: EUR <--> GBP', font=('Consolas', 20), bg='#999999')
    title.grid(row=0, column=0, columnspan=2, padx=200, pady=5)

    exchange = Label(root)
    exchange.config(text='1.00 EUR = 0.90 GBP\n1.00 GBP = 1.11 EUR', font=('Consolas', 12), bg='#999999')
    exchange.grid(row=1, column=0, columnspan=2, padx=200, pady=5)

    # EUR
    eur_label = Label(root)
    eur_label.config(text='EUR: ', font=('Consolas', 12), bg='#999999')
    eur_label.grid(row=2, column=0, columnspan=2, padx=100, pady=5, sticky=W)

    eur = Entry(root)
    eur.grid(row=2, column=1, padx=100, pady=5, sticky=W)

    # GBP
    gbp_label = Label(root)
    gbp_label.config(text='GBP: ', font=('Consolas', 12), bg='#999999')
    gbp_label.grid(row=3, column=0, columnspan=2, padx=100, pady=5, sticky=W)

    gbp = Entry(root)
    gbp.grid(row=3, column=1, padx=100, pady=5, sticky=W)

    # Botón de conversión
    btn = Button(root)
    btn.config(text='Convert', command=convert, bg='#CCCCCC')
    btn.grid(row=4, column=0, columnspan=2, padx=200, pady=5)

    # Mensajes
    msg = Text(root)
    msg.config(width=50, height=5, bg='#999999', bd=0, font=('Consolas', 12))
    msg.grid(row=5, column=0, columnspan=2, padx=100, pady=5, sticky=W)
    
    root.mainloop()
