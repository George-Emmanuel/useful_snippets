from math import gcd
a = int(input())
arr = list(map(int, input().split()))
res = gcd(arr[0], arr[1])
for i in range(2, len(arr)):
    res = gcd(res, arr[i])
print(res)
