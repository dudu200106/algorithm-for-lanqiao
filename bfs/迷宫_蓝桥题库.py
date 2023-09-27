import os
import sys

# g = list()
# for i in range(10):
#     li = list(input())
#     g.append(li)
g = ['UDDLUULRUL',
     'UURLLLRRRU',
     'RRUURLDLRD',
     'RUDDDDUUUU',
     'URUDLLRRUU',
     'DURLRLDLRL',
     'ULLURLLRDU',
     'RDLULLRDDD',
     'UUDDUDUDLL',
     'ULRDLUURRR']

# # 暴力解法:
# cnt = 0
# for i in range(10):
#     for j in range(10):
#         vis = [[0] * 10 for i in range(10)]
#         tx, ty = i, j
#         while 1:
#             if ty < 0 or tx < 0 or ty >= 10 or tx >= 10:
#                 cnt += 1
#                 break
#             if vis[tx][ty] == 1:  # 陷入循环, 不能走出
#                 break
#             vis[tx][ty] = 1  # 已访问
#
#             if g[tx][ty] == 'U':
#                 tx -= 1
#             elif g[tx][ty] == 'D':
#                 tx += 1
#             elif g[tx][ty] == 'L':
#                 ty -= 1
#             else:
#                 ty += 1
#
# print(cnt)
#

from collections import deque
dir = deque()
yes = [[0] * 10 for i in range(10)] # 记录可到达的点, 这里可以暴力解决, 故不用

cnt2 = 0
for i in range(10):
    for j in range(10):
        vis = [[0] * 10 for i in range(10)]
        tx, ty = i, j
        if yes[tx][ty] == 1:
            cnt2 += 1
            # 再将路径上的点标位可走
            for k in dir:
                x, y = k[0], k[1]
                yes[x][y]=1
            continue
        while 1:
            if ty < 0 or tx < 0 or ty >= 10 or tx >= 10:
                cnt2 += 1
                break
            if vis[tx][ty] == 1:  # 陷入循环, 不能走出
                dir = deque() # 队列清空
                break
            vis[tx][ty] = 1  # 已访问

            if g[tx][ty] == 'U':
                tx -= 1
            elif g[tx][ty] == 'D':
                tx += 1
            elif g[tx][ty] == 'L':
                ty -= 1
            else:
                ty += 1
            dir.append([tx, ty]) # 记录路径

print(cnt2)
