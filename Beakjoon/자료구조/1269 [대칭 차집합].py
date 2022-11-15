a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# result = (A | B) - (A & B)
result = A ^ B
print(len(result))


