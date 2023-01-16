import sys


N = int(sys.stdin.readline())

A, B = map(int,sys.stdin.readline().split())

C = int(sys.stdin.readline())

D = []
for i in range(N):
    D.append(int(sys.stdin.readline()))

D.sort(reverse=True)

result = C
coin = A
cal = C // A

for i in range(N):
    if (result + D[i]) // (coin + B) >= cal:
        result += D[i]
        coin += B
        cal = result // coin
    else:
        break

print(cal)
