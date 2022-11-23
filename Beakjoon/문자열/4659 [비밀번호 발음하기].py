import re

def check(s) :
    v = "aeiou"
    p = re.compile('[a|e|i|o|u]')
    m = p.search(s)
    
    # 모음 하나를 반드시 포함하는 경우
    if m == None :
        return False
    else :
        # 모음, 자음이 연속으로 오는 경우
        for i in range(len(s) - 2) :
            # 모음인 경우
            if s[i] in v :
                if s[i+1] in v :
                    if s[i+2] in v :
                        return False
            # 자음인 경우
            elif s[i] not in v :
                if s[i+1] not in v :
                    if s[i+2] not in v :
                        return False

        # 같은 글자가 연속적으로 두번 오는 경우
        for i in range(len(s) - 1) :
            if s[i] == s[i+1] and s[i] != 'e' and s[i] != 'o' :
                return False

    return True

while True :
    str = input()
    if str != 'end' :
        if check(str) :
            print("<", str, "> is acceptable.", sep='')
        else :
            print("<", str, "> is not acceptable.", sep='')
    else :
        break


'''
# 정규표현식만 이용하여 풀이

while True :
    str = input()
    if str == 'end' :
        break

    case1 = len(re.findall('[aeiou]', str)) != 0 
    case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}', str)) == 0
    case3 = len(re.findall('([a-df-np-z])\\1', str)) == 0


    if case1 and case2 and case3:
        print(f'<{str}> is acceptable.')
    else:
        print(f'<{str}> is not acceptable.')
'''