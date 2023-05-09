import random

a = [random.randint(1, 10) for i in range(5)]
#print('случайно сгенерированный список - ' + str(a))

b = int(input('Введите случайное число - '))
if b in a:
    print('Поздравляю, вы угадали число: ' + 'ваше число- ' + str(b))
    print('случайно сгенерированный список - ' + str(a))
else:
    print('Нет такого числа - ' + ' ваше число- ' + str(b))
    print('случайно сгенерированный список - ' + str(a))
pov = {x for x in a if a.count(x) > 1}

print('Повторяющиеся числа ' + str(pov))



def d1():
    days = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Суб', 'Вс')
    n_days = list(days)
    n2_days = n_days.copy()
    #print(n_days)
    days_off = int(input('Сколько выходных ты хочешь?'))
    del n_days[0:7 - days_off:1]
    n_days1 = tuple(n_days)
    print('Твои выходные: ', n_days1)
    del n2_days[7 - days_off: 7:1]
    n_days2 = tuple(n2_days)
    print('Рабочие дни: ', n_days2)

def d2():
 a = (input('Нажмите пробел + Enter, чтобы продолжить'))
 if a == (' '):
  users1 = ["Кудяшова", "Тоцкая", "Васькова","Aймалетдинова","Автореева","Баданина","Васильева","Беляева", "Джимбеев", "Жук"]
  users2 = ["Кудяшова2", "Тоцкая2", "Васькова2","Aймалетдинова2","Автореева2","Баданина2","Васильева2","Беляева2", "Джимбеев2", "Жук"]
  print(users1)
  print(users2)
  users1.sort()
  n = 0
  users2.reverse()
  u12=users1.copy()
  u21=users2.copy()
  del users1[5:11:1]
  del u12[0:5:1]
  del users2[5:11:1]
  del u21[0:5:1]
  play1=u21+users1
  play2=u12+users2
  play2.sort()
  pl = tuple(play1)
  p2 = tuple(play2)
  prov = "Жук" # элемент для удаления
  for i in p2:
   if i ==  prov:
    n = n+1
  print('новая тим: ', p2, 'кол-во участников: ', len(p2), 'Количество участников с фамилией Жук', n)


d1()
d2()