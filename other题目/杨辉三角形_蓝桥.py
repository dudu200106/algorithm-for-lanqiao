import os
import sys

# 请在此输入您的代码
n = int(input())

def solve(n):
  cnt=1
  l1=[1]
  if n==1: return cnt
  for i in range(2,35):
    l2=[]
    for j in range(len(l1)+1):
      if j==0 or j==len(l1):
        l2.append(1)
        cnt += 1
        continue
      num_n = l1[j-1]+l1[j]
      l2.append(num_n)
      cnt+=1
      if num_n== n :
        return cnt
    l1=list(l2)
    # print(l1)

print(solve(n))