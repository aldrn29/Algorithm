from sys import stdin
from collections import deque

n = int(input())
m = [list(map(int, stdin.readline().strip())) for _ in range(n)]
visited = set()

def bfs(start) : 
    queue = deque()
    queue.append(start)
    cnt = 0
    
    while queue :
        x, y = queue.popleft()

        if (x, y) in visited : continue
        else : 
            visited.add((x,y)) 
            cnt += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)] :
            nx = x+dx
            ny = y+dy

            if 0 <= nx < n and 0 <= ny < n : 
                if m[nx][ny] == 1 and (nx, ny) not in visited : 
                    queue.append((nx, ny))
                    visited.add((x, y))
                    
    return cnt


count = []

# 모든 정점을 시작점으로 bfs 탐색
for i in range(n) :
    for j in range(n) :
        if m[i][j] == 1 and (i, j) not in visited : 
            count.append(bfs((i, j)))

print(len(count))
print('\n'.join(map(str, sorted(count))))
