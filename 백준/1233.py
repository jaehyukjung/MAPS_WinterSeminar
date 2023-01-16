a,b,c = map(int, input().split())

dic = {}

for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            result = i+j+k
            if result not in dic:
                dic[result] = 1
            else:
                dic[result] += 1

result = sorted(dic.items(),key=lambda x: (-x[1],x[0]))
print(result[0][0])