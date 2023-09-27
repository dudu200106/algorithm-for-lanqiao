import sys
import os

# 小明喜欢观景，于是今天他来到了蓝桥公园。
# 已知公园有N个景点，景点和景点之间一共有M条道路。
# 小明有Q个观景计划，每个计划包含一个起点st和一个终点ed,表示他想从st去到ed。
# 但是小明的体力有限,对于每个计划他想走最少的路完成，你可以帮帮他吗?(输出每个计划的最短路径)
# 测试数据:
# 3 3 3
# 1 2 1
# 1 3 5
# 2 3 2
# 1 2
# 1 3
# 2 3


INF = float('inf')

n, m, q = map(int, input().split())
dis = [[INF] * (n + 1) for i in range(n + 1)]
path = [list(range(n + 1)) for i in range(n + 1)]  # 初始化path数组 -- 默认u能直接到v
for i in range(1, n + 1):
    dis[i][i] = 0  # 到达本身

for i in range(m):  # 向邻接矩阵加入权值
    u, v, w = map(int, input().split())
    dis[u][v] = min(dis[u][v], w)

for k in range(1, n + 1):  # 遍历每个顶点, 以每个顶点为中转站, 尝试更新所有入度 和 出度
    for i in range(1, n + 1):  # 入度
        for j in range(1, n + 1):  # 出度
            # dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
            if dis[i][j] > dis[i][k] + dis[k][j]:
                dis[i][j] = dis[i][k] + dis[k][j]
                path[i][j] = k

print(path)
print(dis)
# for i in range(q):
#     u, v = map(int, input().split())
#     print(dis[u][v]) if dis[u][v] != INF else print(-1)

