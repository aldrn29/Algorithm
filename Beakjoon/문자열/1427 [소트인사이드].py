s = list(map(int, list(input())))

sorted_s = sorted(s, reverse=True)
print("".join(list(map(str, sorted_s))))