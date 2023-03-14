types = input('Для начала операции нажмите любую клавишу, для завершения работы введите "выход" без кавычек')
while True:
    if types == 'выход':
        break
    else:
        print('Введите тип валюты (доллар, Евро, Рубль)')
        types = input()
        print('Во что хотите конвертировать валюту? (доллар, Евро, Рубль)')
        types2 = input()
        print('Введите число')
        num = input()
        num = float(num)


        def dollars_rubble ():
            p = num * 0.013
            return(round(p, 2))

        def rubble_dollars ():
            p = num * 76.20
            return(round(p, 2))

        def euro_rubble ():
            p = num * 0.013
            return(round(p, 2))

        def rubble_euro ():
            p = num * 81.13
            return(round(p, 2))

        def dollars_euro ():
            p = num * 0.94
            return(round(p, 2))

        def euro_dollars ():
            p = num * 1.06 
            return(round(p, 2))

        if types == 'доллар' and types2 == 'рубль':
            print(dollars_rubble())
        elif types == 'рубль' and types2 == 'доллар':
            print(rubble_dollars())
        elif types == 'евро' and types2 == 'рубль':
            print(euro_rubble())
        elif types == 'рубль' and types2 == 'евро':
            print(rubble_euro())
        elif types == 'доллар' and types2 == 'евро':
            print(dollars_euro())
        elif types == 'евро' and types2 == 'доллар':
            print(euro_dollars())
        elif types == 'доллар' and types2 == 'доллар':
            print(round(num, 2))
        elif types == 'евро' and types2 == 'евро':
            print(round(num, 2))
        elif types == 'рубль' and types2 == 'рубль':
            print(round(num, 2))
        else:
            print('Неверная операция, повторите сначала')
print('Работа завершена')
