import re

s = input().strip()
t = input().strip()

# 숫자만 제거
# new_s = re.sub(r"[0-9]", "", s)
new_s = re.sub("[0-9]", "", s)
print(new_s)
if t in new_s :
    print(1)
else : print(0)