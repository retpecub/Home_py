month = input("Введите месяц: ")
date = int(input("Введите число: "))
if month == "март" and date >= 21 or month =="апрель" and date <= 20:
    print("Овен")
elif month == "апрель" and date >= 21 or month =="май" and date <= 21:
    print("Телец")
elif month == "май" and date >= 22 or month =="июнь" and date <= 21:
    print("Близнецы")
elif month == "июнь" and date >= 22 or month =="июль" and date <= 22:
    print("Рак")
elif month == "июль" and date >=23 or month =="август" and date <=21:
    print("Лев")
elif month == "август" and date >=22 or month =="сентябрь" and date <=23:
    print("Дева")
elif month == "сентябрь" and date >=24 or month =="октябрь" and date <=23:
    print("Весы")
elif month == "октябрь" and date >=24 or month =="ноябрь" and date <=22:
    print("Скорпион")
elif month == "ноябрь" and date >=23 or month =="декабрь" and date <=22:
    print("Стрелец")
elif month == "декабрь" and date >=23 or month =="январь" and date <=20:
    print("Козерог")
elif month == "январь" and date >=21 or month =="февраль" and date <=19:
    print("Водолей")
elif month == "февраль" and date >=20 or month =="март" and date <=20:
    print("Рыбы")
