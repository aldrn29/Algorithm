###
# permutations
###

from itertools import permutations

n, m = map(int, input().split())
result = list(permutations(range(1, n+1), m))

for i in result :
    for j in range(m) :
        print(i[j], end=' ')
    print()


###
# backtracking
###

n, m = map(int, input().split())  # m = depth 4 2
result = []
visitied = [False]*(n+1)

def dfs(depth) :
    if depth == m+1 :
        for i in result :
            print(i, end=' ')
        print()
        return
    for i in range(1, n+1) :
        if not visitied[i] :
            visitied[i] = True
            result.append(i)
            dfs(depth+1)
            visitied[i] = False
            result.pop()

dfs(1)