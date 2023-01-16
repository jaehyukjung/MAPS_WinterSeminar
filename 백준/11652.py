import sys
N = int(sys.stdin.readline())

result = {}

for i in range(N):
    a = int(input())
    if a not in result:
        result[a] = 1
    else:
        result[a] += 1

result = sorted(result.items(),key=lambda x: (-x[1],x[0]))
print(result[0][0])