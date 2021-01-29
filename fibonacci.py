n = int(input())      # Give your input here which is your first n terms
f = [0, 1]
for i in range(2, n + 1):
    f.append(f[i - 1] + f[i - 2])
print(f)       # Your Fibonacci series is stored in f array
