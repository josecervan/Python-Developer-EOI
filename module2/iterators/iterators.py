# class Counter:
#     def __init__(self, size):
#         self.size = size
#         self.start = 0
#
#     def __iter__(self):
#         print('Método __iter__ invocado', self.size)
#         return self
#
#     def __next__(self):
#         if self.start < self.size:
#             self.start += 1
#             return self
#         raise StopIteration
#
#
# CounterIterator = Counter
#
#
# class Counter2:
#     def __init__(self, size):
#         self.size = size
#
#     def __iter__(self):
#         return CounterIterator(self.size)
#
#
# c = Counter2(2)
#
# filas = Counter2(3)
# columnas = Counter2(3)
#
# for x in filas:
#     for y in columnas:
#         print(x.start, y.start)

# class InfiniteCounter:
#     def __init__(self):
#         self.num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.num += 1
#         return self.num
#
# for num in InfiniteCounter():
#     print(num)








