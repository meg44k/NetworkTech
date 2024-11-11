n = int(input())

if n < 1:
    print("1未満の値は入力できません")
else:
    for i in range(1,n+1):
        if i == 1:
            a = 1
            print(a)
        elif i == 2:
            b = 1
            print(b)
        else:
            c = a + b
            a = b
            b = c
            print(c)