n = int(input())
result = []
for i in range(n):
    a,b = map(int, input().split())
    p = min(a,b)
    q = max(a,b)

    i = 0
    j = 1
    c = 0
    k = 0
    while j * p != c:
        i += 1
        c = i * q
        while j * p <= c:
            if j * p == c:
                result.append(c)
                break
            else:
                j += 1

for i in result:
    print(i)

