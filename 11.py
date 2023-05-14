def z1():
    c = input( " Ваш ресторан сейчас открыт?(да/нет) ")
    #n = input(" Обновленный рейтинг ")
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, reiting):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.reiting = reiting

        #@classmethod
        #def ne_reiting(cls,reiting):
           # return cls(reiting == n )
            #print("Обновленный рейтинг :", n)

        def new_reiting(self):
            self.reiting = n
            print("Обновленный рейтинг :", n)

        def new_reiting1(self):
            self.reiting = n1
            print("Обновленный рейтинг :", n1)

        def new_reiting2(self):
            self.reiting = n2
            print("Обновленный рейтинг :", n2)

        def new_reiting3(self):
            self.reiting = n3
            print("Обновленный рейтинг :", n3)

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type}, рейтинг: {self.reiting} ")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")

        def close_restaurant(self):
            print("Ресторан сейчас закрыт")

    newRestaurant = Restaurant("kjhkj", "kuh", "7.0")
    n = input(" Обновленный рейтинг ")
    #newRestaurant11 = Restaurant.ne_reiting("bkjdfdj", "kuh", n)
    #print(newRestaurant11.reiting)


    newRestaurant1 = Restaurant(input(" Введите название ресторана "), input(" Введите кухню "), input(" рейтинг "))
    n1 = input(" Обновленный рейтинг ")
    u = input(" Ваш ресторан сейчас открыт?(да/нет) ")

    newRestaurant2 = Restaurant(input(" Введите название ресторана "), input(" Введите кухню "), input(" рейтинг "))
    n2 = input(" Обновленный рейтинг ")
    v = input(" Ваш ресторан сейчас открыт?(да/нет) ")

    newRestaurant3 = Restaurant(input(" Введите название ресторана "), input(" Введите кухню "), input(" рейтинг "))
    n3 = input(" Обновленный рейтинг ")
    #print(newRestaurant.restaurant_name)
    #print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

    newRestaurant.new_reiting()
    newRestaurant.describe_restaurant()

    newRestaurant1.describe_restaurant()
    if c == "да":
         newRestaurant1.open_restaurant()
    else:
        newRestaurant1.close_restaurant()
    newRestaurant1.new_reiting1()
    newRestaurant1.describe_restaurant()

    newRestaurant2.describe_restaurant()
    if u == "да":
        newRestaurant2.open_restaurant()
    else:
        newRestaurant2.close_restaurant()
    newRestaurant2.new_reiting2()
    newRestaurant2.describe_restaurant()

    newRestaurant3.describe_restaurant()
    if v == "да":
        newRestaurant3.open_restaurant()
    else:
        newRestaurant3.close_restaurant()
    newRestaurant3.new_reiting3()
    newRestaurant3.describe_restaurant()





z1()