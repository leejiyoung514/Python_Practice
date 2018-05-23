#07-(07)
#a.입력 받은 숫자가 홀수인 경우에는, 입력 값까지 홀수의 합을 출력합니다
#예) 입력시 7이면 16을 출력(1+3+5+7=16)
#b.입력 받은 숫자가 짝수인 경우에는, 입력 값까지 짝수의 합을 출력합니다.

sum=0
num=int(input("숫자를 입력하세요:"))
if num%2==0:
    startNum=2
else:
    startNum=1
for i in range(startNum, num+1, 2):
      sum=sum+i
print("결과값:",sum)