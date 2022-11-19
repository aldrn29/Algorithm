str = input().strip()
stick = []
result = 0

for i in range(len(str)) :
    if str[i] == '(' :
        stick.append('(')
    else :
        # 레이저 
        if str[i-1] == '(' :
            stick.pop()
            result += len(stick)
        else :
            stick.pop()
            result += 1

print(result)