import copy
arr = [2,4,5,1,3]

def merge(l, m, h):
    help = copy.deepcopy(arr)
    cur = l  # 注意这里不是从0开始
    p1, p2 = l, m+1
    while p1 <= m and p2 <= h:
        if help[p1] <= help[p2]:
            arr[cur] = help[p1]
            p1 += 1
        else:
            arr[cur] = help[p2]
            p2 += 1
        cur += 1
    while p1 <= m:
        arr[cur] = help[p1]
        cur += 1
        p1 += 1

def merge_sort(l, h):
    if l >= h: return
    m = (l+h)//2
    merge_sort(l, m)
    merge_sort(m+1, h)
    merge(l, m, h)

merge_sort(0, len(arr)-1)
print(arr)