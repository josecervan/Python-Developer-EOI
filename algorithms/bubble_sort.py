import random

A = random.sample(range(100), 15)
print(A)

for i in range(1, len(A)):
    for j in range(len(A) - i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
    print(A)

print('--')
print(A)