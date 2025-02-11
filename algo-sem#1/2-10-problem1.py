#N stairs take 1,2,3 steps at each time 
def problem1(n, memo=None):
    if memo is None:
        memo = {}
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    
    memo[n] = problem1(n-1, memo) + problem1(n-2, memo) + problem1(n-3, memo)
    return memo[n]

a = int(input("Stair number: "))
print(problem1(a))

