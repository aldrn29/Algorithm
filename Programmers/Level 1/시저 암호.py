def solution(s, n):
    answer = ''

    for i in s:
        if i == " ": 
            answer += " " 
            continue
        else: 
            temp = ord(i) + n
            if i <= 'z' and temp > ord('z'): temp -= 26
            elif i <= 'Z' and temp > ord('Z'): temp -= 26
            answer += chr(temp)
    return answer

print(solution("a B z", 4))