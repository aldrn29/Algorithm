def solution(participant, completion):
    dic = dict()
    
    for p in participant :
        dic[p] = dic.get(p, 0) + 1
            
    for c in completion :
        dic[c] = dic.get(c) - 1
    
    for p in participant :
        if dic.get(p) > 0 :
            return p