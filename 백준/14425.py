import sys

N, M = map(int, sys.stdin.readline().split())

word = []
test = []
result = []
sum = 0
for i in range(N):
    word.append(input())

for i in range(M):
    test.append(input())

for i in test:
    if i in word:
        sum += 1
print(sum)