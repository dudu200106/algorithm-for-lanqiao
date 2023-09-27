import os
import sys

# 来自蓝桥杯题库: <滑行>---
#
# 小蓝准备在一个空旷的场地里面滑行，这个场地的高度不一，小蓝用一个 n 行 m 列的矩阵来表示场地，矩阵中的数值表示场地的高度。
# 如果小蓝在某个位置，而他上、下、左、右中有一个位置的高度（严格）低于当前的高度，小蓝就可以滑过去，滑动距离为 1 。
# 如果小蓝在某个位置，而他上、下、左、右中所有位置的高度都大于等于当前的高度，小蓝的滑行就结束了。
# 小蓝不能滑出矩阵所表示的场地。
#
# 小蓝可以任意选择一个位置开始滑行，请问小蓝最多能滑行多远距离。

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dp = [[-1] * 110 for i in range(110)]  # 滑行距离地图, dp备忘录
g = list()  # 存放输入地图数据


def dfs(x, y):
    if dp[x][y] != -1:  # 已经被记录过, 直接返回
        return dp[x][y]
    res = 0  # 存放能滑过去的, 最大的邻居点值, 用于+1
    for i in range(4):  # 否则就进行四个方向的dfs
        cur_x, cur_y = x + dx[i], y + dy[i]
        if 0 <= cur_x < n and 0 <= cur_y < m and g[x][y] > g[cur_x][cur_y]:  # 下标没越界, 且能滑过
            res = max(res, dfs(cur_x, cur_y))  # 待在原地还是滑向低位?
    dp[x][y] = res + 1  # 加一
    return dp[x][y]


# 输入,存放数据
n, m = map(int, input().split())
for i in range(n):
    li = list(map(int, input().split()))
    g.append(li)

res = 0
for i in range(n):
    for j in range(m):
        res = max(dfs(i, j), res)  # 遍历搜索场地, 顺便得出滑行最大距离
print(res)
