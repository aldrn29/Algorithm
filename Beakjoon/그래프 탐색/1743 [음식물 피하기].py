from sys import stdin
from collections import deque

row, col, n = map(int, stdin.readline().split())
m = [[0]*(col+1) for _ in range(row+1)]
visited = [[False] * (col+1) for _ in range(row+1)]

for i in range(n) :
    x, y = map(int, stdin.readline().split())
    m[x][y] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y) :
    queue = deque()
    queue.append((x,y))
    cnt = 0

    while queue :
        x, y = queue.popleft()

        if visited[x][y] : continue
        else : 
            visited[x][y] = True
            cnt += 1
        
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 < nx < row+1 and 0 < ny < col+1 :
                if m[nx][ny] == 1 :
                    queue.append((nx, ny))
    return cnt

m_count = 0
for i in range(row+1) :
    for j in range(col+1) :
        if not visited[i][j] and m[i][j] == 1 :
            temp = bfs(i, j)
            m_count = max(temp, m_count)

print(m_count)