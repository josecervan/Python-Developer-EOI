from tkinter import Button





def buttons():
    b1 = Button(text='Stairway to heaven',
                width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                cursor='arrow',
                command=action)
    b1.pack()
    b1.place(x=206, y=40)

    b2 = Button(text='Still loving you',
                width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                cursor='spraycan')
    b2.pack()
    b2.place(x=206, y=130)

    b3 = Button(text='Thriller',
                width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                cursor='sizing')
    b3.pack()
    b3.place(x=206, y=220)

    b4 = Button(text='Roxanne',
                width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                cursor='target')
    b4.pack()
    b4.place(x=206, y=310)

    b5 = Button(text="Heaven's on fire",
                width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                cursor='star')
    b5.pack()
    b5.place(x=206, y=400)

    b6 = Button(text='Start me up',
                width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                cursor='spider')
    b6.pack()
    b6.place(x=449, y=40)

    b7 = Button(text='Civil war',
                width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                cursor='shuttle')
    b7.pack()
    b7.place(x=449, y=130)

    b8 = Button(text='Show must go on',
                width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                cursor='tcross')
    b8.pack()
    b8.place(x=449, y=220)

    b9 = Button(text='Nothing else matters',
                width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                cursor='clock')
    b9.pack()
    b9.place(x=449, y=310)

    b10 = Button(text='Unchain my heart',
                 width=15, height=5, bg='gray', fg='white', activebackground='#FF0000',
                 cursor='exchange')
    b10.pack()
    b10.place(x=449, y=400)
