# 주식가격

# 나의 풀이
def solution(prices):
    answer = []

    for i in range(0, len(prices) - 1):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[j] >= prices[i]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    answer.append(0)

    return answer


# testcase1
prices = [1, 2, 3, 2, 3]
print(solution(prices))
