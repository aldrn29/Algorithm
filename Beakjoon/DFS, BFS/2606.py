node = int(input())
edge = int(input())
m = [[0 for _ in range(node+1)] for _ in range(node+1)]
visit = [0] * (node+1)
path = []
queue = []

for i in range(edge):
    a, b = map(int, input().split())
    m[a][b] = 1
    m[b][a] = 1

def bfs(n):
    queue.append(n)
    
    # 큐에 원소가 없을때까지 반복
    while len(queue) > 0 :
        n = queue.pop(0)
        visit[n] = 1
        path.append(n)

        # 연결된 노드
        for i in range(1, node+1):
            if visit[i] == 0 and m[n][i] == 1 and queue.count(i) <= 0 :
                queue.append(i)

    return len(path) - 1 # 처음 시작노드 제외

print(bfs(int(1)))