import random

lst1 = random.sample(range(20), 10)
lst2 = random.sample(range(20), 10)

lst = [i for i in lst1 if i in lst2] 

[l.sort() for l in [lst1, lst2, lst]]

print("lista 1: ", lst1)
print("lista 2: ", lst2)
print("lista final: ", lst)
