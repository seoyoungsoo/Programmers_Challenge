# sequence 멤버를 하나로 이어붙이기

# 나의 풀이
def solution(mylist):
    answer = ''
    for i in mylist:
        answer += i
    return answer

# join을 이용한 풀이
def otherSol(mylist):
    return ''.join(mylist)


mylist = ['1', '100', '33']
print(solution(mylist))
print(otherSol(mylist))