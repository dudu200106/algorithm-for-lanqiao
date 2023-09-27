import os
import sys
import copy

n = int(input())
g = []
for i in range(n):
    g.append(list(input()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
old_g = copy.deepcopy(g)


def dfs(x, y):  # 是否能存活
    flag = True
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < n and 0 <= ty < n:
            if old_g[tx][ty] == '.':
                flag = False
                break
    f = [False] * 4
    for j in range(4):
        tx, ty = x + dx[j], y + dy[j]
        if tx < 0 or ty < 0 or tx >= n or ty >= n or g[tx][ty] == '.':
            continue
        g[tx][ty] = '.'
        f[j] = dfs(tx, ty)  # 这里得把flag放在后边, 不然可能会发生短路
    return flag or f[0] or f[1] or f[2] or f[3]  # 只要有一个存活, 就返回True


cnt = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == '#':
            g[i][j] = '.'  # dfs时注意, 起点标记为遍历过
            f = dfs(i, j)
            if not f:
                cnt += 1
print(cnt)
