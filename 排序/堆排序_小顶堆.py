

def adj_heap(arr, root, leng):
    temp = arr[root]
    i = root * 2 + 1
    while i<leng:
        if i+1<leng and arr[i+1] < arr[i]:  # 为了找出子节点最小值
            i+=1
        if arr[i] >= arr[root]:  # 得到想要的下标i, 退出
            break
        arr[root] = arr[i]
        root = i
        i = root * 2 + 1
    arr[root] = temp



def buildh(arr):
    for i in range(len(arr) >> 2, -1, -1):
        adj_heap(arr, i, len(arr))

def min_heap_sort(arr):
    buildh(arr)
    for i in range(len(arr)-1, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        adj_heap(arr, 0, i)
    return arr


h = [2,3,5,6,1,4]
min_heap_sort(h)
print(h)


