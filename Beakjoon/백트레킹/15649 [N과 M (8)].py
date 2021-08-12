n, m = list(map(int,input().split()))
l = list(map(int, input().split()))
l.sort()
result = []

def dfs(start) :
    if len(result) == m :
        print(' '.join(map(str, result)))
        return

    for i in range(start, n) :
        result.append(l[i]) 
        dfs(i)
        result.pop()
dfs(0)