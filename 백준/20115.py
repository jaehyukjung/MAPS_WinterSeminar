k = int(input())

N = list(map(int, input().split()))
result = []

N.sort(reverse = True)

a = N[0]

N.pop(0)

for i in N:
    i = i / 2
    result.append(i)

print(a + sum(result))