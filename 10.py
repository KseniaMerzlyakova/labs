def d1 ():
    import json
    q = {}

    with open("5.json", "r", encoding="utf-8") as read_file:
        rf = json.load(read_file)
        #print(rf)
        for val in rf.values():
            s = input('Товар ')
            h = input('Цена ')
            d = input('Если товар есть в наличии введите: "True", если нет: "False" ')
            f = input('Вес ')
            q["Название"] = s
            q["Назв"] = h
            q["Назdв"] = d
            q["Наdfdзdв"] = f
            val.append(q)

            #print(val)
        for key in rf.keys():
            print(key)
        rf.clear()
        #print(rf)

        rf[key] = val
        #print(rf)
    #print(rf)
    with open("5.json", "w", encoding="utf-8") as write_file:
        json.dump(dict(rf), write_file)

    with open("5.json", "r", encoding="utf-8") as f:
        text = json.load(f)
    for key in text.keys():
        print(key)
    for val in text.values():
        print(val)
    for i in val:
        k = str(i).split()
        p = list(i.values())
        #print(p)
        name, cena, nalicie, massa = p
        if nalicie == ('True'):
            c = 'В наличии'
        else:
            c = 'нет в наличии'
        print('Название:', name)
        print('Цена:', cena)
        print('Вес', massa)
        print(c)
        print()
def d2 ():
    with open('e-r.txt', 'r', encoding="utf-8") as f2:
        f = ()
        p = ()
        d = {}
        n = []
        h = ''
        for line in f2:
            line = line.replace('\n', "")
            new_list = line.split('-')
            # print(new_list)
            with open('e-r.txt', 'a' , encoding="utf-8") as f2:
                #f2.write(new_list)
                d[new_list[1]] = new_list[0]
                list_keys = list(d.keys())
                list_keys.sort()
    for i in list_keys:
        a = (i, '-', d[i])
        j = (' '.join(a))
        print(j)
        with open('r-e.txt', 'a' ) as f2:
            f2.write(j + '\n')
    # print(h)
    # n += new_list
    # print(n)

#d1()
d2()
