def z1():
    a = input('Введите пароль: ')

    is_numeric = False
    is_lower = False
    is_spec = False
    is_upper = False

    for x in a:
        if x.isnumeric():
            is_numeric = True
        elif x.islower():
            is_lower = True
        elif x.isupper():
            is_upper = True
        elif x in "@#%&":
            is_spec = True

    if len(a) > 4 and is_numeric and is_upper  and is_lower and is_spec:
       print('Ок')
    else:
       print('no')
def z2():
    a = int(input('Введите номер места в вагоне '))
    if (a) <= 0 or a >= 55:
        print('неправильное место')

    if (a) % 2 == 0 and a <= 36 and a > 0:
        print('Верхнее')
    if int(a) % 2 != 0 and a <= 36:
        print('Нижнее')

    if a > 36:
        for i in range(37, 55):
            if int(a) == i:
                print('Боковое')

def z3():
    a = input('Введите год ')
    if (int(a) % 4 == 0 and int(a) % 100 != 0) or int(a) % 400 == 0:
        b = f"Год  {a}  -  високосный"
        print(b)
    else:
        print("Это год не високосный")

def z4():
    a = input('введите 1 цвет ')
    b = input('введите 2 цвет ')
    x = ""
    y = 0
    if (a) != ('красный') and str(a) != ('синий') and str(a) != ('желтый'):
        print('Error')
    elif str (b) != ('красный') and str(b) != ('синий') and str(b) != ('желтый'):
        print('Error')
    else:
       #for i in a:
        if str(a)==('красный') or str(b)==('красный') :
            collor_num1 = 10
        else:
            collor_num1 = 0
        if str(a)==('синий') or str(b)==('синий') :
            collor_num2 = 20
        else:
            collor_num2 = 0
        if str(a)==('желтый') or str(b)==('желтый') :
            collor_num3  =  30
        else:
            collor_num3 = 0
        collor_num = collor_num1 + collor_num2 + collor_num3

        if collor_num == 30:
          x = ('фиолетовый')
        elif collor_num == 40:
          x = ('оранжевый')
        elif collor_num == 50:
          x = ('зеленый')


    print(x) #+ str(collor_num)+ "  "+ str(collor_num1)+"  "+ str(collor_num2)+ "  " +str(collor_num3))

def z5():
    kol = input('введите количество слов ')
    i = 0
    s = ""
    while int(i) < int(kol):
        a = input('')
        i += 1
        if i == 1:
            s = str(s) + str(a)
        else:
            s = str(s) + " " + str(a)
    # s = str(s) +  str(a) +", "
    print(str(s))

z1(),z2(),z3(),z4(),z5()