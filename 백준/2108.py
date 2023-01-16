import sys

N = int(sys.stdin.readline())

num = []
result = []
dic = {}

for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()
for i in num:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

a = max(dic.values())

k = []

for i in dic:
    if a == dic[i]:
        k.append(i)

print(round(sum(num)/len(num)))
print(num[len(num)//2])
if len(k) == 1:
    print(k[0])
else:
    print(k[1])
print(max(num) - min(num))
