# 순열과 조합

import itertools


def solution(mylist):
    mylist.sort()
    answer = list(map(list, itertools.permutations(mylist)))
    return answer


mylist = [1, 2, 3]
print(solution(mylist))
