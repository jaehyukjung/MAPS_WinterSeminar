N = int(input())

num = [0]
for i in range(N):
    num.append(int(input()))

num.sort()
sum = 0
for i in range(1,N+1):
    if num[i] != i:
        k = abs(num[i]-i)
        sum += k

print(sum)