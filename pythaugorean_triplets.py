# This will work when 1 side is given

a = int(input())
if a % 2 == 0:
    b = int(int(a ** 2) // 4) - 1
    c = int(b) + 2
else:
    c = ((a ** 2) + 1) // 2
    b = c - 1
print(int(a), int(b), int(c))
