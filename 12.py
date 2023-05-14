from tkinter import *
def z1():
    sort = ["шоколадное", "ванильное","клубничное"]
    meny1 = []
    meny2 = []
    #type = ["на палочке", "рожок", "брикет"]
    #p=[]
    dictionary = {"на палочке": sort,  "рожок": sort}
    #t = ()
    #u = dictionary.get("на палочке")
    #print(u)
    #for i in dictionary.values():
        #print(i)
    #print("шоколадное" in (u))

    #print(dictionary.values())
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня: {self.cuisine_type} ")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")

    newRestaurant = Restaurant("Паста-лопаста", "итальянская")
    #print(newRestaurant.restaurant_name)
    #print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()


    class IceCreamStand(Restaurant):
        def __init__(self, flavors,restaurant_name, cuisine_type, location, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.location  = location
            self.time = time


        def describe_icecream(self):
            print(f" {self.flavors}")

        def appendnew_icecream(self):
            (kol)= input("сколько вкусов хотите добавить? ")
            while int(kol) > 0:
                w = input("введите мороженое: ")
                meny2.append(w)
                kol = int(kol) - 1
            #print(meny2)

        def remow_icecream(self):
            kol = input("сколько вкусов хотите убрать? ")
            while int(kol) > 0:
                sort.remove(input("введите мороженое:"))
                kol = int(kol) - 1

        def new_icecream(self):
            n = input("убрать или добавить мороженое? если хотите убрать напишите -, если добавить + ")
            if n == "+" :
                kol = input("сколько позиций хотите добавить? ")
                while int(kol) > 0 :
                    w = input( "введите мороженое: ")
                    sort.append(w)

                    #IceCreamStanda.newtype_icecream()
                    kol=int(kol)-1
                    #dictionary[e] = w


            elif n == "-":
                kol = input("сколько позиций хотите убрать? ")
                while int(kol) > 0:
                    sort.remove(input("введите мороженое:"))
                    kol = int(kol) - 1

        def meny(self):
            for i in meny1:
                dictionary[i]=meny2

            print("Мороженое в ассортименте")
            print(dictionary)





        def newtype_icecream(self):
            n = input("убрать или добавить тип мороженого? если хотите убрать напишите -, если добавить + ")
            if n == "+" :
                kol = input("сколько позиций хотите добавить? ")
                while int(kol) > 0 :
                    e=(input( "введите тип мороженого: "))
                    kol=int(kol)-1
                    meny1.append(e)
                    #w=(input( "введите вид мороженного: "))
                    IceCreamStanda.appendnew_icecream()
                    IceCreamStanda.meny()
                    #dictionary[e]=w
                #print(meny1)


            elif n == "-":
                kol = input("сколько позиций хотите убрать? ")
                while int(kol) > 0:
                    e = (input("введите тип мороженого: "))
                    kol = int(kol) - 1
                    dictionary.pop(e)
                    # w=(input( "введите вид мороженного: "))
                    #IceCreamStanda.remow_icecream()
                    IceCreamStanda.meny()
        def n_ice(self):
            kol = input("сколько позиций хотите добавить? ")
            while int(kol) > 0:
                w = input("введите мороженое: ")
                sort.append(w)

        def nal_icecream(self):
            t = (input("введите тип, чтобы проверить его наличие ") in dictionary.keys())
            #print(t)
            if t == True:
                print("есть в наличии")

                i = (input("введите вид, чтобы проверить его наличие ") in dictionary.values())

                if i == True:
                    print("есть в наличии, вы можете сделать заказ")
                else:
                    print(" такого вкуса нет в наличии")
            else:
                print("нет в наличии")

            #print(sort)

                #print({self.flavors})
        def type_icecream(self):
            typ = (input(", введите тип мороженого, чтобы проверить его наличие ") in type)
            if typ == True:
                IceCreamStanda.describe_icecream()
            else:
                print("Такого типа мороженого нет в наличии")

        def describe_restaurant(self):
            print(f"Находится по адресу {self.location}, время работы: {self.time},базовые вкусы мороженого,которое вы можете попробовать в нашем ресторане: {self.flavors} ")

        def frame(self):
            root = Tk()
            root['bg'] = '#fafafa'
            root.title('Меню вкусов')
            root.geometry('300x250')
            root.resizable(width=False, height=False)

            canvas = Canvas(root, height=250, width=300)
            canvas.pack()

            frame = Frame(root, bg='#ffb876', bd=5)
            frame.place(relx=0.15, rely=0.15, relheight=0.7, relwidth=0.7)

            title = Label(canvas, text='Вкусы мороженого', bg='#fafafa', font=45)

            for i in self.flavors:
                item = Label(frame, text=i, bg='#ffb876', font=40)
                item.pack()
            title.pack()

            root.mainloop()

    IceCreamStanda = IceCreamStand(sort,"Пасталопаста", "Итальянская", " пер.Солнечный", "12:00 - 20:00")
    IceCreamStanda.describe_restaurant()
    IceCreamStanda.new_icecream()
    IceCreamStanda.frame()
    IceCreamStanda.describe_restaurant()
    IceCreamStanda.newtype_icecream()
    #IceCreamStanda.meny()

    #IceCreamStanda.new_icecream()
    #IceCreamStanda.nal_icecream()
    #IceCreamStanda.describe_icecream()
    #IceCreamStanda.newtype_icecream()
    #IceCreamStanda.describe_icecream()
    #IceCreamStanda.nal_icecream()








z1()