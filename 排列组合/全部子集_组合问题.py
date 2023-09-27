import os
import sys

res = []
num = [1, 2, 3, 4]
# 生成器生成二维数组
nums = [[0 for i in range(3)] for j in range(3)]

# mlist: 一个lieb
# i: 当前列表下表
def combatation(mlist, i):
    for i in range(i, 4):
        mlist.append(num[i])
        print(mlist)
        res.append(mlist[:])
        combatation(mlist, i + 1)
        mlist.pop()

def t():
    print(num)

l = list()
combatation(l, 0)
print(res)
t()
