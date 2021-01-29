n = int(input())
a = list(map(int, input().split()))
f, e = 0, 0
for i in range(n):
    e += a[i]
    if e < 0:
        e = 0
    elif f < e:
        f = e
print(f)
