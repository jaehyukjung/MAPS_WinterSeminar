N, M = map(int,input().split())

result = {}
what = []

for i in range(N):
    a,b = input().split()
    result[a] = b

for i in range(M):
    what.append(input())

for i in range(M):
    print(result.get(what[i]))