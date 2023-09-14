# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def notation10(num: int, base: int) -> str:
    digit: str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
    result: str = ''
    while num > 0:
        result = digit[num % base] + result
        num //= base
    return result

BIN: int = 2
OCT: int = 8
HEX: int = 16

number: int = int(input('Введите десятичное число: '))

print('Двоичное число =', notation10(number, BIN))
print('Проверка через bin():', bin(number))
print('Восьмеричное число =', notation10(number, OCT))
print('Проверка через oct():', oct(number))
print('Шестнадцатеричное число =', notation10(number, HEX))
print('Проверка через hex():', hex(number))
