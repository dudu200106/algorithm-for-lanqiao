import datetime

t = datetime.date(2001, 2, 1)
t2 = datetime.date(2001, 3,1)
print(str(t).replace('-', ''))
print(t == t2)
t += datetime.timedelta(5)
print(t)

def ptime(t1: datetime.date) -> bool:
    s1 = str(t1).replace('-', '')
    if s1 == s1[::-1]:
        return True
    return False

print('判断是否是回文日期: ', ptime(datetime.date(2022, 5, 1)))
print('判断是否是回文日期: ', ptime(datetime.date(2021, 12, 2)))


ss = 'abbc'
print(ss.count('b', 0, 2))
print(ss.endswith('c'))
print('.'.join(['a', 'b', 'c']))
print('.'.join(ss))

import copy
ss2= copy.deepcopy(ss)
print(ss, ss2)
ss += '999'
print(ss, ss2)

print('seAN'.upper())
print('seAN'.lower())
print('seAN'.title())
print('seAAN'.index('A'))


