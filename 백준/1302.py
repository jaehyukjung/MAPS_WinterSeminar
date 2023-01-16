N = int(input())

count={}
lists = []
for i in range(N):
    lists.append(input())

lists.sort()
for i in lists:
    try: count[i] += 1
    except: count[i]=1

print(max(count, key=count.get))