from sys import stdin
from collections import deque

col, row = map(int, stdin.readline().split())
m = [list(map(int, stdin.readline().split())) for _ in range(row)]
visited = [[False] * col for _ in range(row)]

# (0,0) (0,1) ... (0,7)
# ...
# ...
# (3,0) (3,1) ... (3,7)

def bfs(x, y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.popleft()
        
        if visited[x][y] : continue
        else : visited[x][y] = True

        dx = [-1, -1, 0, 0, 1, 1]
        if x % 2 == 0 : 
           dy = [0, 1, -1, 1, 0, 1]
        else : dy = [-1, 0, -1, 1, -1, 0]
        adj = 0
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < row and 0 <= ny < col : 
                if m[nx][ny] == 1 :
                    adj += 1
                    if not visited[nx][ny] :
                        queue.append((nx, ny)) 
                    
        # 벽면 길이의 합 = 6 - 맞닿은 면
        global count
        count += 6 - adj

def check(x, y) :
    queue = deque()
    queue.append((x,y))
    
    global inside
    while queue :
        x, y = queue.popleft()
        
        if visited[x][y] : continue
        else : visited[x][y] = True

        dx = [-1, -1, 0, 0, 1, 1]
        if x % 2 == 0 : 
            dy = [0, 1, -1, 1, 0, 1]
        else : dy = [-1, 0, -1, 1, -1, 0]

        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0 <= nx < row and 0 <= ny < col : 
                if  not visited[nx][ny] and m[nx][ny] == 0 :
                    queue.append((nx, ny)) 

def inside_bfs(x, y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.popleft()
        
        if visited[x][y] : continue
        else : visited[x][y] = True

        dx = [-1, -1, 0, 0, 1, 1]
        if x % 2 == 0 : 
           dy = [0, 1, -1, 1, 0, 1]
        else : dy = [-1, 0, -1, 1, -1, 0]
        adj = 0
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < row and 0 <= ny < col : 
                if m[nx][ny] == 0 :
                    adj += 1
                    if not visited[nx][ny] :
                        queue.append((nx, ny)) 
                    
        global inside_count
        inside_count += 6 - adj

count = 0
inside = []
inside_count = 0

for i in range(row) :
    for j in range(col) :
        if not visited[i][j] and m[i][j] == 1 :
            bfs(i, j)

for i in range(row) :
    for j in range(col) :
        if 0 < i < row-1 and 0 < j < col-1 : continue
        if not visited[i][j] and m[i][j] == 0 :
            check(i, j)

for i in range(row) :
    for j in range(col) :
        if not visited[i][j] :
            inside.append((i,j))

visited = [[False] * col for _ in range(row)]
for i, j in inside :
    inside_bfs(i,j)

print(count - inside_count)