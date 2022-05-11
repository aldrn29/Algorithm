def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True) # 303030 333 343434 555 999
    
    return str(int(''.join(numbers)))