from sys import stdin
from collections import deque

row, col, num = map(int, stdin.readline().split())
matrix = [[0]*col for _ in range(row)]

for i in range(num) :
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for x in range(y1, y2) :
        for y in range(x1, x2) :
            matrix[x][y] = 1

queue = deque()
visited = [[False]*col for _ in range(row)]
count = []

def dfs(x, y) :
    if visited[x][y] or matrix[x][y] == 1 : return

    queue.append((x, y))
    visited[x][y] = True
    num = 0

    while queue :
        x, y = queue.popleft()
        num += 1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col :
                if visited[nx][ny] == False and matrix[nx][ny] == 0 :
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    count.append(num)

for i in range(row) :
    for j in range(col) :
        dfs(i, j)

count.sort()
print(len(count))
for i in count :
    print(i, end=' ')

