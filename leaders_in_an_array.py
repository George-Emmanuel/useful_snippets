n = int(input())
arr = list(map(int, input().split()))
c = []
for i in range(0, len(arr)):
    for j in range(i, len(arr)):
        if arr[i] < arr[j]:
            break
        if j == len(arr)-1:
            c.append(arr[i])
print(c)
