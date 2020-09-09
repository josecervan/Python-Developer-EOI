t = int(input())

for nth_case in range(t):

    n, d = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]

    for xi in x[::-1]:
        d = (d // xi) * xi

    print("Case #%d: %d" % (nth_case + 1, d))
