###
#  list
###

node, edge, start = map(int, input().split())
graph = [[] for _ in range(node+1)]
dfs_visited = [False for _ in range(node+1)]
bfs_visited = [False for _ in range(node+1)]
dfs_path = []
bfs_path = []
queue = []

for _ in range(edge) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(edge) :
    graph[i].sort()

def dfs(v) :
    dfs_visited[v] = True
    dfs_path.append(v)

    for i in graph[v] :
        if not dfs_visited[i] :
            dfs(i)
    return " ".join(map(str, dfs_path))

def bfs(v) :
    bfs_visited[v] = True
    queue.append(v)
    bfs_path.append(v)

    while queue :
        x = queue.pop(0)
        for i in graph[x] :
            if not bfs_visited[i] :
                queue.append(i)
                bfs_path.append(i)
                bfs_visited[i] = True
    return " ".join(map(str, bfs_path))

print(dfs(start))
print(bfs(start))
