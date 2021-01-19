# 가장 많이 등장하는 알파벳 찾기

my_str = input().strip()

import collections

answer = ''
tmp = collections.Counter(my_str)
cnt = 0
for i in tmp:
    if tmp[i] > cnt:
        cnt = tmp[i]
        answer = i
    else:
        if tmp[i] == cnt:
            answer += i

arr = sorted(list([x for x in answer]))
print(''.join(arr))