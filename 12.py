#주어진 문자열의 공백을 콤마(,)로 변경 후 출력하세요
s="This is a pencil"
#This is a pencil
#This,is,a,pencil
print(s.replace(s,"This,is,a,pencil"))
print(s.replace(" ", ","))