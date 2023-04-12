interest_rate = 5
region = input("Введите название региона: ")
total_children = int(input("Введите количество детей в семье: "))
salary_project = input("Есть ли у клиента зарплатный проект в нашем банке? ")
insurance = input("Оформлено ли страхование у клиента в нашем банке? ")
if total_children > 3:
    interest_rate = interest_rate - 1
if salary_project.lower() == "да" or salary_project.lower() == "yes":
    interest_rate = interest_rate - 0.5
if insurance.lower() == "да" or insurance.lower() == "yes":
    interest_rate = interest_rate - 1.5
if region == "Дальний Восток":
    interest_rate = 2
print("Ваша процентная ставка:", interest_rate, "%")
