limit = 1000000
suml = [0] * limit
a = [True] * limit
a[0] = a[1] = False
for i, isprime in enumerate(a):
    if isprime:
        suml[i] = suml[i-1] + i
        for n in range(i*i, limit, i):
            a[n] = False
    else:
        suml[i] = suml[i-1]
print(suml[int(input())])
# ultimate sum is stored in suml and to print the sum up to n digits use print(suml[int(input())])
