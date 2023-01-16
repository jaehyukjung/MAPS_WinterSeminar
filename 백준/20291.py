import sys
N = int(sys.stdin.readline())

word = []
cnt = []
k = 0
for i in range(N):
    a = sys.stdin.readline().strip()

    for i in range(len(a)):
        if a[i] == '.':
            word.append(a[i+1:])

word.sort()

word1 = list(set(word))
word1.sort()

j = 0
z = 0
for i in range(len(word1)):
    while True:
        if word[z] == word1[j]:
            k += 1
            z += 1
            if z == len(word):
                cnt.append(k)
                break
        else:
            j += 1
            cnt.append(k)
            k = 0
            break

for x,y in zip(word1, cnt):
    print(x,y)


