a = input()
a = a.upper()

result = {}

for i in a:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1

result1 = []

for key,value in result.items():
    if value == max(result.values()):
        result1.append(key)

if len(result1) > 1:
    print('?')
else:
    print(result1[0])