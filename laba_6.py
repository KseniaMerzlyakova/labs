countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}
print(countries_dict)
print(countries_dict["Сербия"])
a = input('Введите страну ')
if a in countries_dict:
    print( countries_dict[a])
else:
    print('no')
for key in sorted(countries_dict):
    print(key, " - ", countries_dict[key])

def d1():
 alp = {
         "авеинорст" : 1,
         "дклмпу" : 2,
         "бгёья" : 3,
         "йы" : 4,
         "жзхцч" : 5,
         "шэю" : 8,
         "фщъ" : 10
        }
 a = input('введите слово: ')
 s = 0
 for i in a:
    for x in alp:
        if i in x:
            s += alp[x.lower()]
 print ("Cумма: ", s)

def d2():
 students = {"student1" : "испанский немецкий", "студент2" : "русский китайский французский", "студент3" : "китайский французский итальянский"}
 z = []
 st = []
 z1=[]
 for i in students:
     c = students[i.lower()].split(" ")
     for x in c:
         z1.append(x)
         if x == "китайский":
            st.append(i)
 z = sorted(set(z1))

 print('Студенты знают ' + str(len(z)) + ' языков:' )
 print(z)
 print('Студенты, которые знают китайский:' )
 print(st)

d1()
d2()