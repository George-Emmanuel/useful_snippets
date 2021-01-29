string = input()  # Give your input here
length = len(string)
c = []
for i in range(length):
    for j in range(i, length):
        c.append(string[i:j + 1])
print(c)
