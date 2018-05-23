#20 문자열을 입력받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

str=input('입력>')
s = ''.join(reversed(str))
print(s)

str1 = input('입력>')
str1 = str1[::-1]
print(str1)
