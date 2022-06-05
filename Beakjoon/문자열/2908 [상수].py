num = input().split()

num1 = int(num[0][::-1])
num2 = int(num[1][::-1])

print(num1 if num1 > num2 else num2) 