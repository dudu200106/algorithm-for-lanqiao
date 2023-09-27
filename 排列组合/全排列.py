# 全局变量,存储结果
import itertools

res=[]
# mlist: 需要全排列的列表
def perm(mlist, n):
    from itertools import permutations
    for i in permutations(mlist, n):
        a=list(i)
        res.append(a)

perm([1, 2, 3, 4], 2)
print(res)