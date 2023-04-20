boys = input("Введите имена мальчиков (через пробел): ")
boys = boys.split()
girls = input("Введите имена девушек (через пробел): ")
girls = girls.split()
if len(boys) != len(girls):
    print("Кто-то может остаться без пары!")
else:
    print("Идеальные пары: ")
    for boy, girl in zip(sorted(boys), sorted(girls)):
        print(boy, "и", girl)
