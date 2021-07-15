from sys import stdin
from collections import deque

test_case = int(input())
num = []

def bfs(x, y) :
    if visited[x][y] or matrix[x][y] == 0 : return

    queue.append((x,y))
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col :
                if visited[nx][ny] == False and matrix[nx][ny] == 1 :
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    global count
    count += 1

for _ in range(test_case) :
    col, row, k = map(int, stdin.readline().split())
    matrix = [[0 for _ in range(col)] for _ in range(row)]  

    for _ in range(k) :
        y, x = map(int, stdin.readline().split())
        matrix[x][y] = 1

    queue = deque()
    visited = [[False for _ in range(col)] for _ in range(row)]
    count = 0

    for i in range(row) :
        for j in range(col) :
            bfs(i, j)

    num.append(count)

for i in num :
    print(i)