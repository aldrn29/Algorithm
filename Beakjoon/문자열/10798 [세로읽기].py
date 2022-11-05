matrix = [input().strip() for _ in range(5)]
result = ''
max_col = len(max(matrix, key=len))

for c in range(max_col) :
    for r in range(5) :
        if len(matrix[r]) <= c : continue
        result += matrix[r][c]

print(result)

# try:
#    print(matrix[r][c], end='')
# except:
#    continue