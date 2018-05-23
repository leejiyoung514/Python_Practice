#15 반복문을 이용하여 369게임에서 박수를 처야 하는 경우의 수를 순서대로 화면에 출력해보세요. 1부터 99까지만 실행하세요.

#369게임
#3,6,9 중
# 숫자가 1개면,  짝
# 숫자가 2개면 짝짝

for c in [str(x) for x in range(1,100)]:
	count = c.count('3') + c.count('6') + c.count('9')
	if count:
		print (c,'짝'*count)
	# else:
	# 	print (c)




