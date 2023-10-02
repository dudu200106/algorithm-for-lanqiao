
# 蓝桥王国一共有N个建筑和M条单向道路，条道路都连接着两个建筑，每个建筑都有自己编号，分别为1~N。(其中皇宫的编号为1)
# 国王想让小明回答从皇宫到每个建筑的最短路径是多少,但紧张的小明此时已经无法思考，请你编写程序帮助小明回答国王的考核。
# 输入描述:
# 输入第一行包含两个正整数N,M。
# 第2到M+1行每行包含三个正整数u,v,w,表示u→U之间存在一 条距离为W的路。
# 1≤N≤3x10^5，1≤m≤10^6，1<ui,vi≤N，0≤wi≤10^9
# 输出描述:
# 输出仅一行,共N个数,分别表示从皇宫到编号为1 ~ N建筑的最短距离,两两之间用空格隔开。(如果无法到达则输出-1)

# 解题思路:
### 求图 的源点 到其他点的 最短路径(单源最短路径), 推荐用dijkstra
#  * Dijkstra算法采用的是一种贪心的策略, 用来算出起点到各点的最短距离 (额外加上个前驱prev[]也能逆推处到各点的最短路径)
#  * 1.声明.
#  *      声明一个距离数组dis --- 来保存源点到各个顶点的待定最短距离
#  *      声明一个小顶堆hq --- 保存顶点X的待定最短路径dis[X], 每次弹出堆顶顶点, 然后尝试更新与他相连的使用邻居的dis, 更新后重新放入堆中
#  *      声明一个前继数组prev[],记录每个顶点的前继 -- 在一些题目中可能是必要的, 用来输出最短路径
#  *      注: 每个点用数字1~N代表, 一般来说源点为1;
#               hq支持放入元组, 并以元组第一个元素为权重(priority)组成小顶堆
#  * 2. 初始化.
#  *      给源点1的距离dis[1]=0, 并放入小顶堆中--此时堆中只有他
#  *      给其他顶点的距离dis[]赋原始值, 大小为赋为无穷大
#  *
#  * 3. 贪心--弹出小顶堆的堆顶,访问并尝试更新其相邻顶点的dis, 并将其放回小顶堆中. 重复这个动作直至堆空
#  *          a.弹出堆顶元素(贪心), 该顶点的dis最小, 也就是该点最短距离的最优解
#  *          b.访问该顶点可到达其他邻居顶点(参考bfs);
#  *          c.若通过该顶点到达其他邻居顶点的路径长度, 比原来的dis更短, 则更新(dist[i]>dist[t_id]+cost ? dist[i]=dist[t_id]+cost: 不更新);
#  *          d.continue, 重复step.3所有动作，直到小顶堆为空。
import heapq
import sys
import os

INF = float('inf')  # 极大值

N, M = map(int, input().split())
edges = [[] for i in range(N + 1)]
for j in range(M):
    u, v, w = map(int, input().split())
    edges[u].append([v, w])

dis = [INF] * (N+1)
vis = [False] * (N+1)   # 注: 这里加上一个vis数组, 是因为可能两点间不止一条道路
prev = [] * (N+1)  # 放置前驱顶点, 用于求最短路径

hq = [(0, 1)]  # [(dis[u], u)] , 小顶堆, 元组的第一个元素为priority权重
dis[1] = 0

while hq:
    d, u = heapq.heappop(hq)
    if vis[u] == True:
        continue
    vis[u] = True
    for v, w in edges[u]: # 与点u之间有边相连的点集v
        if dis[v] > dis[u] + w:
            dis[v] = dis[u] + w
            prev[v] = u
            heapq.heappush(hq, (dis[v], v))

print(dis)


