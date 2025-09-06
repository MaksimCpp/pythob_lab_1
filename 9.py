# Задание 9
def even_or_odd(num: int) -> str:
    return 'even' if num % 2 == 0 else 'odd'

num = int(input('Число: '))
print(f'Ваше число: {even_or_odd(num)}')
