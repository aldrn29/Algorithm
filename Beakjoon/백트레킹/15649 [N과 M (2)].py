###
# combinations
###

from itertools import combinations

n, m = map(int, input().split())
result = list(combinations(range(1, n+1), m))

for i in result :
    for j in range(m) :
        print(i[j], end=' ')
    print()


###
# backtracking - 1
###

n, m = map(int, input().split())  
result = []
visitied = [False]*(n+1)

def dfs(depth, start) :
    if depth == m+1 :
        for i in result :
            print(i, end=' ')
        print()
        return
    for i in range(start+1, n+1) :
        if not visitied[i] :
            visitied[i] = True
            result.append(i)
            dfs(depth+1, i)
            visitied[i] = False
            result.pop()
dfs(1, 0)


###
# backtracking - 2
###

n, m = list(map(int,input().split()))
result = []

def dfs(start) :
    if len(result) == m :
        print(' '.join(map(str,result)))
        return
    
    for i in range(start, n+1) : 
        if i not in result :
            result.append(i)
            dfs(i+1) 
            result.pop()
dfs(1)