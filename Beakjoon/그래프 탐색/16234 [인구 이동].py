from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    nation = []

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue :
        x, y = queue.popleft() 

        if visited[x][y] : continue
        else : 
            visited[x][y] = True
            nation.append((x, y))

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if not visited[nx][ny] and l <= abs(m[x][y] - m[nx][ny]) <= r :
                    queue.append((nx, ny))

    if len(nation) > 1 :
        tmp_sum = 0
        for t in nation : 
            tmp_sum += m[t[0]][t[1]]
        tmp = tmp_sum // len(nation)
        for t in nation : 
            m[t[0]][t[1]] = tmp
        return 1
    else : 
        return 0

n, l, r = map(int, stdin.readline().split())
m = [list(map(int, stdin.readline().split())) for _ in range(n)]
date = 0

while True :
    visited = [[False] * n for _ in range(n)]
    t = 0

    for i in range(n) :
        for j in range(n) :
            if visited[i][j] : continue
            t += bfs(i, j)

    if t > 0 : date += 1
    else : 
        print(date)
        break
    