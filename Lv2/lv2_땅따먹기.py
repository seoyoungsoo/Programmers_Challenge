# 땅따먹기

def solution(land):
    for i in range(1, len(land)):
        # 첫 번째 칸
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])

        # 두 번째 칸
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])

        # 세 번째 칸
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])

        # 네 번째 칸
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])

    return max(land[-1])


land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
print(solution(land))
