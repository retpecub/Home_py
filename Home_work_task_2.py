month = input("Введите месяц: ")
date = int(input("Введите число: "))
if month == "март":
    if date >= 21:
        print("Овен")
    else:
        print('Рыбы')
if month == "апрель":
    if date >= 21:
        print("Телец")
    else:
        print('Овен')
if month == "май":
    if date >= 22:
        print("Близнецы")
    else:
        print('Телец')
if month == "июнь":
    if date >= 22:
        print("Рак")
    else:
        print('Близнецы')
if month == "июль":
    if date >= 23:
        print("Лев")
    else:
        print('Рак')
if month == "август":
    if date >= 24:
        print("Дева")
    else:
        print('Лев')
if month == "сентябрь":
    if date >= 23:
        print("Весы")
    else:
        print('Лев')
if month == "октябрь":
    if date >= 23:
        print("Скорпион")
    else:
        print('Весы')
if month == "ноябрь":
    if date >= 22:
        print("Стрелец")
    else:
        print('Скорпион')
if month == "декабрь":
    if date >= 22:
        print("Козерог")
    else:
        print('Стрелец')
if month == "январь":
    if date >= 21:
        print("Водолей")
    else:
        print('Козерог')
if month == "февраль":
    if date >= 20:
        print("Рыбы")
    else:
        print('Водолей')
