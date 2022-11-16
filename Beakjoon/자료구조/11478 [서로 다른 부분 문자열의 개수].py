str = input()
l = len(str)
result = set()

for i in range(1, l+1) :
    for j in range(l-i+1) :
        result.add(str[j:j+i])
        
print(len(result))