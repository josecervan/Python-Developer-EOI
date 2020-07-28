t = int(input())

for nth_case in range(t):

    n = int(input())
    h = [int(i) for i in input().split()]
    n_peaks = 0

    for i in range(1, len(h) - 1):
        if h[i] > h[i - 1] and h[i] > h[i + 1]:
            n_peaks += 1

    print("Case #%d: %d" % (nth_case + 1, n_peaks))
