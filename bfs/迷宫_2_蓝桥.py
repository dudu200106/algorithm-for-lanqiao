import os
import sys

dx=[1, 0, 0, -1]  # 按照"下左右上"的顺序入队
dy=[0, -1, 1, 0]
act = ['D', 'L', 'R','U']
g = []
for i in range(30):
  li = map(int, list(input()) )
  g.append(list(li))
vis = [[0] * 50 for i in range(30)]  # 标记是否访问过

from collections import deque
q = deque()
parents = {}  # 记录当前点的父亲--上一个节点
q.append([0,0,0])
parents[(0, 0)]=[-1, -1, '']  # 记录每一步的前驱(父亲)节点, 包含[x,y,'action']
vis[0][0] = 1


def print_route():
  res=''
  pa_x, pa_y, act = parents[(29, 49)]
  while pa_x != -1:
      res = act + res  # 拼接
      pa_x, pa_y, act = parents[(pa_x, pa_y)]
  print(res)


def solve1():  # 从终点反向找
    while q:
        cur_x, cur_y, d = q.popleft()
        if cur_x == 30 - 1 and cur_y == 50 - 1:
            print_route()  # 根据终点打印移动路径
            break
        for i in range(4):
            tx, ty = cur_x + dx[i], cur_y + dy[i]
            if 0<=tx<30 and  0<=ty<50 and vis[tx][ty]==0 and g[tx][ty] ==0:  # 不越界 没访问过 且可以走
                q.append([tx,ty, d+1])
                vis[tx][ty] = 1
                parents[(tx, ty)] = [cur_x, cur_y, act[i]]

# # 错误方法!! 因为不确定是否是最短的路径, 是否能到达终点
# res = ''
# def solve2():  # 从终点反向找
#     global res
#     while q:
#         cur_x, cur_y, d = q.popleft()
#         if cur_x == 30 - 1 and cur_y == 50 - 1:
#             print(res)
#             return
#         for i in range(4):
#             tx, ty = cur_x + dx[i], cur_y + dy[i]
#             if 0<=tx<30 and  0<=ty<50 and vis[tx][ty]==0 and g[tx][ty] ==0:  # 不越界 没访问过 且可以走
#                 q.append([tx,ty, d+1])
#                 vis[tx][ty] = 1
#                 if d + 1 == len(res) + 1:
#                     res = res + act[i]

solve1()