from PIL import Image, ImageFilter
def p1():
    image = Image.open('1.jpg')
    cropped = image.crop((1,80,200,400))
    cropped.save('3.jpg')
    cropped.show('3.jpg')
def p2():

    from PIL import Image, ImageFont, ImageDraw
    dictionary = { "1":"пасха.jpg","2":"космос.jpg","3":"др.jpg" }
    a = input("Открытку на какой праздник вы бы хотели получить? Напишите цифру: 1, если на Пасху, 2, если на День Космонавтики и 3, если на др ")
    v = input("Какое имя добавить ? ")
    b = ()
    c = dictionary.keys()
    user = ()
    for i  in (c):
       if str (a) == i:
           key = i
           user = dictionary.get(key)
    with Image.open(user) as img:
     draw = ImageDraw.Draw(img)
     #img.show()
     font = ImageFont.truetype("arial_bold.ttf", 100)
     draw.text((50, 50), v+",", (0, 255, 0), font=font)
     img.save('sample.jpg')
     img.show()

p1(),p2()