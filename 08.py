import random

#08-(08)
#숨겨진 숫자를 맞추는 게임입니다.
#프로그램이 실행되면 1~100 사이의 숫자가 결정됩니다.
#사용자가 입력한 숫자가 결정된 숫자보다 높으면 "더 낮게"출력
#사용자가 입력한 숫자가 결정된 숫자보다 낮으면 "더 높게" 출력되며
#정답을 맞춘 경우" 맞았습니다." 출력됩니다.
#게임을 반복하기 위해 y/n이라 묻고 n인 경우 종료됩니다.
#(y인경우 다시 게임이 시작됩니다.)

#입력하는수, 비교되는수(랜덤값)

rn=random.randrange(1,101,1)

print("============================")
print("   [숫자맞추기게임 시작]    ")
print("============================")

while True:
    num = int(input("숫자: "))
    if(num>rn):
        print("더 낮게")
        continue
    elif(num<rn):
        print("더 높게")
        continue
    else:
        print("정답입니다.")

    str=input("게임을 종료하시겠습니까?(y/n):")
    if(str=='y'):
        print("============================")
        print("   [숫자맞추기게임 종료]    ")
        print("============================")
        break
    elif(str=='n'):
        False
