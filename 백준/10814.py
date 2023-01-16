N = int(input())

dic = []
for i in range(N):
    dic.append(input().split())
    dic[i][0] = int(dic[i][0])

dic = sorted(dic, key = lambda x: x[0])
for i in dic:
    print(i[0],i[1])


