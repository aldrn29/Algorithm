from sys import stdin
from collections import deque

row, col = map(int, stdin.readline().split())
m = [list(stdin.readline().strip()) for _ in range(row)]

def bfs(x, y) :
    queue = deque()
    queue.append((x,y))
    visited = [[0]*col for _ in range(row)]
    start = (x, y)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col and (nx, ny) != start :
                if m[nx][ny] == 'L' and visited[nx][ny] == 0 :
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return max(map(max, visited))

move = 0
for i in range(row) :
    for j in range(col) :
        if not m[i][j] == 'L' : continue
        value = bfs(i,j)
        move = max(move, value)

print(move)