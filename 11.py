# Задание 11
def calculate_bmi(weight: float, height: float):
    return weight / (height ** 2)

def get_bmi_category(bmi: int):
    if bmi < 16:
        return "Выраженный дефицит массы тела"
    elif 16 <= bmi < 18.5:
        return "Недостаточная масса тела"
    elif 18.5 <= bmi < 25:
        return "Нормальная масса тела"
    elif 25 <= bmi < 30:
        return "Избыточная масса тела (предожирение)"
    elif 30 <= bmi < 35:
        return "Ожирение 1 степени"
    elif 35 <= bmi < 40:
        return "Ожирение 2 степени"
    else:
        return "Ожирение 3 степени"

user_weight = float(input('Ваш вес (кг): '))
user_height = float(input('Ваш рост (м): '))
user_bmi = calculate_bmi(user_weight, user_height)
print(f'Ваш ИМТ: {user_bmi}\nВаш диагноз: {get_bmi_category(user_bmi)}')

