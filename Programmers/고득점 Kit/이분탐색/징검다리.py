# from itertools import combinations

# def solution(distance, rocks, n):
#     answer = 0

#     rocks.sort()
#     rock_list = list(combinations(rocks, len(rocks)-n))
    
#     distance_list = []
#     for i in rock_list :  # (2, 11, 14)
#         temp = [i[0]]
#         for j in range(len(i)-1) :
#             temp.append(i[j+1] - i[j])
        
#         temp.append(distance - i[len(i)-1])
#         distance_list.append(temp)
    
#     # print(distance_list)
#     for i in distance_list :
#         answer = max(answer, min(i))

#     return answer


def solution(distance, rocks, n):
    answer = 0


    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))