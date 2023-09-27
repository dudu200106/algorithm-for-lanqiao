n, m = int(input()), int(input())
res = [[] for i in range(50)]  ## 桶排序

def sovle(num):
    sum=0
    while num > 0:
        sum += num%10
        num //= 10
    return sum

for i in range(1, n+1):
    seq = sovle(i)
    res[seq].append(i)

for j in range(1, 50):
    if m <= len(res[j]):
        print(res[j][m-1])
        break
    m -= len(res[j])
