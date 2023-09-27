# 全局变量,存储结果
res=[]
# mlist: 需要全排列的列表
def comb(mlist, n):
    from itertools import combinations
    for i in combinations(mlist, n):
        a=list(i)
        res.append(a)

comb([1, 2, 3, 4], 2)
print(res)