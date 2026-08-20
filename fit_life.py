# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_LITER = 1000

user_name = input("Добро пожаловать в FitLife! Как вас зовут? ")
user_name = user_name.title()

while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        break
    except ValueError:
        print("Ошибка! Введите ваш возраст цифрами.")

user_weight = float(input("Напишите свой вес (в кг) "))
user_height = float(input("Укажите свой рост (в м, например 1.78) "))


# Подсчет bmi (Индекс массы тела)
bmi = round(user_weight / (user_height ** 2), 1)


# Подсчет нормы воды в мл.
water_ml = user_weight * WATER_PER_KG

# Подсчет нормы воды в литрах.
water_l = round(water_ml / ML_PER_LITER, 1)


print(f"""
Привет, {user_name}!
Твой индекс массы тела: {bmi}.
Рекомендуемая норма воды: {water_l} литра в день.

Расчет окончен. Будьте здоровы!""")
