# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def gcd_function(x, y) -> int:
    if(y == 0):
        return x 
    else: 
        return gcd_function(y, x % y)

def check_equal(p, q) -> str:
    gcd: int = gcd_function(p, q)
    if p % q == 0:
        return p // gcd
    return str(p // gcd) + '/' + str(q // gcd)

numerator1: int = int(input('Введите числитель первой дроби: '))
denominator1: int = int(input('Введите знаменатель первой дроби: '))
numerator2: int = int(input('Введите числитель второй дроби: '))
denominator2: int = int(input('Введите знаменатель второй дроби: '))

sum: str = check_equal(numerator1 * denominator2 + numerator2 * denominator1, denominator1 * denominator2)
power: str = check_equal(numerator1 * numerator2, denominator1 * denominator2)

print('Сумма дробей =', sum)
print('Проверка через Fraccion():', Fraction(numerator1, denominator1) + Fraction(numerator2, denominator2))
print('Произведение дробей =', power)
print('Проверка через Fraccion():', Fraction(numerator1, denominator1) * Fraction(numerator2, denominator2))
