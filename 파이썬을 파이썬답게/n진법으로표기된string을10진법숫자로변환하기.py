# n진법으로 표기된 string을 10진법 숫자로 변환하기

num, base = map(int, input().strip().split(' '))
n = str(num)
l = len(n) - 1

res = 0
for i in n:
    res += int(i) * (base ** l)
    l -= 1
print(res)

# int 함수는 진법 변환을 지원함
# ex)
print(int(str(num), base))