T = int(input())
result1 = []
for i in range(T):
    N = int(input())
    word1 = list(input())
    word2 = list(input())
    result = []
    Bsum = 0
    Wsum = 0
    cnt = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            result.append(word1[i])

    for i in result:
        if i == 'B':
            Bsum +=1
        else:
            Wsum +=1

    if Bsum != 0 and Wsum != 0:
        cnt = max(Bsum,Wsum)
    else:
        cnt += Bsum + Wsum

    result1.append(cnt)

for i in result1:
    print(i)