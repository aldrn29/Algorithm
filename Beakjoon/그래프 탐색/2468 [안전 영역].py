from sys import stdin
from collections import deque

n = int(input())
m = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = []

def bfs(x, y, h) :
    if visited[x][y] or m[x][y] < h : return 0

    queue.append((x, y))
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if visited[nx][ny] == False and m[nx][ny] >= h :
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return 1

for h in range(1, max(map(max, m))) : 
    queue = deque()
    visited = [[False]*n for _ in range(n)]
    count = 0

    for i in range(n) :
        for j in range(n) :
            count += bfs(i, j, h)
    result.append(count)

print(max(result))
