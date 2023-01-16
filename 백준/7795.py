T = int(input())


for i in range(T):
    N, M = map(int, input().split())

    cnt = 0

    num1 = list((map(int, input().split())))
    num2 = list((map(int, input().split())))

    num1.sort()
    num2.sort()

    j = 0
    k = 0

    for i in num1:
        while True:
            if i > num2[j]:
                if j == len(num2)-1:
                    cnt += len(num2)
                    break
                else:
                    j += 1
                    continue
            else:
                cnt += j
                break

    print(cnt)

