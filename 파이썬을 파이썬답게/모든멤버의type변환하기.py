# 모든 멤버의 type 변환하기

def solution(mylist):
    return list(map(int, [x for x in mylist]))

mylist = ['1', '100', '33']
print(solution(mylist))