# 2차원 리스트 뒤집기

def solution(mylist):
    return list(map(list, zip(*mylist)))


mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(solution(mylist))