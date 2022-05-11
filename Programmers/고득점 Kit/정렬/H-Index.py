def solution(citations):
    answer = 0
    
    citations.sort(reverse = True) # 6 6 6 6 6 1 
    l = len(citations)
    h = 1
    
    for i in range(l) :
        if citations[i] >= h :
            answer = h
            h += 1
        else : break
       
    return answer