# n=int(input())
# a = list(map(int, input().split()))
#
# #从小到大排序
# sorted_a = sorted(a)
# #从大到小排序
# reversed_a = sorted_a[::-1]
# #输出结果
# # 将列表解开成几个独立的参数，传入函数。类似的运算符还有两个星号(**)，是将字典解开成独立的元素作为形参。
# print(*sorted_a)
# print(*reversed_a)

n = int(input())
li = list(map(int, input().split()))
li.sort()
rev_li = li[::-1]
print(li)
print(rev_li)
