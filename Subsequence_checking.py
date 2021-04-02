def check(Str, target):       # This is O(N) time complexity.......remember bruh this is the efficient
    t = 0
    Len = len(Str)
    i = 0
    for i in range(Len):
        if (t == len(target)):
            break
        if (Str[i] == target[t]):
            t += 1
        else:
            t = 0     
    if (t < len(target)):
        return -1
    else:
        return (i - t)
 
a = input()         # First Input
b = input()         # Second input
print(check(a, b))  # will print final ans
