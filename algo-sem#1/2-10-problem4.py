def max_bounty(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    print(dp[0])
    print(dp[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        print(dp[i])
    
    return dp[-1]

nums = list(map(int, input().split()))
print(max_bounty(nums))

