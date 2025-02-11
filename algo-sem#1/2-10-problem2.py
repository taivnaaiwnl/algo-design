#add one 
# multiply two 

def solve(k, memo=None):
    if memo is None:
        memo = {}
    if k == 0:
        return 0
    if k in memo:
        return memo[k]
    if k % 2 == 0:
        memo[k] = 1 + solve(k//2, memo)
    else:
        memo[k] = 1 + solve(k-1, memo)
    return memo[k]
for i in range(10):
    print(solve(i))

