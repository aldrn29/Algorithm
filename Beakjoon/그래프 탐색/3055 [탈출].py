from sys import stdin
from collections import deque

row, col = map(int, stdin.readline().split())
m = [stdin.readline().strip() for _ in range(row)]

queue = deque()
visited = [[0]*col for _ in range(row)]

for i in range(row) :
    for j in range(col) :
        if m[i][j] == '*' : 
            water_position = (i, j)
            visited[i][j] = -1
        if m[i][j] == 'S' : queue.append((i, j)) # 고슴도치

queue.append(water_position) # 물

def bfs() :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col :
                if visited[nx][ny] >= 0 and not m[nx][ny] == 'X': 
                    if visited[x][y] >= 0 :
                        visited[nx][ny] = visited[x][y] + 1 # 고슴도치 이동거리
                        queue.append((nx, ny))

                        if m[nx][ny] == 'D' :  # 고슴도치가 비버에게 도착했을 경우
                            return print(visited[nx][ny])
                    else :
                        if m[nx][ny] != 'D' :
                            visited[nx][ny] = -1
                            if queue.count((nx, ny)) <= 0 : queue.append((nx, ny))

    return print('KAKTUS')
                    
bfs()
