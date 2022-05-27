from collections import deque 

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    count = [0 for _ in range(n+1)]
    queue = deque()

    for a, b in edge :
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n+1) :
        graph[i].sort()

    queue.append(1)
    count[1] = 1

    while queue :
        x = queue.popleft()

        for i in graph[x] :
            if count[i] == 0 :
                queue.append(i)
                count[i] = count[x] + 1

    max_count = max(count)
    for i in range(n+1) :
        if count[i] == max_count :
            answer += 1
                
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))