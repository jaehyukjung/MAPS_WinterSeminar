import itertools

n = int(input())
k = int(input())
num = []
for i in range(n):
    num.append(input())

result = list(map("".join, itertools.permutations(num,k)))

k = set(result)
print(len(k))