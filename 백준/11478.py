S = input()
result = []
i = 0
j = 0

for i in range(len(S)):
    for j in range(len(S)-i):
        result.append(S[j:j+i+1])

a = set(result)

print(len(a))