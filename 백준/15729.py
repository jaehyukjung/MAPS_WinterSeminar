N = int(input())

num = []
for i in range(N):
    num.append(0)

ans = list(map(int, input().split()))

a = -1
cnt = 0

for i,j in zip(num, ans):
    a += 1
    if i != j:
        cnt += 1
        for k in range(3):
            try:
                if num[a+k] == 1:
                    num[a+k] = 0
                else:
                    num[a+k] = 1
            except:
                break


print(cnt)

