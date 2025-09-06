# Задание 13
def sqrt(num: float, precision: float = 1e-10) -> float:
    if num < 0:
        raise ValueError("Нельзя извлечь корень из отрицательного числа")
    if num == 0:
        return 0
    
    x = num
    while True:
        root = 0.5 * (x + num / x)
        if abs(root - x) < precision:
            return root
        x = root

num = int(input('Введите число: '))
print(f'Корень: {sqrt(num)}')
