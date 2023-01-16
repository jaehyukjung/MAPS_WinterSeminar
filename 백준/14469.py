N = int(input())

c = 0

number = []

for i in range(N):
    k = list(map(int, input().split()))
    number.append(k)

number.sort()

for i in range(N):
    if i == 0:
        c = sum(number[0])
    else:
        p = number[i]
        q = p[0]
        j = p[1]
        if q > c:
            c = sum(number[i])
        else:
            c += j
print(c)


