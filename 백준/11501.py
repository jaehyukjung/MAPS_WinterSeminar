import sys

T = int(sys.stdin.readline())


for i in range(T):
    N = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))
    max = 0

    result = 0
    for i in range(len(a)-1,-1,-1):
        if a[i] < max:
            result += max - a[i]
        else:
            max = a[i]
    print(result)
