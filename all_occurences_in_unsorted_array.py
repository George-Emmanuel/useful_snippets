def get_list_indices(ls):
    res = {}
    for n, i in enumerate(ls):
        try:
            res[i].append(n)
        except KeyError:
            res[i] = [n]
    return [i[1] for i in sorted(res.items(), reverse=True)]


n = int(input())  # give the length of array
arr = list(map(int, input().split()))  # Give the input array
tot = get_list_indices(arr)  # 2d matrix of all occurrences are stored in this list
print(tot)
