import sys
import os

n = int(input())
adm = [-1]
for i in map(int, input().split()):
    adm.append(i)
vis = [0] * (n + 1)
m = -1
start = -1


def dfs(ind, cnt):
    global m
    if vis[adm[ind]] == 1:
        if adm[ind] == start:
            m = max(m, cnt)
        return

    vis[ind] = 1
    dfs(adm[ind], cnt + 1)
    vis[ind] = 0


for i in range(1, n + 1):
    start = i
    dfs(i, 1)
print(m)
