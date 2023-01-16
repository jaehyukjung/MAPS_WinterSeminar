N = int(input())

word = list(input())
word1 = []
word2 = []
sumB = 0
sumR = 0
k = ''
for i in word:
    if i == 'B':
        sumB += 1
    else:
        sumR += 1

for i in range(len(word)):
    if word[i] == 'B':
        word1.append(i)
    else:
        word1.append('R')

for i in range(len(word)):
    if word[i] == 'R':
        word2.append(i)
    else:
        word2.append('B')

result = 0
result1 = 0
for i in range(len(word1)-1):
    if word1[i] == word1[i+1]:
        result += 1

for i in range(len(word2)-1):
    if word2[i] == word2[i+1]:
        result1 += 1

q = sumR-result+1
p = sumB-result1+1
print(min(p,q))