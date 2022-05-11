def solution(clothes):
    answer = 1
    closet = dict() # 종류가 같은 것끼리 저장해 놓을 변수
    
    # 종류가 같은 것 분류해서 저장
    for c in clothes:
        if c[1] in closet.keys():
            closet[c[1]].append(c[0])
        else:
            closet[c[1]] = [c[0]]
    
    # 경우의 수 구하기            
    for value in closet.values():
        print(value)
        answer *= len(value) + 1
    
    # 아무것도 입지 않은 경우 제외
    return answer-1