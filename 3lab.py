kol = input('введите колличество слов ')
i = 0
s = ""
while i < int(kol):
    a = input('')
    i+=1
    if i == 1 :
        s = str(s) +  str(a)
    else:
     s = str(s) +  " " + str(a)
   # s = str(s) + str(a) +", "
print (str(s))

def p1():
  # программа ведется до того момента как появится стоп
  #kol = input('введите колличество слов ')
 print("Введите слова, как только вы захотите преобразовать все их в список, введите stop")
 i = 0
 s = ""
 words =[]
 while (new_str := str(input())) != "stop":
    words.append(new_str)

 print(" ". join(words))

def p2():

  #Проверка на букву ф

 print("Вводи слова, попробуй отгадать редкие, если ты захочешь прекратить игры, напиши stop")
 while (new_str := str(input())) != "stop":
  if "ф" in new_str or "Ф" in new_str:
        print(" Ого! Это редкое слово!")
  else:
        print(" Эх, это не очень редкое слово...")

def p3():

 from random import randint


 print("Игра калькулятор. Если хотите завершить игру, введите слово stop")
 o=0
 c=0
 while True:
    a = randint(1, 100)
    b = randint(1, 100)
    print(f"{a}+{b}= ", end="")
    res = input()
    #проверяем на то, чтобы можно было вводить только число, иначе False
    while not res.isdigit() and res != "stop":
        print("Вы ввели что-то не то, повторите ввод")
        res = input()
    if res == "stop":
        break
    res = int(res)
    if a+b == res:
        print("Правильно!")
        c = c+1
    else:
        print("Ответ неправильный :(")
        o = o+1

    if o == 3:
        print(f"Игра окончена. Правильных ответов, {c}")
        break


p1()
p2()
p3()