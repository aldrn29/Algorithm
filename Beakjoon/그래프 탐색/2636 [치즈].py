from sys import stdin
from collections import deque

row, col = map(int, stdin.readline().split())
m = [list(map(int, stdin.readline().split())) for _ in range(row)]
date = 0
last_list = []

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    visited = set()
    cheese = []

    while queue :
        x, y = queue.popleft()

        if not m[x][y] == 0 : continue
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
            nx = x + dx
            ny = y + dy

            if 0 <= nx < row and 0 <= ny < col :
                if (nx, ny) not in visited :
                    visited.add((nx, ny))
                    if m[nx][ny] == 0 : queue.append((nx, ny))
                    if m[nx][ny] == 1 :
                        cheese.append((nx, ny))
    return cheese

while True :
    cheese_list = bfs(0, 0)
    
    if len(cheese_list) <= 0 :
        print(date)
        print(len(last_list))
        break
    else : last_list = cheese_list

    for i in cheese_list :
        m[i[0]][i[1]] = 0 

    date += 1