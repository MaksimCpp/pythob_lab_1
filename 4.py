# Задание 4
def celsius_to_fahrenheit(celsius: int) -> int:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit}°F")