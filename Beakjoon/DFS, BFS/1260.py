node, edge, start = map(int, input().split())
m = [[0 for _ in range(node+1)] for _ in range(node+1)]
dfs_visit = [0] * (node+1)
bfs_visit = [0] * (node+1)
dfs_path = []
bfs_path = []
queue = []

for i in range(edge):
    a, b = map(int, input().split())
    m[a][b] = 1
    m[b][a] = 1

def dfs(n):
    # 방문한 곳
    dfs_visit[n] = 1
    dfs_path.append(n)

    # 연결된 노드
    for i in range(1, node+1):
        if dfs_visit[i] == 0 and m[n][i] == 1:
            dfs(i) 
    return " ".join(map(str, dfs_path))

def bfs(n):
    queue.append(n)
    
    # 큐에 원소가 없을때까지 반복
    while len(queue) > 0 :
        n = queue.pop(0)
        bfs_visit[n] = 1
        bfs_path.append(n)

        # 연결된 노드
        for i in range(1, node+1):
            if bfs_visit[i] == 0 and m[n][i] == 1 and queue.count(i) <= 0 :
                queue.append(i)

    return " ".join(map(str, bfs_path))


print(dfs(start))
print(bfs(start))