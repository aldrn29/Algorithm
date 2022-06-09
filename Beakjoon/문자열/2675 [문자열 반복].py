num = int(input())

for _ in range(num) :
    repeat, str = input().split()
    result = ''

    for i in str :
        result += i * int(repeat)
    print(result)