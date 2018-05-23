#5 정수 다섯개를 입력받아 가장 큰 수를 출력하세요

print("숫자를 입력하세요")
max=0

for i in range(1,6,1):
    num=int(input("숫자:"))
    if(num>max):
        max=num
print("최대값은", max, "입니다")
