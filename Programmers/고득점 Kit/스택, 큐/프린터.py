from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque(priorities)
    temp = deque([i for i in range(len(queue))])
    
    while queue :
        x = queue.popleft()
        
        if queue :
            if x < max(queue) :
                temp.append(temp.popleft())
                queue.append(x)
            else :
                answer += 1
                if temp[0] == location :
                    return answer
                else :
                    temp.popleft()
    return answer + 1