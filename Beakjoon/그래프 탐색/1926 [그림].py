from sys import stdin
from collections import deque

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
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col :
                if not visited[nx][ny] and m[nx][ny] == 1 :
                    queue.append((nx, ny))
    return cnt

row, col = map(int, stdin.readline().split())
m = [list(map(int, stdin.readline().split())) for _ in range(row)]
visited = [[False] * col for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
area = 0

for i in range(row) :
    for j in range(col) :
        if not visited[i][j] and m[i][j] == 1 : 
            area = max(area, bfs(i, j))
            count += 1

print(count)
print(area)