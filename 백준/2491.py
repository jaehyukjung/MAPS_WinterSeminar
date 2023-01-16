N = int(input())

result = list(map(int, input().split()))

num1 = 1
num3 = 1
num2 = [1]
num4 = [1]
for i in range(N-1):
    if result[i] <= result[i+1]:
        num1 += 1
        if num1 > len(num2):
            num2.append(1)
    else:
        num1 = 1

for i in range(N-1):
    if result[i] >= result[i+1]:
        num3 += 1
        if num3 > len(num4):
            num4.append(1)
    else:
        num3 = 1

print(max(len(num2),len(num4)))