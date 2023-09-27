
coins = [25, 10, 5, 1]

def dfs1(m, p):
    if p == 3 or m == 0:
        return 1
    cnt = 0
    while m >= 0:
        cnt += dfs1(m, p + 1)
        m -= coins[p]
    return cnt


dp = [ [-1] * 4 for i in range(101)]
def dfs2(m, p):
    if dp[m][p] != -1:
        return dp[m][p]
    if p == 3 or m == 0:
        return 1
    ways = 0
    while m >= 0:
        ways += dfs2(m, p+1)
        m -= coins[p]
    dp[m][p] = ways
    return ways


money = 100
print(dfs1(100, 0))
print(dfs2(100, 0))
