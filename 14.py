#파이썬 경로명 s="/user/local/bin/python.exe"을 이용하여 아래와 같이 출력해보세요.
#usr,local,bin,python.exe
#/usr/local/bin,python.exe

s="/user/local/bin/python.exe"
s1=s.replace('/',',')
print(s1[1:])
print(s[:15]+','+s[16:])
