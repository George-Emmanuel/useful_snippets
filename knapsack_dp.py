def knapsack(Capacity, weights, profits, n):
    if n == 0 or Capacity == 0:
        return 0
    if weights[n - 1] > Capacity:
        return knapsack(Capacity, weights, profits, n - 1)
    else:
        return max(profits[n - 1] + knapsack(Capacity - weights[n - 1], weights, profits, n - 1),
                   knapsack(Capacity, weights, profits, n - 1))


n, Capacity = map(int, input().split())
profits = list(map(int, input().split()))
weights = list(map(int, input().split()))
print(knapsack(Capacity, weights, profits, n))
