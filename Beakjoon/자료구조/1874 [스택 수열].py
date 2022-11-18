from collections import deque

# m 리트스대로..
# l에 없다면 그 숫자만큼 추가한 뒤 pop
# 마지막 숫자를 pop 하는데, 그 숫자가 아니면 NO
def check() :
    n = int(input())
    m = [int(input()) for _ in range(n)]
    l = deque()
    count = 0
    result = ""

    for i in m :
        while count < i :
            count += 1
            l.append(count)
            result += '+\n'
        
        if l[-1] == i :
            l.pop()
            result += '-\n'
        else :
            return "NO"

    return result

print(check())