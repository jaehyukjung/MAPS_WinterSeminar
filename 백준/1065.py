N = int(input())
a = []

sum = 0
k = 0
for i in range(1,N+1):
    if i <= 99:
        sum += 1
    else:
        j = i
        for p in str(j):
            a.append(p)
        a = list(map(int, a))
        while True:
            if k <= len(a)-3:
                if a[k] - a[k+1] == a[k+1] - a[k+2]:
                        if k + 2 == len(a)-1:
                            sum += 1
                            k = 0
                            a.clear()
                            break
                        else:
                            k += 1
                else:
                    k = 0
                    a.clear()
                    break

print(sum)


