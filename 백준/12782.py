T = int(input())

for i in range(T):
    N, M = input().split()

    N = list(N)
    M = list(M)
    sum = 0
    one = 0
    zero = 0
    new = []

    for i in range(len(N)):
        if N[i] != M[i]:
            new.append(N[i])

    for i in new:
        if i == '1':
            one += 1
        else:
            zero += 1

    k = min(one, zero)
    p = len(new) - k * 2


    print(k+p)