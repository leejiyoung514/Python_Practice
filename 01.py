#1에서 70까지의 수에서 5의 배수 이면서 7의 배수인 수를 출력하세요

for i in range(1, 71):
    if i%5==0 and i%7==0:
        print(i)