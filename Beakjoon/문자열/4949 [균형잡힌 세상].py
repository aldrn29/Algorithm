from sys import stdin

input = stdin.readline

def solution(s) :
    stack = []
    for x in s :
        if x == '.' :
            if len(stack) > 0 :
                return "no"
            return "yes"

        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')' or x == ']':
            if len(stack)  < 1 :
                return "no"
            
            if stack[-1] == '(' and x == ')' :
                stack.pop()
            elif stack[-1] == '[' and x == ']' :
                stack.pop()
            else : return "no"

while True :
    s = input().rstrip()
    if s == '.' : break
    else : 
        print(solution(s))