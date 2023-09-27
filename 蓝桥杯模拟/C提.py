li = list(input())
o = int(li[1])
l, w = 1189, 841


def paper(order : int):
    global l, w
    while order>0:
        temp = w
        w = l//2
        l = temp
        order -= 1


paper(o)
print(l, w)

