N = int(input())

num = [list(map(int, input().split())) for i in range(N)]

num.sort(key = lambda x : (x[0],x[1]))

for i in num:
    print(i[0],i[1])
