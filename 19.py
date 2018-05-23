#19 주어진 if 문을 dict를 사용하여 같은 결과가 나오도록 수정하세요.
#기존
# menu=input('메뉴:')
#
# if menu =="오뎅":
#     price=300
# elif menu=="순대":
#     price=400
# elif menu=="만두":
#     price=500
# else:
#     price=0
#
# print('가격: {0}'.format(price))

#딕셔너리사용
menu=input('메뉴:')
list={'오뎅':300, '순대':400, '만두':500}
if menu in list:
    print('가격:',list[menu])
else:
    print('가격:', 0)

