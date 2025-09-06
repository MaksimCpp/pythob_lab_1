# Задание 10
def factorial(num: int) -> int:
    if num <= 1:
        return 1
    return num * factorial(num - 1)

num = int(input("Введите число: "))
print(f'Факториал вашего числа: {factorial(num)}')
