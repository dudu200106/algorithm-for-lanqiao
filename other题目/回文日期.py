import os
import sys
import datetime

# 2020 年春节期间，有一个特殊的日期引起了大家的注意：2020 年 2 月 2 日。
# 因为如果将这个日期按 “yyyymmdd” 的格式写成一个 8 位数是 20200202，恰好是一个回文数。我们称这样的日期是回文日期。
# 有人表示 20200202 并不仅仅是一个回文日期，还是一个 ABABBABA 型的回文日期。
# 给定一个 8 位数的日期，请你计算该日期之后下一个回文日期和下一个 ABABBABA 型的回文日期各是哪一天。

date = input()
y = int(date[0:4])  # 将输入的日期转化为年月日的形式
m = int(date[4:6])
d = int(date[6:])
dt = datetime.date(y, m, d)  # 将y,m，d转化为日期格式
flag = True
for i in range(89991232):
    strdt = str(dt).replace('-', '')
    if strdt == strdt[::-1]:
        if flag:
            print(strdt)
            flag = False
        if strdt[0] == strdt[2] == strdt[-1] == strdt[-3] and strdt[1] == strdt[3] == strdt[4] == strdt[-2]:
            print(strdt)
            break
    dt = dt + datetime.timedelta(days=1)
