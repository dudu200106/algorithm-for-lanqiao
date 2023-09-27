s = [1, 2, 3, 4]

num = 2 ** 4
for i in range(1, num+1):
    res = []
    for j in range(4):  # 右位移几位
        if (i>>j)&1 == 1:
            res.append(j+1)

    print(res)
print(num)


res = []  
for i in range(1, len(s)+1):
    temp = []
    for j in range(i, len(s)+1):
        temp.append(j)
        print(temp)
        res.insert(0, temp)
print(res)
