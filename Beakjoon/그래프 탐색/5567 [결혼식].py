from sys import stdin
from collections import deque

n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(n+1) :
    friends[i].sort()

queue = deque()
visited = [False for _ in range(n+1)]
host = []

def bfs(v) :
    queue.append(v)
    visited[v] = True

    # 친구의 친구까지 검사하기 위한 준비
    host.append(v)
    for i in friends[v] :
        host.append(i)

    while queue :
        nv = queue.popleft()

        for i in friends[nv] :
            if not visited[i] and host.count(nv) > 0 :
                visited[i] = True
                queue.append(i)

bfs(1)
print(visited.count(True) - 1)