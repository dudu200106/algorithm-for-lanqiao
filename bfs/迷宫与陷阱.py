import os
import sys

# 注: 这个题不适合用Python提交, Python会超时, 只能通过一半!!!

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
n, k = map(int, input().split())
g = []
for i in range(n):
  g.append(list(input()))
vis=[[0] * n for i in range(n)]  # 标记是否访问过

from collections import deque
q = deque()


def bfs(x,y):
  q.append([x,y,0,0])  # 创建队列顺便起点入队
  vis[x][y] = 1
  while q:
    cur_x, cur_y, wd, d = q.popleft()
    if cur_x == n-1 and cur_y == n-1:
      print(d)
      return
    for i in range(4):
      tx, ty = cur_x + dx[i], cur_y + dy[i]
      if tx <0 or ty <0 or tx>=n or ty>=n or g[tx][ty] == '#':  # 越界, 是墙壁
        continue
      if g[tx][ty] == '%' and vis[tx][ty] == 0:  # 遇到无敌, 且未曾访问过, wd回满, 该点入栈
        q.append([tx, ty, k, d+1])  # 该点入队
        vis[tx][ty] = 1
      else:
        if wd > 0:  # 无敌值大于0, 这时不论是陷阱是路, 是否访问过, 都能走
          q.append([tx, ty, wd-1, d + 1])  # 该点入队
          vis[tx][ty] = 1
        elif g[tx][ty] == '.' and vis[tx][ty] == 0:
          q.append([tx, ty, 0, d+1])  # 该点入队
          vis[tx][ty] = 1

  print(-1)
bfs(0,0)
