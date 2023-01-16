import sys

a = int(sys.stdin.readline())

main = {}
result = []
for i in range(a):
    b,c = sys.stdin.readline().split()
    main[b] = c

for key,value in main.items():
    if value == 'enter':
        result.append(key)


result.sort(reverse=True)

for i in result:
    print(i)