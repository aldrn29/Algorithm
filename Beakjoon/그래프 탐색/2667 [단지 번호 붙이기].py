from sys import stdin
from collections import deque

n = int(input())
m = [list(map(int, stdin.readline().strip())) for _ in range(n)]

queue = deque()
visited = [[False]*n for _ in range(n)]
count = 0
num = []

def dfs(x, y) :
    if m[x][y] == 0 or visited[x][y] : return 0

    apart_num = 0
    queue.append((x, y))
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue :
        x, y = queue.popleft()
        apart_num += 1

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if visited[nx][ny] == False and m[nx][ny] == 1 :
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    num.append(apart_num)
    return 1

for i in range(n) :
    for j in range(n) :
        count += dfs(i, j)

print(count)
num.sort()
for i in num :
    print(i)
