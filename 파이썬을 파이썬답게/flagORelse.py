# flag OR else

arr = [int(input()) for _ in range(5)]

tmp = 1
for i in arr:
    tmp *= i
    if tmp ** 0.5 == int(tmp ** 0.5):
        print('found')
        break
else:
    print('not found')