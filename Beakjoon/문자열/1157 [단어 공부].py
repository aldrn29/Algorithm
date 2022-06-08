from collections import defaultdict


word = input().upper()
dict = defaultdict(int)

for i in word :
    dict[i] += 1

max_count = max(dict.values())
max_alphabet = ""
count = 0
for key, value in dict.items() :
    if value == max_count :
        count += 1
        max_alphabet = key

if count == 1 :
    print(max_alphabet)
else :
    print("?")
