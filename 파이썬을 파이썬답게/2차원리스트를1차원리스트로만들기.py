# 2차원 리스트를 1차원 리스트로 만들기
# 파이썬의 다양한 기능
# https://programmers.co.kr/learn/courses/4008/lessons/12738

def solution(mylist):
    answer = mylist[0]
    for i in range(1, len(mylist)):
        for j in mylist[i]:
            answer.append(j)
    return answer


mylist = [['A', 'B'], ['X', 'Y'], ['1']]
print(solution(mylist))