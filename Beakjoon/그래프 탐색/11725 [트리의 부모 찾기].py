import sys
sys.setrecursionlimit(10**6)

node = int(input())
graph = [[] for _ in range(node+1)]
parent = [0] * (node+1)
visited = [False] *(node+1)

for _ in range(node-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(node+1) :
    graph[i].sort()

def dfs(v) :
    visited[v] = True

    for i in graph[v] :
        if not visited[i] :
            parent[i] = v # 부모노드 저장
            dfs(i)

dfs(1)

for i in range(2, node+1) :
    print(parent[i])

'''
while q :
    x = q.popleft()
    # 연결된 노드 순회
    for i in tree[x] :
        if nodes[i] == 0 : # 부모노드 없으면
            nodes[i] = x # 부모노드 넣어주기
            q.append(i) # 그다음 순회할 노드 추가
'''