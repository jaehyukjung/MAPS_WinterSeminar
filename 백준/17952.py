import sys
input = sys.stdin.readline

N = int(input())

result1 = []
result2 = []
last = []
for i in range(N):
    a = list(map(int, input().split()))
    if a[0] == 1:
        result1.append(a[1])
        result2.append(a[2])
        result2[-1] -= 1
        if result2[-1] == 0:
            last.append(result1[-1])
            result1.pop(-1)
            result2.pop(-1)
    else:
        if not result2:
            continue
        else:
            result2[-1] -= 1
            if result2[-1] == 0:
                last.append(result1[-1])
                result1.pop(-1)
                result2.pop(-1)

print(sum(last))