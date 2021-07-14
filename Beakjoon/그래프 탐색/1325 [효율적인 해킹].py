from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
count = [0] * (n+1)

for _ in range(m) :
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(v):
    q = deque()
    q.append(v)
    visited = [False] * (n + 1)
    visited[v] = True

    while q:
        node = q.popleft()
        for i in graph[node] :
            if visited[i] == True:
                continue
            else :
                q.append(i)
                visited[i] = True

    return visited.count(True)


for v in range(1, n+1):
    count[v] = bfs(v)

for i in range(1, n+1):
    if count[i] == max(count):
        print(i, end=' ')
