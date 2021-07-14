from sys import stdin
from collections import deque

row, col = map(int, stdin.readline().split())
matrix = [stdin.readline().strip() for _ in range(row)]
visited = [[0]*col for _ in range(row)]

q = deque()
q.append((0,0))
visited[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q :
    x, y = q.popleft()

    # 도착 위치
    if x == row-1 and y == col-1 :
        print(visited[x][y])
        break

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내에서
        if 0 <= nx < row and 0 <= ny < col :
            # 아직 가보지 않았고, 갈 수 있는 곳이면
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1' :
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))