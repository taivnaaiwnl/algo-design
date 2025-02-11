def exchange_coins(coins, k):
    dp = [float('inf')] * (k+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, k+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[k] if dp[k] != float('inf') else -1

coins = list(map(int, input().split()))
for i in range(12):
    print(exchange_coins(coins, i))

