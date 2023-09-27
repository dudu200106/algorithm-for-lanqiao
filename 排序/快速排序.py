

def partition(arr, l, r):
    piv = arr[l]
    f, b = l, r
    while f < b:
        while f < b and arr[b] >= piv:
            b -= 1
        arr[f] = arr[b]
        while f < b and arr[f] <= piv:
            f += 1
        arr[b] = arr[f]
    arr[f] = piv  ## 此时left==b, 两个指针用谁都一样
    return f

def quick_sort(arr, l, r):
    if l >= r:
        return
    mid = partition(arr, l, r)
    quick_sort(arr, l, mid)
    quick_sort(arr, mid+1, r)



arg = [2,4,1,5,3]
quick_sort(arg, 0, 4)
print(arg)