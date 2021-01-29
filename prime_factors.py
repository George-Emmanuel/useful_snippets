# Note:- Here prime factors are in c but in string type

import math
n = int(input())
x = str(n)
c = []
while n % 2 == 0:
    c.append("2")
    n = n / 2
for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        c.append(str(i))
        n = n / i
if n > 2:
    c.append(str(int(n)))
print(c)
