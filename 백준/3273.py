n = int(input())

a = list(map(int, input().split()))
x = int(input())

a.sort()
i = 0
j = len(a)-1
cnt = 0
while i<j:
    if a[i] + a[j] == x:
        cnt += 1
        i += 1
        j -= 1
    else:
        if a[i] + a[j] < x:
            i += 1
        else:
            j -= 1

print(cnt)