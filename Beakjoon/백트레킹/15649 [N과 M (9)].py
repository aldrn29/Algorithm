###
# permutations
###

from itertools import permutations

n, m = list(map(int,input().split()))
l = list(map(int, input().split()))

pmt = list(permutations(l, m))
result = sorted(list(set(pmt)))

for i in result :
    for j in range(m) :
        print(i[j], end=' ')
    print()


###
# backtracking - 시간 초과
###

n, m = list(map(int,input().split()))
l = list(map(int, input().split()))
l.sort()
visited = [False] * n
tmp = []
result = []

def dfs() :
    if len(tmp) == m :
        s = ' '.join(map(str, tmp))
        if s not in result :
            result.append(s)
        return

    for i in range(n):
        if not visited[i]:
            tmp.append(l[i])
            visited[i] = True
            dfs()
            tmp.pop()
            visited[i] = False

dfs()
for i in result :
    print(i)
