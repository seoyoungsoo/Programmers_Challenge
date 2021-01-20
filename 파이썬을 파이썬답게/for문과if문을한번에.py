# for 문과 if문을 한번에

def solution(mylist):
    return [i ** 2 for i in mylist if i % 2 == 0]


mylist = [3, 2, 6, 7]
print(solution(mylist))
