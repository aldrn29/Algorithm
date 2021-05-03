import re

def solution(new_id):
    answer = new_id
    # 1단계
    answer = answer.lower()
    # 2단계: 소문자, 숫자, -, _, .
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    # 3단계: 마침표 2개 이상을 1개로
    answer = re.sub('\.+', '.', answer)
    # 4단계: .가 처음이나 끝에 위치하면 제거
    answer = re.sub('^[.]|[.]$', '', answer)
    # 5단계: 빈 문자열이라면 a 대입, 6단계: 15자까지, .가 끝에 위치하면 제거
    answer = 'a' if len(answer) == 0 else answer[:15]
    answer = re.sub('^[.]|[.]$', '', answer)
    # 7단계: 길이가 2이하라면 마지막 문자를 3이 될때까지
    answer = answer if len(answer) > 2 else answer + "".join([answer[-1] for i in range(3-len(st))])
    
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))