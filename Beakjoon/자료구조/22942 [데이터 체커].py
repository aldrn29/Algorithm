# 원 하나를 스택에 추가하고, 나머지 원들과 비교한다.
# 만약 다른 모든 원들과 겹치지 않으면 넘어가고, 다른 원을 스택에 추가하여 다시 비교 반복한다.
# 겹치면 NO 

'''
def check(circles) :
    while circles :
        temp = circles.pop()
        # 원 밖 or 원 안에 있는지 확인
        for i in range(len(circles)) : 
            d = abs(circles[i][0] - temp[0])
            if circles[i][1] + temp[1] < d or abs(circles[i][1] - temp[1]) > d :
                continue
            else :
                return "NO"
        
        temp = circles.pop()
        
    return "YES"


n = int(input())
circles = []
for _ in range(n) :
    x, r = map(int, input().split())
    circles.append((x, r))

print(check(circles))
'''

from sys import stdin
n = int(input())

circles = []
stack = []

for _ in range(n) :
    # x, r = map(int, input().split())
    x, r = map(int, stdin.readline().split())
    circles.append((x-r, x, 0))
    circles.append((x+r, x, 1))

circles.sort()

for i in range(len(circles)) :
    if circles[i][2] == 0 :
        stack.append(circles[i][1])
    elif circles[i][2] == 1 :
        if circles[i][1] == stack.pop() :
            continue
        else :
            print("NO")
            exit(0)

print("YES")