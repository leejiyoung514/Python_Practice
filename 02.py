#02. 숫자를 입력받아 아래와 같이 출력하시오
# 1
# 22
# 333
# 4444
# .....
num=int(input("숫자를 입력하세요\n"))
for a in range(1, num+1, 1):
    for b in range(1, num+1, 1):
       if a>=b:
           print(a, end=" ")
    print(" ")