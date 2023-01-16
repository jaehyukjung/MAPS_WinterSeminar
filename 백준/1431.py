import re
N = int(input())

word = []

for i in range(N):
    word.append(input())

def alpha(n):
    a = map(int, re.findall('\d', n))
    k = sum(a)
    return k


word.sort(key = lambda x: (len(x),alpha(x),x))
for i in range(N):
    print(word[i])



