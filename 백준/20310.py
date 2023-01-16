S = input()

one = 0
zero = 0
result = list(S)

one = S.count('1')
zero = S.count('0')

one = one // 2
zero = zero // 2

cnt = 0
temp = []
for i in range(len(result)):
    if result[i] == '1':
        temp.append(i)
        cnt += 1
        if cnt == one:
            break

cnt = 0
for i in range(len(result)-1,0,-1):
    if result[i] == '0':
        temp.append(i)
        cnt += 1
        if cnt == zero:
            break
temp.sort(reverse=True)

for i in temp:
    result.pop(i)

print(''.join(result))