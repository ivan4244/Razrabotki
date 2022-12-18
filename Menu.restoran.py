print("выберите тип блюда: супы(1) выпечка(2) гарнир(3)")
e = int(input())
if e < 2:
    print('выберите суп: борщ(1), суп пюре(2), щи(3)')
    c = int(input())
    if c < 2:
        print("120р")
    elif c == 2:
        print('140р')
    elif c > 2:
        print('84р')
if e == 2:
    print('выберите выпечку: булочка(1), вишневый пирожок(2), чебурек(3)')
    r = int(input())
    if r < 2:
        print('46р')
    elif r == 2:
        print('38р')
    elif r > 2:
        print('60р')
if e > 2:
    print('выберите гарнир: шашлык(1), жареная картошка(2), плов(3)')
    t = int(input())
    if t < 2:
        print('130р')
    elif t == 2:
        print('83р')
    elif t > 2:
        print('79р')
