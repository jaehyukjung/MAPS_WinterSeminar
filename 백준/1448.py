import sys

N = int(sys.stdin.readline())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline().strip()))


num.sort(reverse=True)

while True:
    if len(num) == 2:
        print(-1)
        break
    else:
        if num[0] < num[1] + num[2]:
            print(num[0] + num[1] + num[2])
            break
        else:
            num.pop(0)

