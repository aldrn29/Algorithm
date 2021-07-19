from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
queue = deque()
visited = [0] * 100001

queue.append(n)
while queue :
    x = queue.popleft() 

    if x == k : 
        print(visited[x])
        break

    for i in (x-1, x+1, x*2) : # 4, 6, 10
        if 0 <= i < 100001 and visited[i] == 0 : 
            visited[i] = visited[x] + 1
            queue.append(i)

