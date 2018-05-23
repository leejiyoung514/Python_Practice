#06-(07)
#키보드로 정수 수치를 입력받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요
#입력받은 수치가 숫자인지도 판별하여 숫자가 아닌경우 "숫자가 아닙니다."라고 출력합니다.


num=int(input("수를 입력하세요"))

while num.isdigit():
    if num % 2 == 0:
        print("짝수")
    elif num % 2 == 1:
        print("홀수")
else:
    print('숫자가 아닙니다.')







# try:
#     num = input("수를 입력하세요:")
#     int(num)
#     if int(num) % 2 == 0:
#         print("짝수")
#     elif int(num) % 2 == 1:
#         print("홀수")
# except ValueError as e:
#     print('숫자가 아닙니다.')



