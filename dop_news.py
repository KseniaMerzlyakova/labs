news=[(5, 'Курс биткоина вырос до 1000 долларов.'),(10,'В новогоднюю ночь выйдет новая первая серия нового сезона "Шерлока".'),(7, 'В Новосибирске из автобуса сбежала кондуктор.'),(1, 'Самолет «Почты России» вылетел с опозданием в несколько месяцев.'),(20, 'Козёл Тимур подружился с тигром Амуром.'),(10, 'Инженерам из Space X удалось посадить первую ступень ракеты на землю')]
newspub=[]
#a = 0
dict={}
pos=[]
for i,y in news:
    dict[i]=y
    #for positivity, title, in news:
    from functools import reduce
    all_max = reduce(lambda a, b: a if (a > b) else b, dict.keys())
    #print(all_max)
    newspub.append(dict[all_max])
    if newspub.count(dict[all_max])>1:
        newspub.pop()
        #print(all_max)
print(newspub)
    #pos.append(dict.keys())
#print(dict)
#print()
#items = [1, 24, 17, 14, 9, 32, 2]

#all_max
#if int(positivity) > a:
   #newspub.append(title)
#a= positivity
#print(all_max)

