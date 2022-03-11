from collections import deque
from sys import stdin

n, m = list(map(int, stdin.readline().split()))
graph = []

for i in range(n) :
    graph.append(list(map(int, stdin.readline().strip())))

print(graph)

def bfs(x, y) :
    que = deque()
    que.append((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while que :
        x, y = que.popleft()

        if x == n-1 and y == m-1 :
            return(graph[n-1][m-1])

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx, ny))

result = bfs(0, 0)
print(result)

# 입력 예시
'''
5 6
101010
111111
000001
111111
111111
'''