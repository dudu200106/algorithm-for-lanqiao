n, m, b = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
g = [[0] * (m + 1) for i in range(n + 1)]
for i in range(b):
    x, y = map(int, input().split())
    g[x][y] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
vis = [[False] * (m + 1) for i in range(n + 1)]
vis[1][1] = True


def dfs(x, y):
    if x == x2 and y == y2:
        return 1
    res = 0
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if tx < 1 or ty < 1 or tx > n or ty > m:
            continue
        if g[tx][ty] == 1 or vis[tx][ty]:  # 障碍, 或者被访问过
            continue
        vis[tx][ty] = True
        res += dfs(tx, ty)
        vis[tx][ty] = False
    return res


print(dfs(1, 1))
