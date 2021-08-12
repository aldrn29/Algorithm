n, m = list(map(int,input().split()))
l = list(map(int, input().split()))
l.sort()
result = []

def dfs() :
    if len(result) == m :
        print(' '.join(map(str, result)))
        return

    for i in l :
        if i not in result :
            result.append(i)
            dfs()
            result.pop()
dfs()