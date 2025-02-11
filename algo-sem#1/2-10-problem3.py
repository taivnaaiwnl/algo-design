import math


def solve(n,memo=None):
    if memo is None:
        memo = {}
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    if math.log(n,2) == math.ceil(math.log(n,2)):
        memo[n] = math.ceil(math.log(n,2))
    else:
        memo[n] = n
    return memo[n]
for i in range(10):
    print(solve(i))

