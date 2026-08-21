# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_LITER = 1000

user_name = ""

# Проверка на буквы в имени
while not user_name.isalpha():
    user_name = input("Добро пожаловать в FitLife! Как вас зовут? ")
    user_name = user_name.title()

    if not user_name.isalpha():
        print("Ошибка: имя должно содержать только буквы.")
# Проверка на возраст > 0
while True:
    try:
        user_age = int(input("Сколько вам лет? "))

        if user_age > 0:
            break
        else:
            print("Ошибка: возраст должен быть больше 0. Попробуйте снова.")

    except ValueError:
        print("Ошибка! Введите ваш возраст цифрами.")
# Проверка на вес > 0
while True:
    try:
        user_weight = float(input("Напишите свой вес (в кг) "))

        if user_weight > 0:
            break
        else:
            print("Ошибка: вес должен быть больше 0. Попробуйте снова.")

    except ValueError:
        print("Ошибка! Введите ваш вес цифрами.")
# Проверка на рост > 0
while True:
    try:
        user_height = float(input("Укажите свой рост (в м, например 1.78) "))

        if user_height > 0:
            break
        else:
            print("Ошибка: рост должен быть больше 0. Попробуйте снова.")
    except ValueError:
        print("Ошибка! Введите ваш рост цифрами.")
# Подсчет bmi (Индекс массы тела)
bmi = round(user_weight / (user_height ** 2), 1)


# Подсчет нормы воды в мл, вес на норму воды на кг.
water_ml = user_weight * WATER_PER_KG

# Подсчет нормы воды в литрах, перевод из мл в литры.
water_l = round(water_ml / ML_PER_LITER, 1)


print(f"""
Привет, {user_name}!
Твой индекс массы тела: {bmi}.
Рекомендуемая норма воды: {water_l} литра в день.

Расчет окончен. Будьте здоровы!""")

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
