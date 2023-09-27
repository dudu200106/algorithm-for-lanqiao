import copy

l = list(input())

vis=[]
flag=True  ## 为了标记是否没有了
while flag:
    flag = False
    i = 0
    while i< (len(l)):
        if i<len(l)-2 and l[i+1] == l[i+2] and l[i] != l[i+1]:
            flag = True
            i+=3
            continue
        if i>2 and l[i-1] == l[i-2] and l[i] != l[i-1]:
            flag = True
            i+=1
            continue
        # print(l[i])
        vis.append(l[i])
        i+=1

    l=copy.deepcopy(vis)
    vis.clear()
print(str(*l))

