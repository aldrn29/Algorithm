from sys import stdin   
input = stdin.readline

def isPrime(num) :
    if num < 2 : 
        return False

    x = int(num**(1/2))
    for i in range(2, x+1) :
        if num % i == 0 :
            return False
    return True

m = int(input())
n = int(input())
result = []

for i in range(m, n+1) :
    if isPrime(i) : 
        result.append(i)

if len(result) > 0 :
    print(sum(result))
    print(result[0])
else : print(-1)
