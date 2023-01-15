a = int(input())

for i in range(a):
    N,M = map(int, input().split())

    num = list(map(int, input().split()))

    num[M] = num[M] * 1.0

    cnt = 0

    while True:
        if num[0] == max(num):
            cnt += 1
            if type(num[0]) == float:
                print(cnt)
                break
            else:
                num.pop(0)
        else:
            num.append(num[0])
            num.pop(0)

