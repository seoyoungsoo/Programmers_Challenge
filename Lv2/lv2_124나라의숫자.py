# 124 나라의 숫자

# 1,2,4를 사용하는 3진법이라고 생각하고 접근해야 함
# 3의 배수일 때와 아닐 때가 다름
# #1, #2: 왜 +=가 아닌지 잘 생각해보자
# 나의 풀이
def solution(n):
    answer = ''

    while n > 0:
        if n % 3:
            answer = str(n % 3) + answer  # #1
            n //= 3
        else:
            answer = '4' + answer  # #2
            n = n // 3 - 1

    return answer


# 다른 풀이
def otherSol(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n % 3] + answer
        n //= 3

    return answer


# testcase1
n = 57
print(solution(n))
print(otherSol(n))