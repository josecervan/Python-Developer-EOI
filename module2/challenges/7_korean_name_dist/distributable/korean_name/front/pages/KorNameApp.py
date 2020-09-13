import os
import tkinter as tk  # python 3

from tkinter import font as tkfont  # python 3

from korean_name.front.pages.StartPage import StartPage
from korean_name.front.pages.GenPage import GenPage


class KorNameApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title('Name Translator')
        self.title_font = tkfont.Font(family='Consolas', size=35, weight='bold', slant='italic')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Window dimensions
        self.geometry('800x600')
        self.resizable(width=False, height=False)

        self.frames = {}
        for F in (StartPage, GenPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('StartPage')

        # Presentation
        tk.Label(self, text=' Name Translator ',

                 font=('Consolas', 35),
                 bg='lightgray', fg='black',
                 relief='groove').place(relx=0.5, rely=0, anchor=tk.N)

        tk.Label(self, text='What is your name in korean?\nDiscover it from your birth date',
                 font=('Consolas', 15),
                 bg='lightgray', fg='black',
                 relief='groove').place(relx=0.5, rely=0.15, anchor=tk.N)

        # PyNet info
        tk.Label(self, text='Korean Name Generator © 2020',
                 font=('Consolas', 10),
                 bg='lightgray', fg='black',
                 relief='groove').place(relx=0.5, rely=0.95, anchor=tk.N)

        # Quit button
        tk.Button(self, text='Quit', command=self.destroy).place(relx=0.5, rely=0.85, anchor=tk.N)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
