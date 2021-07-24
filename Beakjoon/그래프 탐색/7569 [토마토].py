from sys import stdin
from collections import deque

col, row, h = map(int, stdin.readline().split())
m = []
start = [] # 토마토 시작 위치

for i in range(h) :
    temp = []
    for j in range(row) :
        temp.append(list(map(int, stdin.readline().split())))
        for k in range(col) :
            if temp[j][k] == 1 : start.append((i, j, k))
    m.append(temp)


def bfs(start) :
    queue = deque()
    for z, x, y in start :
        queue.append((z, x, y))

    while queue :
        z, x, y = queue.popleft()

        for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)] :
            nx = x+dx
            ny = y+dy
            nz = z+dz
            
            if 0 <= nx < row and 0 <= ny < col and 0 <= nz < h: 
                if m[nz][nx][ny] == 0 :
                    m[nz][nx][ny] = m[z][x][y] + 1
                    queue.append((nz, nx, ny))

    max_day = 0
    for i in m : 
        for j in i :
            for k in j : 
                if k == 0 :
                    return print(-1)
                max_day = max(max_day, k)
    return print(max_day - 1)

bfs(start)