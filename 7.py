# Задание 7
def area_circle(radius: int) -> int:
    PI = 3.14
    return PI * (radius ** 2)

rad = int(input('Введите радиус: '))
print(f'Площадь круга: {area_circle(rad)}')
