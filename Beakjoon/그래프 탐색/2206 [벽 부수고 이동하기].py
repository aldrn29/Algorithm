from sys import stdin
from collections import deque

def bfs(x, y, is_break) :
    queue = deque()
    queue.append((x, y, is_break))
    visited[x][y][is_break] = 1

    while queue :
        x, y, is_break = queue.popleft()

        if x == row-1 and y == col-1 :
            return visited[x][y][is_break]

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col :
                if m[nx][ny] == 0 and visited[nx][ny][is_break] == 0 : # 벽이 아닐 때
                    queue.append((nx, ny, is_break))
                    visited[nx][ny][is_break] = visited[x][y][is_break] + 1
                elif m[nx][ny] == 1 and is_break == 0 : # 벽일 때 and 벽을 부순적이 없을 때
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][is_break] + 1

    return -1

row, col = map(int, stdin.readline().split())
m = [list(map(int, stdin.readline().strip())) for _ in range(row)]
visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(bfs(0,0,0))
