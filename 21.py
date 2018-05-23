#21함수 sum()을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def sum(*args):
    total=0
    for each in args:
        total+=each
    print(total)

sum()
sum(0,3,20)


