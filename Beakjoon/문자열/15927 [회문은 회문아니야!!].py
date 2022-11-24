str = input()

# 같은 문자 반복일 때
if str == str[0] * len(str) :
    print(-1)
# 회문인 경우
elif str == str[::-1] :
    print(len(str) - 1) 
else : 
    print(len(str))
