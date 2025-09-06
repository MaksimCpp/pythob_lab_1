# Задание 6
num = int(input('Введите число: '))
table = ''
start, end = 1, 11

print('Таблица умножения:')
for i in range(start, end):
    print(f'{num} * {i} = {num * i}')
