num = int(input())
result = set()

for _ in range(num) :
    result.add(input())

result = list(result)
result.sort()
result.sort(key=len)

for i in result :
    print(i)