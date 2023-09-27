n, m  = map(int, input().split())

v = [0] * n+1
w = [0] * m+1
dp = [[0] * m+1 for i in range(n+1)]

for i in range(n):
    v[i], w[i] = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, m+1):
        if j > w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j]= dp[i-1][j]

print(dp[n][m])