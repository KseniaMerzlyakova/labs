from PIL import Image, ImageFilter
def p1():
 filename = ('натюрморт.jpg')
 with Image.open(filename) as img:
     img.show()
 width, height = img.size
 format = img.format
 mode = img.mode

 print("ширина:", width)
 print("высота:", height)
 print("формат:", format)
 print("цветовая модель:", mode)

def p2():
    from PIL import Image, ImageFilter
    filename = ('натюрморт.jpg')
    with Image.open(filename) as img:
        res_img2 = img.reduce(3)
    res_img2.show()
    res_img2.save('mini.jpg')
    res_img3 = res_img2.transpose(Image.FLIP_LEFT_RIGHT)
    res_img3.show()
    res_img3.save('minireflac.jpg')
    res_img4 = res_img2.transpose(Image.ROTATE_180)
    res_img4.show()
    res_img4.save('minirot.jpg')

def p3():
    from PIL import Image, ImageFilter
    filename = ('1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg')
    for i in filename:
        with Image.open(i) as img:
            img_g = img.filter(ImageFilter.CONTOUR)
            img.show()
            img_g.show()
            img_g.save('filters/' + str(i))

def p4():
    from PIL import Image, ImageFilter
    filename = ('12.jpg', 'натюрморт.jpg')
    r1 = Image.open('13.png')
    for i in filename:
        with Image.open(i) as img:
            img.paste(r1, (100, 100), r1)
            img.show()


p1(),p2(),p3(),p4()