from sys import stdin
from collections import deque

n = int(input())
m = [stdin.readline().strip() for _ in range(n)]

def bfs(x, y, rg) :
    if visited[x][y] == 1 : return 0

    queue.appendleft((x,y))
    visited[x][y] = 1

    while queue :
        x, y = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if rg == 0 : # 적록색약이 아닌 사람
                    if visited[nx][ny] == 0 and m[x][y] == m[nx][ny] :
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                else : # 적록색약인 사람
                    if visited[nx][ny] == 0 and (m[x][y] == m[nx][ny] or 
                                                (m[x][y] == 'R' and m[nx][ny] == 'G') or 
                                                (m[x][y] == 'G' and m[nx][ny] == 'R')) :
                        visited[nx][ny] = 1
                        queue.append((nx, ny))

    return 1

for rg in range(2) :
    queue = deque()
    visited = [[0]*n for _ in range(n)]
    count = 0

    for i in range(n) :
        for j in range(n) :
            count += bfs(i, j, rg)
    print(count, end=' ')