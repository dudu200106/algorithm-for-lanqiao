

def issim(s, cha):
    ss = s + cha
    n = len(ss) // 2
    for i in range(1, n+1):
        if ss[-i:] == ss[-(2*i):-i]:
            return False
    return True

ss=''
def dfs(l, n):
    global ss
    if len(ss) == n:
        return
    for i in range(97, 97+l):
        cha = chr(i)
        if issim(ss, cha):
            ss += cha
            dfs(l, n)
            break


dfs(3, 7)
print(ss)