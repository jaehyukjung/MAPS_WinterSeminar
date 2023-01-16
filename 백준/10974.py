import itertools

N = int(input())

num = []

for i in range(1,N+1):
    num.append(i)

a = itertools.permutations(num,N)

k = list(a)

for i in k:
    p = str(i)
    p = p.replace("(","").replace(",","").replace(")","")
    print(p)