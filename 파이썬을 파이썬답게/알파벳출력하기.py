# 알파벳 출력하기
num = int(input().strip())
import string

if num:
    print(string.ascii_uppercase)
else:
    print(string.ascii_lowercase)