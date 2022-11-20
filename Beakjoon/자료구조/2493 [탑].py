num = int(input())
tops = list(map(int, input().split()))

stack = []
stack.append((tops[-1], num-1)) 
result = [0 for _ in range(num)]

for i in range(num-2, -1, -1) :
    while stack :  
        if stack[-1][0] <= tops[i] :
            result[stack.pop()[1]] = i+1 
        else :
            stack.append((tops[i], i))
            break
    stack.append((tops[i], i)) 

print(*result)