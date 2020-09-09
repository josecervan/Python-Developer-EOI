# Question 1
# a = {1, 2, 3}
# b = {4, 5, 6}
#
# print(a.union(b))
# print(b.union(a))


# Question 2
# class Dog:
#     def woof(self):
#         return 'woof!'
#
# t = Dog()
# print(t.woof())


# Question 3
# with open('hello.txt', 'w') as file:
#     file.write('hello!')
#
# print(file.closed)


# Question 4
# class Dog:
#     def __init__(self):
#         pass
#
#     def bark(self):
#         return 'bark bark bark bark bark bark...'
#
# d = Dog()
# print(d.bark())


# Question 5
# @square_it
# @document_it
# def add_ints(a, b):
#     return a + b
#
# add_ints(3, 5)


# Question 6
# packages = ['numpy', 'pandas', 'scipy']
# for i in packages:
#     print(i)


# Question 7
# w = 'python'
# w_iterator = iter(w)
# next(w_iterator)


# Question 8
# def make_dict(**kwargs):
#     return kwargs
#
# print(make_dict(a=1, b=2))


# Question 9
# book = {
#     'title': 'The Giver',
#     'author': 'Lois Lowry',
#     'rating': 4.13,
#     'format': 'paperback'
# }
# 
# book.pop('format')
# 
# print(book)


# Question 10
# def add_many(*args):
#     s = 0
#     for n in args:
#         s += n
#     print(s)
#
# add_many(100, 50, 3)


# Question 11
# import sqlite3
# from sqlite3 import Error
#
# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print('Conexión realizada')
#     except Error as e:
#         print(f'Error {e}')
#     return connection
#
# connection = create_connection('curso.db')


# Question 12
# l = [i * 2 for i in range(5)]
# print(l)


# Question 13
# import tkinter as tk
#
# root = tk.Tk()
# label = tk.Label(root, text='Nombre')
# label.pack(side='left')
# entry = tk.Entry(root)
# entry.pack(side='right')
# root.mainloop()


# Question 14
# suma = lambda x, n=3: x + n
# print(suma(2))


# Question 15
# class Planet:
#     def __init__(self, name):
#         self.name = name
#
# m = Planet('mercury')
# print(m.name)


# Question 16
# any()

