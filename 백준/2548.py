import math

N = int(input())

num = list(map(int, input().split()))

num.sort()

a = len(num)/2

k = int(math.ceil(a))

print(num[k-1])