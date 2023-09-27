import os
import sys

cnt = [0] * 200
word = input()
for ch in word:
    cnt[ord(ch)] += 1

res = ''
m_time = 0
for j in range(200):
    if m_time < cnt[j]:
        m_time = cnt[j]
        res = chr(j)
print(res)
print(m_time)
