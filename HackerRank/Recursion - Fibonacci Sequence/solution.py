def fibonacci(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


memo = {}

# HackerRank's code
n = int(raw_input())
print(fibonacci(n, memo))