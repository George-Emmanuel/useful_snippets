L = 10 ** 6
a = [0] * L
for i in range(2, L):
    if a[i] == 1:
        continue
    for j in range(i ** 2, L, i):
        a[j] = 1
primes = []
for i in range(2, L):
    if a[i] == 0:
        primes.append(i)
print(primes)
