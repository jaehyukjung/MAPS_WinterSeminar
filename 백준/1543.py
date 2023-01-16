a = list(input())
b = list(input())
sum = 0
i = 0
while i <= len(a)-len(b)+1:
    if a[i:i+len(b)] == b:
        i = i + len(b)
        sum += 1
    else:
        i += 1

print(sum)
