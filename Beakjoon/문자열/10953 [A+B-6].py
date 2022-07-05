from sys import stdin

input = stdin.readline
num = int(input())
for _ in range(num) :
    a, b = map(int, input().strip().split(","))
    print(a+b)

