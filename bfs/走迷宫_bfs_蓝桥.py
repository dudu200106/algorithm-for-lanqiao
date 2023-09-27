import os
import sys

# 给定一个 N×M 的网格迷宫的每个格子要么是道路，要么是障碍物（道路用1表示，障碍物用0表示）。
# 已知迷宫的入口位置为 (x_1,y_1)，出口位置为 (x_2 , y_2)
# 问从入口走到出口，最少要走多少个格子。
# 输入样例:
# 5 5
# 1 0 1 1 0
# 1 1 0 1 1
# 0 1 0 1 1
# 1 1 1 1 1
# 1 0 0 0 1
# 1 1 5 5
# 输出: 8

# 注意事项:
# bfs不用递归!!
# 直接用一个判断队列是否为空的while循环代替

from collections import deque

dx = [-1, 1, 0, 0]  # 控制移动方位
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
vis = [[-1] * m for i in range(n)]  # 是否访问--到起点距离二合一

mp = [list(map(int, input().split())) for i in range(n)]
x1, y1, x2, y2 = map(int, input().split())
q = deque()


def bfs(x, y):
    q.append([x, y])  # 起点入队
    vis[x][y] = 0  # 起点标记被访问过
    while q:
        cur_x, cur_y = q.popleft()  # 出栈, 记录其坐标
        if cur_x == x2 - 1 and cur_y == y2 - 1:
            break
        for i in range(4):  # 移动到相邻点
            tx = cur_x + dx[i]
            ty = cur_y + dy[i]
            # 如果邻居点没越界+没访问过+能走得通
            if (0 <= tx < n and 0 <= ty < m) and vis[tx][ty] == -1 and mp[tx][ty] == 1:
                q.append([tx, ty])
                vis[tx][ty] = vis[cur_x][cur_y] + 1
    return vis[x2 - 1][y2 - 1]  # 正好, 能到达返回距离, 访问不到为-1

print(bfs(x1 - 1, y1 - 1))

