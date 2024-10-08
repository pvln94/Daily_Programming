def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        dp[i] = min([dp[i - coin] + 1 if i - coin >= 0 else float('inf') for coin in coins])
    return dp[amount] if dp[amount] != float('inf') else -1

coins = list(map(int, input().split()))
amount = int(input())
print(coinChange(coins, amount))
