import heapq

n, m = map(int, input().split())

qq = []
for i in range(n):
    up, red = map(int, input().split())
    qq.append((-up, red))
heapq.heapify(qq)

sum = 0
pu, pr = 0, 0
while qq and m > 0:
    u, r = heapq.heappop(qq)
    u = abs(u)  ## 取出最大值--全是正数, 取反就是大顶堆了
    if u == pu and r < pr:  ## 防止有两个相同大小, 但B不同的
        sum -= pu
        heapq.heappush(qq, (-pu, pr))  ## 把他重新放回去
    sum += u
    u -= r
    if u>0:
        heapq.heappush(qq, (-u, r))
    m -= 1  ## 技能用了一次, 减一

print(sum)

# 3 6
# 10 5
# 9 2
# 8 1