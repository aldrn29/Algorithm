def solution(phoneBook): 
    phoneBook.sort()
    
    for i in range(len(phoneBook) - 1): 
        if phoneBook[i+1].startswith(phoneBook[i]): 
            return False 
    return True