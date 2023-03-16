def z1(a):

 return True if a % 3 == 0 else False

def z2(a):
    try:
        #a = int(input('Введите число: '))
        b = 100 / int(a)
    except ZeroDivisionError:
        print('Введён 0')
    except ValueError:
        print('Введено не число')
    else:
        print('Результат деления 100 на введённое число: ', b)

def z3(a):
    #date = input('Введите дату в формате дд.мм.гггг: ')
    a = a.split('.')
    if int(a[0]) * int(a[1]) == int(a[2][2:4]):
        print('Дата магическая')
    else:
        print('Дата не является магической')

def z4(a):
    x = 0
    y = 0
    if len(str(a)) % 2 == 0:
        for i in a[0:int(len(a) / 2)]:
            x = x + int(i)
        for i in a[int(len(a) / 2):int(len(a))+1]:
            y = y + int(i)
        if x == y:
            print('Билет счастливый!')
        else:
            print('Билет несчастливый!')
    else:
            print('Неправильно введен номер билета(кол-во цифр нечетное)!')

if __name__ == "__main__":
    print(z1(0))
    print(z2(0))
    print(z3('02.11.2022'))
    print(z4('385916'))