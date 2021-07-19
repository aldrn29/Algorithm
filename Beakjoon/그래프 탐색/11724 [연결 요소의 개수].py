import sys
sys.setrecursionlimit(10**6)

n, e = map(int, sys.stdin.readline().split())
graph = [[] * n for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(e) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v) :
    if visited[v] : return
    visited[v] = True

    for i in graph[v] :
        if not visited[i] :
            dfs(i)

for i in range(1, n+1) :
    if not visited[i] :
        dfs(i)
        count += 1

print(count)